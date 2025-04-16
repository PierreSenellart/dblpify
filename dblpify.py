#!/usr/bin/env python3

import bibtexparser
import json
import re
import requests
import sys
import urllib.parse

def clean_string(s):
    s = re.sub(r'\\href{.*}{(.*)}', r'\1', s, flags=re.DOTALL)
    s = re.sub(r'\\[a-z]+', r'', s)
    s = re.sub(r'[{}]', r'', s)
    return(s)

def extract_last_names(a):
    for x in re.split(r' +and +', a):
        if(re.match(r',', x)):
            yield re.sub(r',.*', '', x, flags=re.DOTALL)
        else:
            yield re.sub(r'.* ', '', x, flags=re.DOTALL)

def process_content(content):
    library = bibtexparser.loads(content)
    for e in library.get_entry_list():
        original_id = e['ID']
        if re.match('^DBLP:', original_id):
            id=re.sub('^DBLP:', '', original_id)
        else:
            title = clean_string(e['title'])
            if 'author' not in e:
                print("Author missing for title “%s”"%(title), sys.stderr)
                print(content)
                continue
            ln = extract_last_names(e['author'])
            query = title + ' ' + ' '.join(ln)
            response = requests.get('https://dblp.org/search/publ/api?q='+urllib.parse.quote_plus(query)+'&h=1&format=json')
            try:
                response.raise_for_status()
                j = json.loads(response.content)
                id = j['result']['hits']['hit'][0]['info']['key']
            except:
                id = None

        if id != None:
            response = requests.get('https://dblp.org/rec/'+id+'.bib')
            try:
                response.raise_for_status()
                content=re.sub(r'^(@.*){(.*),', r'\1{'+original_id+',', response.text)
            except:
                pass
        print(content)

with open('/dev/stdin') as input:
    content=''
    for line in input.read():
        if re.match(r'^ *@', line) and content!='':
            process_content(content)
            content=''
        content+=line
    process_content(content)


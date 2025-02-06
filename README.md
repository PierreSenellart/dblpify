# dblpify

[DBLP](https://dblp.org/) is a curated open bibliography database specialized for computer science. Compared to other bibliography sources (scholarly search engines such as [Google Scholar](https://scholar.google.com/), [Crossref](https://community.crossref.org), or even publishers' Web sites and digital libraries), it usually has cleaner and more consistent information.

This project provides a quick-and-dirty script that uses the DBLP API to clean up and make uniform references in a BibTeX file provided on the standard input. References are matched based on the title and author last names, as interpreted by the search function of the DBLP API. Keys used in the BibTeX files are left unchanged.

It is good enough for simple cases but will definitely fail at complex cases; also check the resulting DBLP entries, some may not be perfect.

## Prerequisites

This is a Python 3 script that depends on one external library: [bibtexparser](https://pypi.org/project/bibtexparser/).

## Usage

```bash
python3 dblpify.py < input.bib > output.bib
```

## License

dblpify is provided as open-source software under the MIT License. See [LICENSE](LICENSE).

## Contact

<https://github.com/PierreSenellart/provsql>

Pierre Senellart <pierre@senellart.com>

Bug reports and feature requests are preferably sent through the *Issues* feature of GitHub.

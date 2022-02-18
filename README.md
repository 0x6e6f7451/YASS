# YASS - Yet Another Shodan Scraper
Simple python script for scraping/filtering shodan.io search, code kept short and scrambled quickly for capability showcase purposes.

## Usage
`python3 main.py`

`Search> "your desired search criteria"` without quotation marks.

Output is sent to `scraper-output.txt`

## Caveats
Personal API key is removed for security reasons. If you want to use this script you'll have to [generate your own](https://developer.shodan.io/api/requirements) and edit the `key` value in `/src/scrape.py`.

## References
* [Shodan official python library](https://shodan.readthedocs.io)
* [Shodan REST API reference](https://developer.shodan.io/api)
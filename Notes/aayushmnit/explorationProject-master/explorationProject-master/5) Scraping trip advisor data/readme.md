## Scraping trip advisor restaurant review data

An example of how we can scrape a website using Python beautiful soup. This case we will be scraping a restaurant reviews whose home page link is given [here](https://www.tripadvisor.com/Restaurant_Review-g60763-d477541-Reviews-Rice_to_Riches-New_York_City_New_York.html).

## Getting started
1) Open python interpreter
2) `python <filepath/tripadvisor.py> - outputpath "path/<filename>.csv" -url_path <restaurant home page url>`
3) Example `python Trip_advisor.py -output_path "C:/Users/100967/Desktop/Work/tripadvisor/data.csv" -url_path https://www.tripadvisor.com/Restaurant_Review-g60763-d8483826-Reviews-Gabriel_Kreuther-New_York_City_New_York.html`

## Requirements
- **Python 2.7**
- **Libraries** - Pandas, numpy, BeautifulSoup, urllib2, argparse, unicodedata

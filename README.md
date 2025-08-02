# Semi-Auto-Image-Scraper
Make manual image scraping easier and more streamlined

## Input Config Args Syntax
python semiAuto.py \<inputCSV> \<wordColumnName> \<imgsPerWord><br/>
**inputCSV** - csv holding words<br/>
**wordColumnName** - name of column within csv holding all words<br/>
**imgsPerWord** - number of images desired per word<br/>

## Hard Coded Config Args Syntax
**URL_PREFIX** - parent link for words from CSV to be attached to<br/>
**OUTPUT_CSV** - name of output CSV<br/>
**POLL_INTERVAL** - time (in seconds) scraper will wait before check clipboard for new additions<br/>

## Instructions
*Works best with split screen, with search engine on one side and console on the other.*
1. Run scraper
2. Ctrl + Click the link provided by the scraper (or whatever keyboard shortcut your system take to open links from console)
3. Copy image addresses of any images desired (go slow not too fast)
4. When desired number of images is reached, scraper will auto move onto the next word.
5. Repeat until all words are scraped for, after which the script will save the csv with words and their image addresses.

###### Created with the assistance of AI

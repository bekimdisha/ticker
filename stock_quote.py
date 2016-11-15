#!/usr/bin/python

import urllib
import re

def get_stock_quote(ticker_symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + ticker_symbol).read()
    m = re.search('id="ref_(.*?)">(.*?)<', content)
    if m:
        quote = m.group(2)
    else:
        quote = 'no quote available for: ' + ticker_symbol
    return quote

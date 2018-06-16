#!/usr/bin/python
import json
import random
import sys
import time
import re
import argparse
import yaml
from urllib2 import Request, urlopen

def buildUrl(symbols):
    symbol_list = ','.join([symbol for symbol in symbols])
    # a deprecated but still active & correct api
    return 'http://finance.google.com/finance/info?client=ig&q=' \
        + symbol_list
		
def request(symbols):
    url = buildUrl(symbols)
    req = Request(url)
    resp = urlopen(req)
    # remove special symbols such as the pound symbol
    content = resp.read().decode('ascii', 'ignore').strip()
    content = content[3:]
    return content

def replaceKeys(quotes):
    global googleFinanceKeyToFullName
    quotesWithReadableKey = []
    for q in quotes:
        qReadableKey = {}
        for k in googleFinanceKeyToFullName:
            if k in q:
                qReadableKey[googleFinanceKeyToFullName[k]] = q[k]
        quotesWithReadableKey.append(qReadableKey)
    return quotesWithReadableKey
	
googleFinanceKeyToFullName = {
    u'id'     : u'ID',
    u't'      : u'StockSymbol',
    u'e'      : u'Index',
    u'l'      : u'LastTradePrice',
    u'l_cur'  : u'LastTradeWithCurrency',
    u'ltt'    : u'LastTradeTime',
    u'lt_dts' : u'LastTradeDateTime',
    u'lt'     : u'LastTradeDateTimeLong',
    u'div'    : u'Dividend',
    u'yld'    : u'Yield',
    u's'      : u'LastTradeSize',
    u'c'      : u'Change',
    u'cp'      : u'ChangePercent',
    u'el'     : u'ExtHrsLastTradePrice',
    u'el_cur' : u'ExtHrsLastTradeWithCurrency',
    u'elt'    : u'ExtHrsLastTradeDateTimeLong',
    u'ec'     : u'ExtHrsChange',
    u'ecp'    : u'ExtHrsChangePercent',
    u'pcls_fix': u'PreviousClosePrice'
}


def main():

	parser = argparse.ArgumentParser(__file__, description="Google Finance Data Fetcher (real-time, no-delay)")
	parser.add_argument("--output", "-o", help="Output channel for fetched data. When <CONSOLE> (default), output is returned to stdout; when <LOG> it's written into a 'gfin_' prefixed text file.", choices=['LOG','CONSOLE'] )
	parser.add_argument("--num", "-n", help="Number of fetch event (0 for infinite)", type=int, default=1)
	parser.add_argument("--delay", "-d", help="Delay between data fetches", default=0.0, type=float)
	parser.add_argument("--symbol", "-s", help="Stock symbol", default=0.0, type=str)

	timestr = time.strftime("%Y%m%d-%H%M%S%s")
	fname = 'gfin_data_'+timestr+'.txt'

	args = parser.parse_args()
	f = open(fname,"w") if args.output=='LOG' else sys.stdout
	
	flag = True
	lines = args.num
        while (flag):
		a = replaceKeys(json.loads(request([args.symbol])))
        	b = map(lambda x: yaml.safe_load(a[0][x]),
			["ID","StockSymbol","LastTradePrice","ChangePercent","LastTradeSize","LastTradeWithCurrency","LastTradeDateTime","LastTradeTime","PreviousClosePrice","Index"])
        	f.write("\t".join(map(lambda x: str(x),b)) + "\n")
        	time.sleep(args.delay)
        	lines = lines - 1
        	flag = False if lines == 0 else True

if __name__ == "__main__":
	main()
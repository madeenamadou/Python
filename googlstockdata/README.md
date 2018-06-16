# googlstockdata
A python module to conveniently fetch real-time (no delay) stocks market data from Google Finance API.

This python module retrieves real-time stocks market data from Google Finance API. It is inspired by the [googlefinance](https://github.com/hongtaocai/googlefinance) module, which does not inherently enable to collect a continuous stream of data nor to store the data in a file. This module, however, is more user-friendly in many ways:

* generate an infinite stream of data
* directly inject the data as it arrives into a tab-separated txext file, to facilitate further ingestion and analysis
* adjust the lap time between data fetch events
* define a specific number of fecth events

I find it very useful for streaming data ingest and/or analytics. BTW I originally developped it to run a data analytics app on Amazon Web Services.


## Installation
Please, mind that this program was developped under Python 2.7.

```
git clone https://github.com/madeenamadou/googlstockdata
cd googlstockdata
pip install -r requirements.txt
```


## Dedicated help
```
s-4.2# python googlstockdata.py --help
usage: googlstockdata.py [-h] [--output {LOG,CONSOLE}] [--num NUM]
                         [--delay DELAY] [--symbol SYMBOL]

Google Finance Data Fetcher (real-time, no-delay)

optional arguments:
  -h, --help            show this help message and exit
  --output {LOG,CONSOLE}, -o {LOG,CONSOLE}
                        Output channel for fetched data. When <CONSOLE>
                        (default), output is returned to stdout; when <LOG>
                        it's written into a 'gfin_' prefixed text file.
  --num NUM, -n NUM     Number of fetch event (0 for infinite)
  --delay DELAY, -d DELAY
                        Delay between data fetches
  --symbol SYMBOL, -s SYMBOL
                        Stock symbol
```


## Usage examples
Perform two retrievals of Apple stock data from NASDAQ, at half-a-second interval.
```
sh-4.2# python googlstockdata.py -n 2 -o CONSOLE -s AAPL -d 0.5
22144   AAPL    NASDAQ  147.48  2017-06-09 14:52:21     147.48  2:52PM EDT      Jun 9, 2:52PM EDT
22144   AAPL    NASDAQ  147.48  2017-06-09 14:52:21     147.48  2:52PM EDT      Jun 9, 2:52PM EDT
```

Generate an infinite stream of the Apple stock data from NASDAQ, at half-a-second interval.
```
sh-4.2# python googlstockdata.py -n 0 -o CONSOLE -s AAPL -d 0.5
22144   AAPL    NASDAQ  147.48  2017-06-09 14:52:21     147.48  2:52PM EDT      Jun 9, 2:52PM EDT
22144   AAPL    NASDAQ  147.48  2017-06-09 14:52:21     147.48  2:52PM EDT      Jun 9, 2:52PM EDT
...
```


## License
This program is released under the [MIT](/LICENSE) license.


## Reference
The [googlefinance](https://github.com/hongtaocai/googlefinance) module, by Hongtao Cai.



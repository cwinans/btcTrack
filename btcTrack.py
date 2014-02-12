import re
import urllib2
from datetime import datetime


def main():

    # find current conversion rate
    pageData = urllib2.urlopen('http://www.coinbase.com').read()
    foundPrice = re.search('Current Buy Price:\s+\$(\d+.\d\d)', pageData)
    if foundPrice:
        currentPrice = foundPrice.group(1)

        # get current date and time
        collectionDatTime = datetime.utcnow().strftime('%Y%m%d%H%M')

        # append to CSV file
        f = open('btcTrack.csv', 'a')
        f.write(collectionDatTime+','+currentPrice+'\n')
        f.close()

if __name__ == '__main__':
    main()
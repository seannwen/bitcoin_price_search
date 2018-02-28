import requests
from bs4 import BeautifulSoup


def bitstamp_price():

    bitstamp_page = requests.get('https://bitcoinwisdom.com/markets/bitstamp/btcusd')
    bitstamp_soup = BeautifulSoup(bitstamp_page.text, "html.parser")

    coinbase_page = requests.get('https://bitcoinwisdom.com/markets/coinbase/btcusd')
    coinbase_soup = BeautifulSoup(coinbase_page.text, "html.parser")

    bitstamp_bit_price = bitstamp_soup.find('div', id='price').text
    coinbase_bit_price = coinbase_soup.find('div', id='price').text

    print 'Bitstamp BTC/USD: ${}'.format(bitstamp_bit_price)
    print 'Coinbase BTC/USD: ${}'.format(coinbase_bit_price)


def bitfinex_price():

    bitfinex_page = requests.get('https://www.bitfinex.com/trading')
    bitfinex_soup = BeautifulSoup(bitfinex_page.text, 'html.parser')

    # print bitfinex_soup.find('tbody', {'tr': 'col-info'})
    # bitfinex_bit_price = bitfinex_soup.find('td', {'data-pair': 'BTCUSD'})
    # print bitfinex_bit_price


def gdax_price():

    gdax_page = requests.get('https://www.gdax.com/trade/BTC-USD')
    gdax_soup = BeautifulSoup(gdax_page.text, "html.parser")

    # print gdax_soup.prettify()
    gdax_bit_price = gdax_soup.find('span', {'class': 'MarketInfo_market-num_1lAXs'})
    # print gdax_bit_price


if __name__ == "__main__":

    bitstamp_price()
    # bitfinex_price()
    gdax_price()

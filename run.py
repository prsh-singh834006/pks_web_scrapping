import sys
from urllib import request
import csv
from bs4 import BeautifulSoup


def web_scrap(kw='as'):
    page = request.urlopen('http://shopping.com/products?KW={}'.format(kw))
    soup = BeautifulSoup(page, 'html.parser')
    deals = soup.find_all('div', 'deal')

    with open('deals.csv', 'w', newline='') as csvFile:
        fieldnames = ['item_name', 'price']
        writer = csv.DictWriter(csvFile, fieldnames)
        writer.writeheader()
        for i in deals:
            item_name = i.find('a', 'productName').span.get_text()
            price = i.find('span', 'productPrice').a.get_text()
            writer.writerow({
                'item_name': item_name,
                'price': price
            })


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
        web_scrap(kw=arg)
    except (TypeError, ValueError, FileNotFoundError, FileExistsError) as e:
        print('Something went bad :)')
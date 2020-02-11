#!/usr/bin/env python3
from urllib.request import urlopen
import bs4

class Client_Web(object):
    def __init__(self):
        pass

    def do_request(self,str="https://www.banggood.com/es/flashdeals.html"):
        file = urlopen(str)
        data = file.read()
        file.close()
        return data

    def process_all_products(self,html):
        tree = bs4.BeautifulSoup(html,features="lxml")
        self.print_product_information(self.get_titles(tree),self.get_prices(tree))


    def get_titles(self,tree):
        list_product = []
        products = tree.find_all("span", "title")

        for product in products:
            list_product.append(product.find("a").text)

        return list_product

    def get_prices(self,tree):
        list_prices = []
        price_items = tree.find_all("div", "priceitem")

        for price in price_items:
            if price.find("span","price_old") is None:
                list_prices.append((price.find("span", "price").text, "None"))
            else:
                list_prices.append((price.find("span","price").text,price.find("span","price_old").text))

        return list_prices

    def print_product_information(self, list_product, list_prices):
        for index in range(len(list_prices)):
            percentage = 100 - (list_prices[index][0]*100)/list_prices[index][1]
            print("Product name: ", list_product[index],
                  "\nCurrent price: ", list_prices[index][0],
                  "\nOld price: ",list_prices[index][1],
                  "\nApplied discount: ", discount)
            print("\n")


    def run(self):
        data = self.do_request()
        self.process_all_products(data)

if __name__=="__main__":
    client = Client_Web()
    client.run()

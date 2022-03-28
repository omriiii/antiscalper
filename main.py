
import time
import requests
from time import sleep
import webbrowser
from playsound import playsound
from urllib.parse import urlparse
import json
import sys
import threading

from bs4 import BeautifulSoup



def getPage(url):
    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Referer": "https://google.com",
            "Upgrade-Insecure-Requests": "1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }

    try:
        r = requests.get(url=url, timeout=10, headers=header)

        if r.status_code == 200:
            return r.content.decode("utf-8")
    except:
        print("Exception...")
        return None

def getUrlDomain(url):
    return urlparse(url).netloc

def getProducts(url):
    temp = getPage(url)
    while temp == None:
        sleep(3)
        temp = getPage(url)
    html = temp

    soup = BeautifulSoup(html, 'html.parser')
    products = []
    domain = getUrlDomain(url)

    if domain == "www.bhphotovideo.com":
        products_div = soup.findAll("div", {"data-selenium": "miniProductPage"})
        for tag in products_div:
            price = 0 # Placeholder
            prix_tag = tag.findChildren("span", {"data-selenium": "uppedDecimalPriceFirst"} )
            if len(prix_tag) > 0:
                price = float(prix_tag[0].text.replace(",", "").split("$", 1)[1])
            purchasable = "Add to Cart" in tag.findChildren("div", {"data-selenium": "miniProductPageProductConversion"})[0].text
            a_tag = tag.findChildren("a", {"data-selenium": "miniProductPageProductNameLink"})[0]
            name = a_tag.text
            link = domain + a_tag.attrs["href"]
            products.append({"name": name, "price": price, "link": link, "purchasable": purchasable})

    if domain == "www.bestbuy.com":
        products_div = soup.findAll("div", {"class": "shop-sku-list-item"})
        for tag in products_div:
            price = float(tag.findChildren("div", {"class": "priceView-hero-price"} )[0].text.split("$")[2])
            purchasable = tag.findChildren("button", {"class": "add-to-cart-button"} )[0].text == "Add to Cart"
            a_tag = tag.findChildren("div", {"class": "sku-title"} )[0].findChildren("a")[0]
            name = a_tag.text
            link = domain + a_tag.attrs["href"]
            products.append({"name": name, "price": price, "link": link, "purchasable": purchasable})

    if domain == "www.newegg.com":
        products_div = soup.findAll("div", {"class": "item-cell"})
        for tag in products_div:
            if len(tag.findChildren("a", {"class": "txt-ads-box"})) == 0:
                price = 0 # They don't show the price of the product in the page HOWEVER the query url makes sure all the items we're purchasing are within budget :)
                purchasable = True
                temp = tag.findChildren("p", {"class": "item-promo"} )
                if len(temp) > 0:
                    if temp[0].text == "OUT OF STOCK":
                        purchasable = False
                a_tag = tag.findChildren("a", {"class": "item-title"} )[0]
                name = a_tag.text
                link = a_tag.attrs["href"]
                products.append({"name": name, "price": price, "link": link, "purchasable": purchasable})

    if domain == "www.amazon.com":
        products_div = soup.findAll("div", {"class": "s-result-item"})
        for tag in products_div:
            price = 0 # They don't show the price of the product in the page HOWEVER the query url makes sure all the items we're purchasing are within budget :)
            purchasable = False
            temp = tag.findChildren("span", {"class": "a-price-whole"})
            if len(temp) > 0:
                purchasable = True
                price = float(temp[0].text)
            a_tag = tag.findChildren("a", {"class": "a-text-normal"})[0]
            name = a_tag.text
            link = a_tag.attrs["href"]


            products.append({"name": name, "price": price, "link": link, "purchasable": purchasable})

    if config["print_queries"]:
        print("\r" + domain[4:-4])
        for product in products:
            print("    " + str(product["purchasable"]).ljust(6) + str(product["price"]).ljust(9) + product["name"].ljust(100)  + product["link"].ljust(100))
    return products


def main(config):
    while True:
        for query_url in config["query_urls"]:
            products = getProducts(query_url)
            for product in products:
                if product["purchasable"] and (config["product_name"] in product["name"].lower()) and (product["price"] <= config["max_budget"]):
                    print(product["link"])
                    webbrowser.open(product["link"])
                    playsound('The Giant Enemy Spider.mp3')
                    playsound('The Giant Enemy Spider.mp3')
                    playsound('The Giant Enemy Spider.mp3')
                    exit()
        sleep(config["refresh_rate"])


default_config = { }
default_config["refresh_rate"] = 10 # In seconds
default_config["max_budget"] = 700
default_config["product_name"] = "geforce rtx 3070"
default_config["print_queries"] = True
default_config["query_urls"] =  [
        "https://www.amazon.com/s?k=geforce+rtx+3070&rh=p_36%3A50000-70000",
        "https://www.bhphotovideo.com/c/search?Ntt=rtx%203070",
        "https://www.bestbuy.com/site/searchpage.jsp?st=rtx+3070",
        "https://www.newegg.com/p/pl?d=Geforce+RTX+3070&PageSize=96&LeftPriceRange=0+" + str(default_config["max_budget"]),
        ]

def drawSpinny():
    arr = [ "/", "-", "\\", "|" ]

    cntr = 0
    while True:
        sys.stdout.write(arr[ cntr ])
        sys.stdout.flush()
        cntr = (cntr + 1) % len(arr)
        time.sleep(0.1)
        sys.stdout.write('\b')

if __name__ == "__main__":

    # Config Stuff
    config = default_config
    if(len(sys.argv) > 1):
        config_file = sys.argv[1]
        f = open(config_file, "r")
        config = json.loads(f.read())

    if not config["print_queries"]:
        spinny_thread = threading.Thread(target=drawSpinny, daemon=True)
        spinny_thread.start()
        
    # Test Existing Code (maybe something is broken!!)
    for query_url in config["query_urls"]:
        try:
            getProducts(query_url)
        except:
          print("\nThe template for " + query_url.split("://")[1].split("/")[0] + " has changed.") 
          print("Please update this script/contact it's developer to fix it.")
          exit()
    
    # Run
    main(config)
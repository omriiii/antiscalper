# antiscalper
This is a program I made to help me buy a Geforce RTX 3070!

### Note & Disclaimer
Please don't use this for scalping. Scalpers are scum.
By using this program you run the risk of having your IP address banned from these storefronts while using this program. (This can be circumvented by using a proxy but I'm lazy)

As of right now, this program will only work with Newegg, B&H and BestBuy. You'll also need Python installed.

### How does it work?
This program will go to a set of storefront links (eg. Amazon, Newegg) and give you back if any of the products in those store fronts are purchaseable.
If they are, the program will open up the page in your default browser and play a little song to notify you.

## How to run it
## 1. configure `config.json`

`refresh_rate` -- The rate at which your computer will query all pages (in seconds).

`product_name` -- Product name of what you wish to buy (Duh).

`max_budget`   -- Maximum amount of dollars you're willing to spend on a purchasable product.

`query_urls`   -- All the storefront links you want to check every `refresh_rate` seconds.


## 2. install dependecies
Open up a terminal/command line, change directories to this project's directory and insert the following command:
```
pip install -r requirements.txt
```

## 3. run!
Just click on `run.bat` and you're set. Good luck on getting your product.

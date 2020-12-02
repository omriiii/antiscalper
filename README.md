# antiscalper
This is a program I made to help me buy a Geforce RTX 3070!

### Note & Disclaimer
*Please don't use this for scalping.* ***Scalpers are scum.***

By using this program you run the risk of having your IP address banned from these storefronts. (This can be circumvented by using a proxy but I'm lazy)

To get this to run you'll need [Python](https://www.python.org/downloads/) installed and make sure its [added to your enviorment variables](https://cdn.discordapp.com/attachments/782031383501078538/782050193892966462/gRyw8.png).

### How does it work?
This program will go to a set of storefront links (eg. Amazon, Newegg) and give you back if any of the products in those store fronts are purchaseable.
If they are, the program will open up the page in your default browser and play a little song to notify you.

## How to run it
### 1. configure `config.json`

`refresh_rate` -- The rate at which your computer will query all pages (in seconds).

`product_name` -- Product name of what you want to buy (Duh).

`max_budget`   -- Maximum amount of dollars you're willing to spend on a purchasable product.

`query_urls`   -- All the storefront links you want to check every `refresh_rate` seconds. (Only supports Newegg, B&H and BestBuy)

### 2. install dependecies
Run `install-reqs.bat`.

### 3. run!
Run `run.bat` and you're set! Good luck on getting your product.

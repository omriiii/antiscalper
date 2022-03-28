# antiscalper
This is a program I made to help me buy a Geforce RTX 3070!

***NOTE: As of March 2022 (or potentially earlier), this code is outdated. 
If you wish to use this tool, you'd would need to update the HTML parsing function (`getProducts(url)`) to parse the new website's HTML template.***

### Note & Disclaimer
*Please don't use this for scalping.* ***Scalpers are scum.***

By using this program you run the risk of having your IP address banned from these storefronts. (This can be circumvented by using a proxy but I'm lazy)

To get this to run you'll need [Python](https://www.python.org/downloads/) installed and make sure it's [added to your enviorment variables](https://cdn.discordapp.com/attachments/782031383501078538/782050193892966462/gRyw8.png).

### How does it work?
This program will go to a set of storefront links (eg. Amazon, Newegg) and give you back if any of the products in those store fronts are purchaseable.
If they are, the program will open up the page in your default browser and play a little song to notify you.

## How to run it
### 1. configure `config.json`

`refresh_rate` -- The rate at which your computer will query all pages (in seconds).

`product_name` -- Product name of what you want to buy (Duh).

`max_budget`   -- Maximum amount of dollars you're willing to spend on a purchasable product.

`query_urls`   -- All the storefront links you want to check every `refresh_rate` seconds. (Only supports Newegg, B&H and BestBuy)

** An example `config.json` file is in this repository (It's the same one I used to get my 3070)

### 2. install dependecies
Run `install-reqs.bat`.

### 3. run!
Run `run.bat` and you're set! Good luck on getting your product.

## Troubleshooting 
If you've been running the bot for some time and things don't work then try these! 
1. You can verify the bot work by asking the bot to find something that IS in stock (eg. usb/hdmi cable are always in stock generally). You'd have to modify `config.json` to look for these items obviously. 
2. Your IP address has been blacklisted (temporarily or permanently). You can verify this by just going to that website in your own browser (eg. Chrome/Firefox/Safari) and seeing if you get blocked or not. From my experience B&H will put you a temporary "naughty list" that asks you do to a captcha when you visit their site. I'm not sure about Newegg and BestBuy. 
3. The templating of these websites has changed and I need to update the bot for it -- in which case, [message me on Twitter (@omrii_)]((https://twitter.com/omrii_)) or create an [Issue in this repo](https://github.com/omriiii/antiscalper/issues).

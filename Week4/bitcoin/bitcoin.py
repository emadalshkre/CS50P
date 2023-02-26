import json
import sys
import requests

def isfloat(st:str):
    try:
        float(st)
        return True
    except ValueError:
        return False

# check if comand_line is wroung input or not
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit() 
elif not isfloat(sys.argv[1]):
    print("Command-line argument is not a number")
    sys.exit()
#

#
p = {"time":{"updated":"Feb 24, 2023 14:16:00 UTC","updatedISO":"2023-02-24T14:16:00+00:00","updateduk":"Feb 24, 2023 at 14:16 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"23,733.3031","description":"United States Dollar","rate_float":23733.3031},"GBP":{"code":"GBP","symbol":"&pound;","rate":"19,831.3582","description":"British Pound Sterling","rate_float":19831.3582},"EUR":{"code":"EUR","symbol":"&euro;","rate":"23,119.7023","description":"Euro","rate_float":23119.7023}}}
#

#take key
for iterate in p["bpi"]["USD"]:
        if iterate == "rate":
            price = p["bpi"]["USD"][iterate]
#

price = float(price.replace(",", ""))
amount = price * float(sys.argv[1])
print(f"{amount:,.4f}")

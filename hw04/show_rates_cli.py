from utils import currency_rates
import sys

if len(sys.argv) > 1 and len(sys.argv[1]) == 3:
    currency_rate = currency_rates(sys.argv[1])
    if currency_rate["Value"] is None:
        print("Currency not found")
    else:
        print(f"Date: {currency_rate['Date']} rate: {currency_rate['Value']}")



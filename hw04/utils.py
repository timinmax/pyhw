import requests
import xmltodict
import xml
from datetime import datetime


def currency_rates(curr_code):
    data_to_return = {"Date": None, "Value": None}
    currency_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    try:
        raw_xml = requests.get(currency_url)
    except requests.exceptions.ConnectionError:
        print("Connection Error")
        return data_to_return
    try:
        currency_data = xmltodict.parse(raw_xml.content)
    except xml.parsers.expat.ExpatError:
        print("Parse error")
        return data_to_return

    data_to_return["Date"] = datetime.strptime(currency_data["ValCurs"]["@Date"], "%d.%m.%Y")
    for curr_rate in currency_data["ValCurs"]["Valute"]:
        if curr_rate["CharCode"].lower() == curr_code.lower():
            data_to_return["Value"] = curr_rate["Value"]

    return data_to_return


if __name__ == "__main__":
    usd_rate = currency_rates("USD")
    eur_rate = currency_rates("EUR")

    print(usd_rate)
    print(eur_rate)


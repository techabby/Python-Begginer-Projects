import requests


def ExchangeRate(BaseCurrency, TargetCurrency):
    url = f"https://api.exchangerate-api.com/v4/latest/{BaseCurrency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ExchangeRates = data["rates"][TargetCurrency]
        return ExchangeRates
    else:
        return None


def Convert(Amount, ExchangeRates):
    return Amount * ExchangeRates


def main():
    BaseCurrency = input("Enter the currency you want to convert: ")
    TargetCurrency = input("Enter the currency you want to convert in: ")
    Amount = float(input("Enter the amount of currency you want to convert: "))
    ExchangeRates = ExchangeRate(BaseCurrency, TargetCurrency)
    if ExchangeRates is not None:
        ConvertedCurrency = Convert(Amount, ExchangeRates)
        print(
            f"{Amount} {BaseCurrency} is converted to {ConvertedCurrency} {TargetCurrency}"
        )
    else:
        print("Unable to convert. Please try again later!")


main()

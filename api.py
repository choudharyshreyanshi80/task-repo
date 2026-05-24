import requests

base= input("Enter base currency (USD): ")
target= input("Enter target currency (INR): ")
url = f"https://api.exchangerate-api.com/v4/latest/{base}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    print("\nCURRENCY EXCHANGE DETAILS")
    print("\nBase Currency:", base)
    print("Target Currency:", target)
    print("Exchange Rate:", data['rates'][target])
    print("Date:", data['date'])
    print("\nSome Other Currency Rates:")
    print("EUR:", data['rates']['EUR'])
    print("GBP:", data['rates']['GBP'])
    print("JPY:", data['rates']['JPY'])

except requests.exceptions.RequestException as e:
    print(e)
except KeyError:
    print("Invalid Currency Code")
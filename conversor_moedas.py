from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()

print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)

# Format the result with two decimal places
formatted_result = "{:.2f}".format(result)

print(formatted_result)
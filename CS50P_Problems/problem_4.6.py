import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit(("Command-line argument is not a number"))

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="
key = "158f57b4c37122dbc9efc6d88c9b5bb388ff7457e9b5d83112fd31c9ee8d0001"
try:
    response = requests.get(url+key)
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Network error occurred")

print(f"{n*price:,.4f}")


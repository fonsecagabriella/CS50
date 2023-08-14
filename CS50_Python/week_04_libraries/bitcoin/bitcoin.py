import sys
import requests


def main():
    # gets the amount of bitcoins the user wants to buy
    x = buy_bitcoins()
    # gets the price of the bitcoin now in USD
    y = price_bitcoin()
    # calculates the amount in USD and prints
    amount = x * y
    print(f"${amount:,.4f}")

def buy_bitcoins():
    while True:
        try:
            # if there is no value passed by user
            if len(sys.argv) == 1:
                print ("Missing command-line argument")
                sys.exit(1)
            else:
            # gets value passed by user
                return float(sys.argv[1])
        except ValueError:
            # catches values that are not number and exits
            print ("Command-line argument is not a number")
            sys.exit(1)

def price_bitcoin():
    while True:
        try:
        # makes a request for bitcoin price and returns it
            return make_request()
        except requests.RequestException:
        # catches exception in case request doesn't work
            print ("Bad request")

def make_request():
    # requests from api
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # creates a data variable json type
    data = r.json()
    # access value in USD and return it
    return float(data['bpi']['USD']['rate_float'])


if __name__ == "__main__":
    main()
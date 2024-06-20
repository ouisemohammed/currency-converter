import requests

# API key and URL for the currency conversion service
API_KEY = 'gcphbaASK0oQe03WRwNUW3bIAaaHk033'
API_URL = 'https://api.apilayer.com/fixer/convert'

def get_exchange_rate(from_currency, to_currency, amount):
    """
    Fetch the exchange rate and convert the amount from one currency to another.

    Parameters:
    - from_currency: The currency code to convert from (e.g., 'USD').
    - to_currency: The currency code to convert to (e.g., 'EUR').
    - amount: The amount of currency to convert.

    Returns:
    - The converted amount in the target currency.

    Raises:
    - Exception: If there is an error fetching the conversion rate.
    """
    params = {
        'from': from_currency,
        'to': to_currency,
        'amount': amount
    }
    headers = {
        'apikey': API_KEY
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        if 'error' in data:
            raise Exception(f"API Error: {data['error']}")

        return data['result']
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request Error: {str(e)}")


def main():
    """
    Main function to handle user input and perform the currency conversion.
    """
    while True:
        from_currency = input("Enter the currency you want to convert from (e.g., USD): ").strip().upper()
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").strip().upper()

        try:
            amount = float(input("Enter the amount you want to convert: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
        
        except ValueError as e:
            print(e)
            continue
        
        try:
            converted_amount = get_exchange_rate(from_currency, to_currency, amount)
            print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
            break
        
        except Exception as e:
            print(e)
            print("Please try again.")

if __name__ == "__main__":
    main()

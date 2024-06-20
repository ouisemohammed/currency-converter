# starting the program
import requests

initial_currency = input("please insert initial currency : ")
target_currency = input("please insert trget currency : ")

while True:
    try:
        amount = float(input("Enter the amount you want to compare: "))
    except:
        print("the amount need to be in numbers ")
        continue

    if amount == 0:
        print("amount needs to be greater than 0")
        continue
    else:
        break


import requests

url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "gcphbaASK0oQe03WRwNUW3bIAaaHk033"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if status_code != 200:
    print("there was a problem , please try again later")
    quit()

result = response.json()
print(result['result'])
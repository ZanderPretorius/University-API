import requests

requested_flag = "South Africa"


response = requests.get(
    f"https://countryflagapi.herokuapp.com/country/{requested_flag}")

data = response.json()
print(data)

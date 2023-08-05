import requests
import time


base_url = 'http://api.open-notify.org/iss-now.json'
while True:
    response = requests.get(url=base_url)
    data = response.json()
    result = f'{data["iss_position"]["longitude"]}; {data["iss_position"]["latitude"]}\n'

    print(result)

    with open(f'statistic/data.csv', 'a') as file:
        file.write(result)
    time.sleep(5)


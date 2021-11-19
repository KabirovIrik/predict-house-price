import requests
import json

# Адрес обращения
url = 'http://127.0.0.1:5000/api/'

# Примеры входных данных 
data = {
    'level':8,
    'num_levels':16,
    'square_full':35,
    'rooms_vals':1,
    'date_public': '10.10.2021'
}
# Преобразование входных данных
j_data = json.dumps(data)

# Отправка запроса
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)

# Вывод статуса ответа и результат
print(r, r.text)
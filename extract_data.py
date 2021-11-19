import requests
import time
from bs4 import BeautifulSoup
import csv
import urllib

# Страница - список квартир, который будем обходиться используя пагинацию сайта
url_main = 'http://www.citystar.ru/detal.htm?d=462&nm=%CE%E1%FA%FF%E2%EB%E5%ED%E8%FF+%2D+%CD%EE%E2%EE%F1%F2%F0%EE%E9%EA%E8+%E2+%E3%2E+%CC%E0%E3%ED%E8%F2%EE%E3%EE%F0%F1%EA%E5&pN='

# Данные будут сохранены в csv файл
with open('sites_html.csv', 'a', newline='', encoding='utf-8') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=';')
	spamwriter.writerow(['date', 'rooms', 'level', 'num_levels', 'square_full', 'square_live', 'square_other', 'price'])

	# Обход веб-страниц 
	for p in range(1, 12):
		# указываем URL и номер страницы
		url_i = url_main + str(p)
		
		# Получаем содержимое страницы
		r = urllib.request.urlopen(url_i)
		page_conetnt = r.read()
		print('page:', p, '- status:', r.status)

		# Парсинг содержимого страницы
		soup = BeautifulSoup(page_conetnt, 'html.parser', from_encoding='cp1251')
		# Обход ячейки таблицы, содержащей данные
		for j, tr in enumerate(soup.select('.tbb')):
			row = []
			for i, td in enumerate(tr.findChildren('td')):
				if i == 1: # date
					try:
						# td.contents[2].text # time
						row.append(td.contents[0])
					except Exception as e:
						print('Page:', p, 'item:', j)
						print(str(e))
						row.append('')
				elif i == 2: # rooms
					try:
						row.append(td.text)
					except Exception as e:
						print('Page:', p, 'item:', j)
						print(str(e))
						row.append('')
				elif i == 4: # street
					pass
				elif i == 5: # level / number levels
					try:
						levels = td.text.split('/')
						row.append(levels[0])
						row.append(levels[1])
					except Exception as e:
						print('Page:', p, 'item:', j)
						print(str(e))
						row.append('')
						row.append('')
				elif i == 6: # square full
					try:
						row.append(td.text)
					except Exception as e:
						print('Page:', p, 'item:', j)
						print(str(e))
						row.append('')
				elif i == 7: # square live
					try:
						row.append(td.text)
					except Exception as e:
						print('Page:', p, 'item:', j)
						print(str(e))
						row.append('')
				elif i == 8: # square other
					try:
						row.append(td.text)
					except Exception as e:
						print('Page:', p, 'item:', j)
						print(str(e))
						row.append('')
				elif i == 10: # price
					try:
						row.append(td.text)
					except Exception as e:
						print('Page:', p, 'item:', j)
						print(str(e))
						row.append('')

			spamwriter.writerow(row)

		time.sleep(2)

print('done!')
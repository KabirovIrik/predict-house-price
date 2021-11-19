import pandas as pd
import numpy as np
import joblib, pickle
from datetime import date
from catboost import CatBoostRegressor

CATEGORICAL = ['rooms_vals' , 'month_public']
NUMERICAL = ['level', 'num_levels', 'square_full', 'days_public']

REQUIRED_ARGS = [
'level',
'num_levels',
'square_full',
'rooms_vals',
'date_public'
]
# Загружаем преобразователь масштаба числовых данных
scaler = joblib.load('num-scaler.joblib')

# Получаем признаки из даты
def getDateFeatures(val):
    # Дней с момента публикации
    today = pd.to_datetime(date.today().strftime("%d.%m.%Y"), format='%d.%m.%Y')
    days_public = today - val
    # Месяц публикации
    month_public = val.month
    return days_public.days, month_public

# Получаем оценку
def getResponse(df):
	# Создаем модель
	model_cb = CatBoostRegressor()
	# Загружаем обученную модель
	model_cb.load_model('CBregressor', format='cbm')
	return str(model_cb.predict(df))

# Получение DataFrame
def getDataFrame(argums):
	# Аргументы запроса
	level = int(argums['level'])
	num_levels = int(argums['num_levels'])
	square_full = float(argums['square_full'])
	rooms_vals = str(argums['rooms_vals'])
	date_public = str(argums['date_public'])

	# Создаем DataFrmae
	df = pd.DataFrame({
		'level':[level],
		'num_levels':[num_levels],
		'square_full':[square_full],
		'rooms_vals':[rooms_vals],
		'date_public':[date_public]
	})

	# Получаем данные даты-времени
	df['date_public'] = pd.to_datetime(df['date_public'], format='%d.%m.%Y')
	df['days_public'], df['month_public'] = zip(*df['date_public'].apply(getDateFeatures))

	# Преобразуем тип данных категорий 
	df['month_public'] = df['month_public'].astype('category')
	df['rooms_vals'] = df['rooms_vals'].astype('category')
	# Масштабируем числовые признаки
	df[NUMERICAL] = scaler.transform(df[NUMERICAL])

	return df[NUMERICAL+CATEGORICAL]
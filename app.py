from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json

from convertInput import *


app = Flask(__name__)


@app.route('/api/', methods=['POST', 'GET'])
def makecalc():
    """
    Список параметров:
    level
    num_levels
    square_full
    rooms_vals
    date_public
    """
    data = request.get_json()

    # Проверка на наличие всех аргументов
    for req_arg in REQUIRED_ARGS:
        if req_arg not in data:
            return 'Заполнены не все параметры'

    # Получаем DataFrame
    df = getDataFrame(data)

    return getResponse(df)

if __name__ == '__main__':
    app.run(debug=True)

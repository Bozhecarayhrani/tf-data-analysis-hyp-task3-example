import pandas as pd
import numpy as np


chat_id = 740849508 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return stats.ttest_ind(x, y, equal_var=False)[1] < 0.03 # Ваш ответ, True или False

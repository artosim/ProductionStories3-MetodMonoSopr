import numpy as np
import pandas as pd
from scipy.stats import rankdata

# Читаем данные
data = pd.read_table('in.txt', sep=' ', header=None, names=['x', 'y'])
N = len(data)

# Проверяем условие на количество данных
if N < 9:
    raise ValueError('Not enough data')

# Сортируем по одной переменной
data = data.sort_values('x')

# Определяем ранги по другой переменной
ranks = rankdata(data['y'].values, method='average')
data['r'] = ranks
data['r'] -= data['r'].max() + 1
data['r'] *= -1

# p - ближайшее к N/3 целое число
p = round(N / 3)

# Суммы первых и последних p рангов
R1 = data['r'][:p].sum()
R2 = data['r'][-p:].sum()

# Разность R1 - R2 как нормально распределенное отклонение
# со стандартной ошибкой
dif = R1 - R2
st_err = (N + 1 / 2) * np.sqrt(p / 6)

# Мера сопряженности
mera = dif / (p * (N - p))

# Записываем в файл ответ
with open('out.txt', 'w') as f:
    f.write(f'{int(np.round(dif))} {int(np.round(st_err))} {np.round(mera, 2)}\n')

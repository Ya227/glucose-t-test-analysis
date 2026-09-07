import pandas as pd
import numpy as np
import statistics
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('data/diabetes.csv')

glucose = df.iloc[:300, 1].tolist()
diabet = df.iloc[:300, 8].tolist()
data = []
for i in range(len(glucose)):
    if(diabet[i]==1):
        data.append(glucose[i])

data.sort()
n = len(data)
print('Объем выборки: ', n)
max_g = data[-1]
print("Максимум: ", max_g)
min_g = data[0]
print("Минимум: ", min_g)
sr = statistics.mean(data)
print("Среднее арифметическое: ", sr)
dis = statistics.variance(data)
print("дисперсия: ", dis)
med = statistics.median(data)
print("медиана: ", med)
st = statistics.stdev(data)
print("стандартное отклонение: ", st)
moda = statistics.mode(data)
print("мода: ", moda)
weighted_average = 0
uni, weight = np.unique(data, return_counts=True)
for i in range(len(uni)):
    weighted_average += (uni[i]*weight[i])
weighted_average /= sum(weight)
print('Среднее взвешенное: ', weighted_average)
print('Объем уникальных значений: ', len(uni))

# H0 - средний уровени глюкозы у диабетиков в среднем равно 130
# H1 - меньше или больше 130
# alpha = 0.05

alpha = 0.05
beta = 1-alpha
df = n - 1
T = ((sr-130)/st)*(np.sqrt(df))
print('Статистика одновыборочного критерия Стьюдента:', T)

critical_value = stats.t.ppf(1 - alpha / 2, df)
p_value = 2 * stats.t.sf(abs(T), df)
print(f"Критическое значение (C): {critical_value}")
print(f"p-значение: {p_value}")

# т.к. |Т| > C-крит, то H0 отвергается
# т.к. p-value < alpha, то H0 отвергается

x=np.linspace(-4,4,500)
y=stats.t.pdf(x, df)

plt.figure(figsize=(10,5))
plt.plot(x, y, 'b-', label=f'T (df={df})')

plt.fill_between(x, y, where=(x <= -critical_value), color='red', alpha=0.3, label='Критическая область')
plt.fill_between(x, y, where=(x >= critical_value), color='red', alpha=0.3)
plt.axvline(T, color='g', linestyle='--', label=f'Выборочная статистика (T={T:.2f})')

plt.title('Двусторонний T критерий Стьюдента')
plt.xlabel('Значение t-статистики')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()

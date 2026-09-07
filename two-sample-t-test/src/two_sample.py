import pandas as pd
import statistics
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/diabetes.csv')
glucose = df.iloc[:300, 1].tolist()
diabet = df.iloc[:300, 8].tolist()
group1 = []
group2 = []
for i in range(len(glucose)):
    if(diabet[i]==1):
        group1.append(glucose[i])
    else:
        group2.append(glucose[i])

group1.sort()
group2.sort()

n1 = len(group1)
n2 = len(group2)
print(f'Объем выборок: n1={n1}, n2={n2}')
max_g1 = group1[-1]
max_g2 = group2[-1]
print(f"Максимумы: max1={max_g1}, max2={max_g2}")
min_g1 = group1[0]
min_g2 = group2[0]
print(f"Максимумы: min1={min_g1}, min2={min_g2}")
sr1 = statistics.mean(group1)
sr2 = statistics.mean(group2)
print(f"Среднее арифметическое: mean1={sr1}, mean2={sr2}")
dis1 = statistics.variance(group1)
dis2 = statistics.variance(group2)
print(f"Дисперсия: var1={dis1}, var2={dis2}")
med1 = statistics.median(group1)
med2 = statistics.median(group2)
print(f"медиана: med1={med1}, med2={med2}")
st1 = statistics.stdev(group1)
st2 = statistics.stdev(group2)
print(f"стандартное отклонение: st1={st1}, st2={st2}")
moda1 = statistics.mode(group1)
moda2 = statistics.mode(group2)
print(f"мода: moda1={moda1}, moda2={moda2}")

# сравнение уровня глюкозы у диабетика и не диабетика
# H0 - Средний уровень глюкозы у диабетиков и не диабетиков одинаков
# H1 - Средний уровень глюкозы у диабетиков и не диабетиков различается
# alpha = 0.05

alpha = 0.05
beta = 1 - alpha
df = n1 + n2 - 2

t_stat, p_value = stats.ttest_ind(group1, group2)
print("t-статистика:", t_stat)
print("p-значение:", p_value)

c_left = stats.t.ppf(alpha/2, df)
c_right = stats.t.ppf(1 - alpha/2, df)
print("c-left", c_left)
print("c-right", c_right)

plt.figure(figsize=(12, 6))
x = np.linspace(-5, 5, 500)
y = stats.t.pdf(x, df)
plt.plot(x, y, 'k-', label='t-распределение')
plt.axvline(t_stat, color='red', linestyle='--', label=f't-статистика = {t_stat}')
plt.fill_between(x, y, where=(x < c_left) | (x > c_right), color='red', alpha=0.3, label='Критическая область')
plt.axvline(c_left, color='green', linestyle=':')
plt.axvline(c_right, color='green', linestyle=':')
plt.title(f'Двухвыборочный t-тест (p = {p_value})')
plt.xlabel('t-значение')
plt.ylabel('Плотность вероятности')
plt.legend()

plt.tight_layout()
plt.show()

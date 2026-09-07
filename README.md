# Анализ уровня глюкозы с использованием критериев Стьюдента
Проект посвящён статистическому анализу уровня глюкозы у диабетиков и не диабетиков с применением одновыборочного и двухвыборочного t‑критерия Стьюдента.

Работа демонстрирует навыки проверки гипотез, расчёта статистических метрик, визуализации критических областей и интерпретации результатов.

## Одновыборочный t‑критерий Стьюдента
### Цель
Проверить гипотезу о том, что средний уровень глюкозы у диабетиков равен 130.

### Основные результаты
* Объём выборки: 114
* Среднее: 138.66
* Стандартное отклонение: 29.54
* t‑статистика: 3.12
* Критическое значение: 1.98
* p‑значение: 0.0023

### Вывод
Гипотеза H0 отвергается — средний уровень глюкозы у диабетиков статистически отличается от 130.

### Материалы
- Notebook: 
  [one_sample_t_test.ipynb](https://github.com/Ya227/glucose-t-test-analysis/blob/main/one-sample-t-test/notebooks/one_sample.ipynb)

- Отчёт: 
  [one_sample_report.md](https://github.com/Ya227/glucose-t-test-analysis/blob/main/one-sample-t-test/reports/one_sample_report.md)

- Код:  
  [one_sample_t_test.py](https://github.com/Ya227/glucose-t-test-analysis/blob/main/one-sample-t-test/src/one_sample.py)


## Двухвыборочный t‑критерий Стьюдента
### Цель
Сравнить уровень глюкозы у диабетиков и не диабетиков.

### Основные результаты
* Объёмы выборок: n₁ = 114, n₂ = 186
* Средние: 138.66 vs 110.33
* t‑статистика: 8.20
* p‑значение: 7.16 × 10⁻¹⁵
* Критические значения: ±1.97

### Вывод
Гипотеза H0 отвергается — уровни глюкозы существенно различаются.

### Материалы
- Notebook: 
  [two_sample.ipynb](https://github.com/Ya227/glucose-t-test-analysis/blob/main/two-sample-t-test/notebooks/two_sample.ipynb)

- Отчёт: 
  [two_sample_report.md](https://github.com/Ya227/glucose-t-test-analysis/blob/main/two-sample-t-test/reports/two_sample_report.md)

- Код:  
  [two_sample.py](https://github.com/Ya227/glucose-t-test-analysis/blob/main/two-sample-t-test/src/two_sample.py)

## Визуализация
Оба анализа включают:
* графики t‑распределения;
* выделение критических областей;
* отображение выборочной статистики;
* сохранение изображений в папку images/.

## Используемые технологии
* Python
* Pandas
* NumPy
* Matplotlib
* SciPy
* statistics

## Запуск в Google Colab

[Открыть одновыборочный тест в Colab](https://colab.research.google.com/github/Ya227/glucose-t-test-analysis/blob/main/one-sample-t-test/notebooks/one_sample.ipynb)

[Открыть двухвыборочный тест в Colab](https://colab.research.google.com/github/Ya227/glucose-t-test-analysis/blob/main/two-sample-t-test/notebooks/two_sample.ipynb)

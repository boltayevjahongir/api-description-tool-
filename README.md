
# Товарный описатель с OpenAI API

## Описание
Этот скрипт автоматизирует процесс генерации уникальных описаний товаров на основе данных из Excel-файла.  
Скрипт использует **OpenAI GPT API** для генерации описаний, которые добавляются в новый столбец исходного Excel-файла.

## Функциональность:
1. Читает Excel-файл с товарами.
2. Генерирует уникальное описание для каждого товара на основе его характеристик.
3. Добавляет сгенерированные описания в новый столбец "Сгенерированное описание".
4. Сохраняет обновленный файл в новом Excel-документе.

## Требования:
- Python 3.8 и выше.
- OpenAI API ключ.

## Установка зависимостей:
Установите необходимые библиотеки командой:
```bash
pip install -r requirements.txt
```

## Использование:
1. Добавьте свой OpenAI API ключ в файл `script.py` в переменную `openai.api_key`.
2. Переименуйте ваш Excel-файл в `input.xlsx` (или укажите путь в коде).
3. Запустите скрипт командой:
```bash
python script.py
```
4. Результат сохранится в файле `output.xlsx`.

## Структура Excel-файла:
Исходный файл должен содержать следующие столбцы:
- `Описание` (название товара)
- `Бренд`
- `Категория 2`
- `Артикул`

## Пример результата:
| Описание                 | Бренд    | Категория 2         | Артикул       | Сгенерированное описание            |
|--------------------------|----------|---------------------|--------------|------------------------------------|
| 04022-04008 ШТИФТ        | KOMATSU  | Гидравлические клапана | 04022-04008 | Уникальное описание для штифта... |

## Контакты:
Если возникнут вопросы или потребуется доработка, свяжитесь со мной.

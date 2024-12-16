
import pandas as pd
import openai

# Установите ваш OpenAI API ключ здесь
openai.api_key = "ВАШ_API_КЛЮЧ"

# Функция для генерации описаний через OpenAI GPT
def generate_description(item_name, brand, category, additional_info):
    prompt = (f"Сгенерируй уникальное, интересное и краткое описание для товара: {item_name}. "
              f"Бренд: {brand}, Категория: {category}. Дополнительная информация: {additional_info}.")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Можно использовать gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100  # Настройте длину текста
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Ошибка при генерации описания: {e}")
        return "Описание недоступно"

# Основная функция
def process_excel(input_file, output_file):
    # Загрузка данных из Excel
    df = pd.read_excel(input_file)

    # Создание нового столбца с описаниями
    descriptions = []
    for index, row in df.iterrows():
        print(f"Генерация описания для товара: {row['Описание']}...")
        desc = generate_description(
            item_name=row['Описание'],
            brand=row['Бренд'],
            category=row['Категория 2'],
            additional_info=f"Артикул: {row['Артикул']}"
        )
        descriptions.append(desc)

    df['Сгенерированное описание'] = descriptions

    # Сохранение файла с новыми описаниями
    df.to_excel(output_file, index=False)
    print(f"Файл сохранен как: {output_file}")

# Запуск скрипта
if __name__ == "__main__":
    input_excel = "input.xlsx"   # Замените на путь к вашему входному файлу
    output_excel = "output.xlsx" # Путь для сохранения файла с описаниями
    process_excel(input_excel, output_excel)

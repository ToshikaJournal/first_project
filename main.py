import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из файла .env
    load_dotenv()
    # Читаем значение переменной AUTHOR
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

# Вызываем функцию для проверки
print_author()

def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл для записи с кодировкой UTF-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings):
            # Получаем номер байта начала строки перед записью
            start_byte_position = file.tell()
            # Записываем строку в файл с символом новой строки
            file.write(string + '\n')
            # Добавляем запись в словарь
            strings_positions[(i + 1, start_byte_position)] = string

    # Возвращаем словарь с позициями строк и самими строками
    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата на консоль
for elem in result.items():
    print(elem)
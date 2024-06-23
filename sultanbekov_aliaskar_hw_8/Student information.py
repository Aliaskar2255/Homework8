import sqlite3

# Функция для получения информации об учениках по id города
def get_students_info_by_city_id(city_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

#Запрос для получения информации об учениках и их городах проживания
    query = '''
    SELECT students.first_name, students.last_name, countries.title AS country, cities.title AS city, cities.area
    FROM students
    INNER JOIN cities ON students.city_id = cities.id
    INNER JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    '''
    cursor.execute(query, (city_id,))
    students_info = cursor.fetchall()

    conn.close()
    return students_info

# Основная функция программы
def main():
#Создаем соединение с базой данных
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    print("Вы можете отобразить список учеников "
          "по выбранному id города из списка городов ниже, для выхода из программы введите 0:")

    # Выводим список городов
    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]}: {city[1]}")

    while True:
        city_id = input("\nВведите id города (или 0 для выхода): ")
        if city_id == '0':
            break

        try:
            city_id = int(city_id)
            if city_id not in [city[0] for city in cities]:
                print("Некорректный id города. Попробуйте снова.")
                continue

            # Получаем информацию об учениках по id города
            students_info = get_students_info_by_city_id(city_id)

            if students_info:
                print(f"\nУченики из города {city_id}:")
                for student in students_info:
                    # Форматированный вывод информации об ученике
                    print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
            else:
                print(f"В городе с id {city_id} нет учеников.")
        except ValueError:
            print("Пожалуйста, введите корректный числовой id города.")

    # Закрываем соединение
    conn.close()

if __name__ == "__main__":
    main()

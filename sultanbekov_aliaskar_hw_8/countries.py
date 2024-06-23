import sqlite3

#Создаем соединение с базой данных (создает файл базы данных, если его не существует)
conn = sqlite3.connect('example.db')

#Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

#Создаем таблицу countries
cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
''')

#Добавляем 3 записи в таблицу countries
countries = [
    ('Kyrgyzstan',),
    ('Kazakhstan',),
    ('China',)
]
cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)

#Получаем id добавленных стран
cursor.execute('SELECT id, title FROM countries')
country_ids = {title: id for id, title in cursor.fetchall()}

#Создаем таблицу cities
cursor.execute('''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)
''')

#Добавляем 7 городов в таблицу cities
cities = [
    ('Bishkek', 127, country_ids['Kyrgyzstan']),
    ('Batken', 205, country_ids['Kyrgyzstan']),
    ('Osh', 182, country_ids['Kyrgyzstan']),
    ('Aktobe', 400, country_ids['Kazakhstan']),
    ('Almaty', 682, country_ids['Kazakhstan']),
    ('Beijing', 16411, country_ids['China']),
    ('Shanghai', 6340, country_ids['China'])
]
cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)

# Получаем id добавленных городов
cursor.execute('SELECT id, title FROM cities')
city_ids = {title: id for id, title in cursor.fetchall()}

#Создаем таблицу students
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)
''')

#Добавляем 15 учеников проживающих в разных городах
students = [
    ('Aliaskar', 'Sultanbekov', city_ids['Bishkek']),
    ('Nurbolot', 'Sultanbekov', city_ids['Bishkek']),
    ('Alina', 'Kuripova', city_ids['Osh']),
    ('Son', 'Min', city_ids['Beijing']),
    ('Nurzat', 'Believa', city_ids['Almaty']),
    ('Li', 'Xian', city_ids['Shanghai']),
    ('Alinur', 'Shamansurov', city_ids['Aktobe']),
    ('Vladimir', 'Karipov', city_ids['Batken']),
    ('Chan', 'Lee', city_ids['Beijing']),
    ('Sabina', 'Kai', city_ids['Almaty']),
    ('Sanira', 'Uralieva', city_ids['Osh']),
    ('Bekzat', 'Ulanov', city_ids['Osh']),
    ('Chan', 'Gan', city_ids['Shanghai']),
    ('Alavset', 'Mamiev', city_ids['Aktobe']),
    ('Samat', 'Isovich', city_ids['Bishkek'])
]
cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', students)

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
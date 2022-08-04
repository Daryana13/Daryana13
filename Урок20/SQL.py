import sqlite3
#Создаём базу данных
conn = sqlite3.connect('name4.db')

#Создаём объект cursor, который позволяет нам взаимод.с базами данных и добавлять записи
cursor = conn.cursor()

#Создаём таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCRENENT, col_1 TEXT, col_2 TEXT)''')

#Заполняем таблиу данными

cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello', 'world')''')

#Сохраняем изменения
conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# print(cursor.fetchall())

d = 'red'
f = 'black'
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''', (d, f))
conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
print(cursor.fetchall())

#Удаление записи из таблицы

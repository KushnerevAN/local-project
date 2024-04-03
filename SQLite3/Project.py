import sqlite3

db = sqlite3.connect('itproger.db') # Создание самой базы данных с указанием названия файла

c = db.cursor() # Создание курсора
#c.execute("""CREATE TABLE articles (
#    title str,
#    full_text str,
#    views int,
#    avtor str
    
#)""")

# Добавление данных
#c.execute("INSERT INTO articles VALUES ('Amazone is cool', 'Amazone is realy cool', 250, 'Tom')")

#Удаление данных
#c.execute("DELETE FROM articles WHERE avtor = 'Admin'")

#Изменение данных
c.execute("UPDATE articles SET avtor = 'Admin' WHERE title = 'Amazone is cool'")

# Просмотр 
c.execute("SELECT rowid, * FROM articles WHERE rowid < 5 ORDER BY views") # Выборка полей (* означает вывод всей информации, можем обратиться к любому полю, например к title)
items = (c.fetchall()) # Вывод все записей
#print(c.fetchmany(1)) # Вывод заданного количества записей
#print(c.fetchone()) # Вывод первой записи из таблицы

for elem in items:
    print(elem[1] + '\n' + elem[4])



db.commit()
db.close()
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1, 'bear')
# zoo.remove('elephant')
# print('Зоопарк:', zoo)
# print('Лев сидит в клетке', zoo.index('lion') + 1)
# print('Обезьяна сидит в клетке', zoo.index('monkey') + 1)

# staff_list = []
# number_staff = int(input('Количество сотрудников: '))
# for i in range(number_staff):
#  print('Зарплата', i + 1, 'сотрудника:', end='')
#  wages = int(input(''))
#  staff_list.append(wages)
# for i in staff_list:
#  if i <= 0:
#    staff_list.remove(i)
#    number_staff -= 1
# print('Осталось сотрудников:', number_staff)
# print('Зарплаты:', staff_list)

# max_number = max(staff_list)
# min_number = min(staff_list)
# print('Максимальная з/п:', max_number)
# print('Минимальная з/п:', min_number)

def i(new_movie, film_list):
    for i_movie in film_list:
        if i_movie == movie:
            return True
    return False


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня', 'Проклятый остров', 'Начало', 'Матрица']
my_films = []
while True:
    print('Ваш текущий топ фильмов', my_films)
    print('Название фильма:', end=' ')
    movie = input()
    if i(movie, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду:')
        if command == 'добавить':
            if i(movie, my_films):
                my_films.append(movie)
            else:
                print('Такой фильм уже есть в вашем рейтинге.')
        if command == 'вставить':
            index = int(input('Укажите место в списке: '))
            my_films.insert(index - 1, movie)
        if command == 'удалить':
            my_films.remove(movie)
        else:
            print('Такого фильма нет в Вашем рейтинге.')

    else:
        print('Такого фильма нет на сайте.')

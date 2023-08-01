def i(new_movie, film_list):
    for i_movie in film_list:
        if i_movie == new_movie:
            return True
    return False

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня', 'Проклятый остров', 'Начало', 'Матрица']
my_films = []
while True:
    print('Ваш текущий топ фильмов', my_films)
    movie = input('Название фильма:')

    if i(movie, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду:')
        if command == 'добавить':
            if i(movie, my_films):
                print('Такой фильм уже есть в вашем рейтинге!')

            else:
                my_films.append(movie)
        if command == 'вставить':
            index = int(input('Укажите место в списке: '))
            my_films.insert(index - 1, movie)
        if command == 'удалить':
            if i(movie, my_films):
                my_films.remove(movie)
            else:
                print('Такого фильма нет в Вашем рейтинге.')

    else:
        print('Такого фильма нет на сайте.')























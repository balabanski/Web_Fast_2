#https://habr.com/ru/post/513328/

1.Схема базы данных и миграции
#опишем схему базы данных. Создадим файл models/users.py И  models/posts.py

#Чтобы автоматизировать миграции базы данных, установим alembic

#Эта команда создаст в текущей директории файл alembic.ini и каталог migrations содержащий:
каталог versions, в котором будут хранится файлы миграций
скрипт env.py, запускающийся при вызове alembic
файл script.py.mako, содержащий шаблон для новых миграций.

#Укажем url нашей базы данных в файле alembic.ini

#пишем скрипт env.py, запускающийся при вызове alembic

2.Запускаем приложение и подключаем БД
-Создадим файл main.py
-Чтобы подключиться к базе данных пишем models/database.py (to main.py)

3.Валидация запроса и ответа
-Создадим файл schemas/users.py
-Добавим файл utils/users.py, в котором создадим методы, необходимые для записи пользователя в БД
-Создадим файл routers/users.py
-подключить роуты из файла routers/users.py в main.py

4.Аутентификация и контроль доступа





#Добавим файл utils/users.py, в котором создадим методы, необходимые
#для записи пользователя в БД

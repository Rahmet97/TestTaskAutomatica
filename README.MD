## Руководство по запуску проекта

версия Python 3.9

1. Скачать проект \
     `git clone https://github.com/Rahmet97/TestTaskAutomatica` \
     `cd TestTaskAutomatica/`

2. Создание и активация виртуальной среды \
   `pip3 install virtualenv` \
   `virtualenv venv` \
   `venv\Scripts\activate` (для Windows) \
   `source venv/bin/activate` (для Linux) 
3. Установить необходимые пакеты \
   `pip install -r requirements.txt`
4. Нужно создать базу данных в MySQL с помощью phpmyadmin или терминала.
5. Миграция \
   `python manage.py migrate`
6. Запуск \
   `python manage.py runserver`
   
## Документация для API
1. Получить список Торговых точек привязанных к переданному номеру телефона \
   GET http://127.0.0.1:8000/api/get-shopping-centers-list?phone=998999682505
2. Выполнить посещение в Торговую точку \
   POST http://127.0.0.1:8000/api/visit с параметрами: \
   phone:998999682505 \
   shopping_center_id:2 \
   latitude:40.02123 \
   longitude:22.35478
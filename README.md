Для установки модулей

'pip install -r requirements.txt'

Для создания таблиц и посева

'py seed.py'

Для запуска сервера

'py -m uvicorn main:app --reload'




За что отвечают файлы
1. database.py - подключение к БД
2. models.py - таблицы БД с описанием связей
3. seed.py - посев (стартовые данные)
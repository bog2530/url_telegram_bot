# Telegram-bot  добавления в базу данных новых данных для парсинга

### Технологии
- python-telegram-bot 13.15  
- python-dotenv 0.20  
- pandas 1.5.2


## Описание
- Пользователь прикрепляет файл excel(x) в формате (название, URL, xpath запрос)
  - Бот получает файл, сохраняет
    - Открывает файл библиотекой pandas
      - Выводит содержимое в ответ пользователю
       - Сохраняет содержимое в локальную бд sqlite

## Как запустить

#### Создать виртуальное окружени
```
python3 -m venv env
```
#### Активировать виртуальное окружение 
```
. env/bin/activate
```
#### Установить Зависимости
```
pip install -r requerments.txt
```
#### Создание базы данных
```
python app.py
```
#### Создать файл .env
- В файле создать TELEGRAM_TOKEN=токен Вашего бота
#### Запуск бота 
```
python telegram_bot.py
```

### Пример ответа в Telegrm 
```
[
   {
      "Name": "Test",
      "URL": "http://test.com/",
      "Xpath": "test"
   }
]
```
## Автор
[Шумский Богдан](https://github.com/bog2530)
Telegram: [@bog2530](https://t.me/bog2530)
Email: bog2530@gmail.com
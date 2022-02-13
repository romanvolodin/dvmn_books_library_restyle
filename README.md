# Парсим онлайн библиотеку

Скрипт `parse.py` скачивает научно-фантастические книги с сайта [tululu.org](http://tululu.org/l55/). Для каждой книги дополнительно скачиваются обложка и комментарии.  
Скрипт `render.py` генерирует сайт для просмотра книг без Интернета.  
Пример сайта можно посмотреть здесь - https://romanvolodin.github.io/scifi-books-demo/

## Требования

Для запуска вам понадобится Python 3.6 или выше.

## Подготовка

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

### Скачайте книги:
```sh
python parse.py --start_page 1 --end_page 10
```
Можно использовать сокращенную запись:
```sh
python parse.py -s 1 -e 10
```
Можно не указывать параметры `--start_page` и `--end_page`, по умолчанию будут скачиваться все доступные страницы, что займет _очень_ много времени.  
В случае успешного выполнения скрипт ничего не выводит.

Доступные параметры:
- `--start_page` - Начиная с какой страницы скачивать книги. По умолчанию: `1`
- `--end_page` - По какую страницу скачивать книги (не включительно). По умолчанию: `702`
- `--dest_folder` - Путь в каталогу с результатами парсинга. По умолчанию: `scifi_books`
- `--skip_imgs` - Пропустить скачивание картинок.
- `--skip_txt` - Пропустить скачивание книг.
- `--json_path` - Путь к JSON-файлу с результатами. По умолчанию: `scifi_books/books.json`

### Сгенерируйте сайт для локального просмотра:
```sh
python render.py
```
В случае успешного выполнения скрипт ничего не выводит.

Доступные параметры:
- `--dest_folder` - Путь в каталогу с результатами парсинга. По умолчанию: `scifi_books`
- `--json_path` - Путь к JSON-файлу с результатами парсинга. По умолчанию: `scifi_books/books.json`
- `--livereload` - Запустить автоматическую генерацию страниц при обновлении. Удобно при разработке.

## Цели проекта

Код написан в учебных целях — для курса по Python на сайте [Devman](https://dvmn.org).
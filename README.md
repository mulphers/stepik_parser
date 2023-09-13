# Парсер для получения информации о курсах по языку Python на платформе stepik.org

## Установка:
````
pip install -r requirements.txt
````

## Технологии, которые использовались в данном парсере:
- Asyncio
- BeautifulSoup
- Selenium

## Файл с результатами находиться в results/results.json и имеет следующий вид:

````
[
    {
        "title": "Title",
        "description": "Description",
        "grade": 5.0,
        "appraisers": 83,
        "price": 0,
        "link": "https://stepik.org/course/..."
    },
    
    ...
]
````


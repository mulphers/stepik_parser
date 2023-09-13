import os

from bs4 import BeautifulSoup

from settings import domain


def appraisers_correction(appraisers):
    return int(appraisers.replace('.', '').replace('K', '00'))


def get_parser_data():
    data = []

    for page in sorted(os.listdir('data'), key=lambda filename: int(filename.split('.')[0])):
        with open(file=f'data/{page}', mode='r', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(
            markup=src,
            features='lxml'
        )

        all_course_cards = soup.find_all('li', class_='course-cards__item')

        for card in all_course_cards:
            title = card.find('a', class_='course-card__title').text.strip()
            description = card.find('div', class_='shortened-text').text.strip()

            try:
                grade = float(card.find('span', class_='course-card__widget').text.split()[-2])
                appraisers = appraisers_correction(
                    appraisers=card.find('span', class_='course-card__widget').text.split()[-1].strip('()')
                )
            except (IndexError, AttributeError):
                grade = None
                appraisers = None

            try:
                price = int(''.join(card.find('span', class_='display-price').text.split()[1:-1]))
            except ValueError:
                price = 0

            link = f'{domain}{card.find("a", class_="course-card__title").get("href")}'

            data.append(
                {
                    'title': title,
                    'description': description,
                    'grade': grade,
                    'appraisers': appraisers,
                    'price': price,
                    'link': link
                }
            )

    return data

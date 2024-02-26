from itertools import count
from time import sleep
from typing import Any

import requests

from src.common.utils import save_data_in_json
from src.core.config import (course_in_page_url_template,
                             info_about_courses_url_template)


def _parse_courses_id_in_pages() -> list[int]:
    courses_id = []

    for page in count(start=1):
        response_json: dict[str, Any] = requests.get(
            url=course_in_page_url_template.format(page)
        ).json()

        if response_json.get('detail') == 'Not found':
            break

        courses_id.extend(map(lambda obj: obj['course'], response_json['search-results']))

        print(f'Page {page} done...')
        sleep(3)

    return courses_id


def parse_info_abot_curses() -> None:
    result = []

    response_json: dict[str, Any] = requests.get(
        url=info_about_courses_url_template.format(
            '&'.join(map(lambda obj: f'ids%5B%5D={obj}', _parse_courses_id_in_pages()))
        )
    ).json()

    for course in response_json['courses']:
        result.append(
            {
                'title': course['title'],
                'url': course['canonical_url'],
                'price': float(course['price']) if course['price'] else 0,
                'learners_count': course['learners_count'],
                'with_certificate': course['with_certificate']
            }
        )

    save_data_in_json(
        file_name='result',
        data=result
    )

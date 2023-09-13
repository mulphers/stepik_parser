import json

from services.analysis import get_parser_data


def save_all_information():
    with open(file='results/results.json', mode='w', encoding='utf-8') as file:
        json.dump(
            obj=get_parser_data(),
            fp=file,
            ensure_ascii=False,
            indent=4
        )

import json
from typing import Any


def save_data_in_json(file_name: str, data: list[dict[str, Any]]) -> None:
    with open(file=f'src/storage/{file_name}.json', mode='w', encoding='utf-8') as file:
        json.dump(
            obj=data,
            fp=file,
            ensure_ascii=False,
            indent=4
        )

    print('Data saved!')

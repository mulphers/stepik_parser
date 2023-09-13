from services.parser import start_loop
from services.saver import save_all_information


def main(save_pages, save_information):
    """
    1. Если save_pages имеет значение True -> все страницы будут сохранены в 'data/{page}.html'.
    2. Если save_information имеет значение True -> все данные будут сохранены в 'results/results.json'
    (перед выполнением данного пункта, убедитесь, что пункт 1 был успешно выполнен и файлы страниц присутствуют в
    'data')

    :param save_pages:
    :param save_information:
    :return:
    """

    if save_pages:
        start_loop()

    if save_information:
        save_all_information()


if __name__ == '__main__':
    main(
        save_pages=False,
        save_information=True
    )

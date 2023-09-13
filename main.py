from services.parser import start_loop
from services.saver import save_all_information


def main(save_pages, save_information):
    """
    1. If save_pages is True -> all pages will be saved to 'data/{page}.html'
    2. If save_information is True -> all data will be saved in 'results/results.json' (before executing
    of this paragraph, make sure that paragraph 1 was completed before this and the page files are present in 'data')

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

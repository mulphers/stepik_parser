import asyncio

from selenium import webdriver

from settings import url


async def save_all_pages(page):
    driver = webdriver.Chrome()

    driver.get(
        url=url.format(page)
    )

    await asyncio.sleep(5)

    for chunk in (1335, 2670):
        driver.execute_script(f'window.scrollTo(0, {chunk})')
        await asyncio.sleep(5)

    with open(file=f'data/{page}.html', mode='w', encoding='utf-8') as file:
        print(driver.page_source, file=file)

    print(f'Saving page {page} is complete!')

    await asyncio.sleep(5)


async def main():
    tasks = [asyncio.create_task(save_all_pages(page)) for page in range(1, 11)]
    await asyncio.gather(*tasks)


def start_loop():
    asyncio.run(main())

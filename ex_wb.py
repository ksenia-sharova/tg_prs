import requests
import json


def numerate_page(num_page):        
        headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': f'https://www.wildberries.ru/catalog/elektronika/igry-i-razvlecheniya/aksessuary/garnitury?sort=popular&page={num_page}&xsubject=593',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.1026 Yowser/2.5 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get(f'https://catalog.wb.ru/catalog/electronic2/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&page={num_page}&pricemarginCoeff=1.0&reg=0&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,40,1,48,71&sort=popular&spp=0&subject=518;593;924;1407;2913;3001;6817&xsubject=593', headers=headers)

        if response.status_code == 200:
                with open("index_wb.html", 'w', encoding='utf-8') as file:
                        file.write(str(response.text))

                current_file = json.loads(response.text)
        return current_file

def get_current_data(current_file):
        df = []
        current_data = current_file['data']['products']
        for item in current_data:
                df.append (
                {'Ссылка': f'https://www.wildberries.ru/catalog/{item["id"]}/detail.aspx?targetUrl=BP',
                'Название': item['name'],
                'Бренд': item['brand'],
                'Скидка_%': item['sale'],
                'Начальная цена': item['priceU'],
                'Цена со скидкой': item['salePriceU']}
        )

        return df[:10]


def common_func(num_page):
        numerate_page(num_page)
        current_file = numerate_page(num_page)
        return get_current_data(current_file)


def main(num_page, brend):
        common_func(num_page)
        res = common_func(num_page)


if __name__ == '__main__':
        page = input('Введите номер страницы для поиска:')
        name_brend = input('Введите название бренда:')
        main(page, name_brend)

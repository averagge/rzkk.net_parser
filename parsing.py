import requests
def name_parser(good_page):
    good_name = good_page.find('h1').text
    return good_name
def description_parser(good_page):
    good_description_p = good_page.find('div', class_='prod_img_cont').find_next_siblings('p')
    good_description = ''
    for p in good_description_p:
        if (p.text.strip() != ''):
            good_description += p.text.strip() + '\n'
    return good_description
def image_parser(good_page, good_link):
    good_image_src = good_page.find("div", class_='prod_img_big').find('img').get('src')
    req = requests.get(f'https://rzkk.net{good_image_src}')
    image_name = good_link.split('/')[-1]
    image_name = image_name.replace('.html', '')
    file_path = f'https://web-coast.su/wordpress/wp-content/uploads/2024/01/{image_name}.jpg'
    windows_path = f'images/{image_name}.jpg'
    with open(windows_path, 'wb') as file:
        file.write(req.content)
    good_images = file_path
    image_list = good_page.find('ul', class_='prod_img_mini').find_all('img')
    count = 1
    for img in image_list:
        file_path = f'https://web-coast.su/wordpress/wp-content/uploads/2024/01/{image_name}_{count}.jpg'
        windows_path = f'images/{image_name}_{count}.jpg'
        req = requests.get(f'https://rzkk.net{img.get("src")}')
        with open(windows_path, 'wb') as file:
            file.write(req.content)
        good_images += ', ' + file_path
        count += 1
    return good_images
def filter_parser(good_page, table_row, table):
    try:
        good_filter = good_page.find('p', text='Фильтр')
        good_attrs = good_filter.find_next_siblings('div')
        index = 39
        for attr in good_attrs:
            table_row[index] = attr.text.strip().split(':')[0]
            index += 4
        selects = good_page.find_all('select', class_='s_filter')
        index = 40
        for s in selects:
            options = s.find_all('option')
            good_options = ''
            for o in options:
                if (o.text != 'Не выбрано'):
                    good_options += ', ' + o.text.replace('.', ',')
            table_row[index] = good_options[2:]
            index += 4
        table.append(table_row)
    except Exception:
        table.append(table_row)
    return table
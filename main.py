import openfile
import soupfile
import parsing

openfile.create_dir()
table_head=openfile.get_table_head()
link="https://rzkk.net/catalog/"
soup=soupfile.get_html(link)
categories=soup.find_all('a', class_="cat_list_name")
table=[]
for cat in categories:
    page_num=1
    category_link=f'https://rzkk.net{cat.get('href')}?PAGEN_1={page_num}'
    category_name=cat.text
    category_page=soupfile.get_html(category_link)
    first_link=category_page.find('a', class_="cat_list_name")
#пагенация
    while True:
        category_link = f'https://rzkk.net{cat.get('href')}?PAGEN_1={page_num}'
        category_page = soupfile.get_html(category_link)
        if(page_num!=1 and category_page.find('a', class_="cat_list_name")==first_link):
            break
        page_num+=1
        goods=category_page.find_all('a', class_="cat_list_name")
        for g in goods:
            good_link='https://rzkk.net'+g.get('href')
            good_page=soupfile.get_html(good_link)
#занесение в строку
            table_row = 82 * ['']
            table_row[3] = parsing.name_parser(good_page)
            table_row[7] = parsing.description_parser(good_page)
            table_row[26] = category_name
            table_row[29] = parsing.image_parser(good_page, good_link)
            parsing.filter_parser(good_page, table_row, table)
soupfile.close_driver()
#запись в csv файл
openfile.write_table_head(table_head)
openfile.write_table(table)
import requests
from lxml import html
import csv

# 常量
BOOK_BASE_URL = "https://books.toscrape.com/"
BOOK_TOP_URL = "https://books.toscrape.com/catalogue/page-{}.html"
BOOK_LIST_FILE = "../csv_data/book_list.csv"

# 获取书本详细信息
def get_book_info(book_info_url):
    book_response = requests.get(book_info_url)
    book_doc = html.fromstring(book_response.text)
    book_name = book_doc.xpath("//*[@id='content_inner']/article/div[1]/div[2]/h1/text()")
    book_price = book_doc.xpath("//*[@id='content_inner']/article/div[1]/div[2]/p[1]/text()")
    book_stock_status = book_doc.xpath("string(//*[@id='content_inner']/article/div[1]/div[2]/p[@class='instock availability'])")
    book_info = {
        "book_name": book_name[0].strip() if book_name else '',
        "book_price": book_price[0].strip() if book_price else '',
        "book_stock_status": book_stock_status.strip() if book_stock_status else ''
    }
    return book_info

# 保存所有书籍信息
def save_all_books(all_books):
    with open(BOOK_LIST_FILE, "w", encoding="utf-8",newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["book_name", "book_price", "book_stock_status"])
        writer.writeheader()
        writer.writerows(all_books)

# 主函数
def main():
    all_books =[]
    for num in range(1,2):
        page_url = BOOK_TOP_URL.format(num)
        # 1.爬取网站数据
        response = requests.get(page_url)
        print(f"发送请求，访问第{num}页数据，获取 BOOK 榜单数据 ...")

        # 2.解析数据，获取书籍列表
        book = html.fromstring(response.text)
        book_list = book.xpath("//*[@id='default']/div/div/div/div/section/div[2]/ol/li")

        # 3.书籍详情
        for li in book_list:
            book_urls = li.xpath("./article/div/a/@href")
            href = book_urls[0]
            if book_urls:
                if href.startswith("catalogue/"):
                    book_info_url = BOOK_BASE_URL.format(num) + book_urls[0]
                else:
                    book_info_url = BOOK_BASE_URL.format(num) + "catalogue/" + book_urls[0]
                book_info = get_book_info(book_info_url)
                all_books.append(book_info)
                print(book_info)

    # 4.保存数据，保存为 csv 文件
    print("获取到所有书籍详情，保存书籍详情到csv文件 ...")
    save_all_books(all_books)

if __name__ == '__main__':
    main()



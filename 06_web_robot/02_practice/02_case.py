import requests
import csv
from lxml import html

# 常量
MOVIE_LIST_FILE = "../csv_data/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"

# 保存电影数据，保存为 csv
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE,"w",encoding = "utf-8",newline="") as f:
        writer = csv.DictWriter(f,fieldnames = ["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "宣传语", "简介"])
        writer.writeheader()
        writer.writerows(all_movies)

# 获取电影详情
def get_movie_info(movie_info_url):
    # 1.发送请求，获取电影详情数据
    movie_response = requests.get(movie_info_url,timeout=60)
    print(f"发送请求{movie_info_url}，获取电影详情数据 ...")
    # 2.解析数据，获取电影详情
    movie_doc = html.fromstring(movie_response.text)
    # 电影名称
    movie_name = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    movie_year = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_dates = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    movie_cost_times = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_languages = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[@class='tagline']/text()")
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    # 3.返回电影详情 -- 字典
    movie_info = {
        "电影名": movie_name[0].strip() if movie_name else '',
        "年份": movie_year[0].strip() if movie_year else '',
        "上映时间": movie_dates[0].strip() if movie_dates else '',
        "类型": movie_tags[0].strip() if movie_tags else '',
        "时长": movie_cost_times[0].strip() if movie_cost_times else '',
        "评分": movie_scores[0].strip() if movie_scores else '',
        "语言": movie_languages[0].strip() if movie_languages else '',
        "导演": movie_directors[0].strip() if movie_directors else '',
        "宣传语": movie_slogans[0].strip() if movie_slogans else '',
        "简介": movie_descriptions[0].strip() if movie_descriptions else '',
    }
    return movie_info


# 主函数：定义核心逻辑
def main():
    all_movies = []
    for page_num in range(1,6):
        # 1.发送请求，获取高分电影榜单数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1,timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&vote_count.lte=&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated",
                                     timeout=60)
        print(f"发送请求，访问第{page_num}页数据，获取 TMDB 电影榜单数据 ...")

        # 2.解析数据，获取电影列表
        doc = html.fromstring(response.text)
        movie_list = doc.xpath("//*[@class='w-full overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-colors hover:border-gray-300']")

        # 3.遍历电影列表，获取电影详情

        for movie in movie_list:
            movie_urls = movie.xpath("./div/div/a/@href")
            if movie_urls:
                # 电影详情的url地址
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求，获取电影详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)
    # 4.保存数据，保存为 csv 文件
    print("获取到所有的电影详情，保存电影数据到CSV文件 ...")
    save_all_movies(all_movies)


if __name__ == '__main__':
    main()

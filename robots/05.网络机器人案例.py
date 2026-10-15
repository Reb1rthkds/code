import requests
from lxml import html
import csv
import re

# 常量
MOVIE_LIST_FILE = "csv_data/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated" # 高分电影榜单的URL(第一页)
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items" # 高分电影榜单的URL(第二页之后)





# 获取电影详情
def get_movie_years(movie_years):
    movie_year =  movie_years[0].strip() if movie_years else ''
    return movie_year.replace("(","").replace(")","")


def get_movie_dates(movie_dates):
    movie_date = movie_dates[0].strip() if movie_dates else ''
    return re.search(r"\d{4}/\d{2}/\d{2}",movie_date).group()


def get_movie_time(movie_times):
    movie_time = movie_times[0].strip() if movie_times else ''
    h_res = re.search(r"(\d+)h",movie_time)
    m_res = re.search(r"(\d+)m",movie_time)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return h * 60 + m


def get_movie_info(movie_info_url):

    print(f"发送请求{movie_info_url}，获取电影详情数据...")
    # 1、发送请求，获取电影详情数据
    movie_response = requests.get(movie_info_url,timeout=60)

    # 2、解析数据，获取电影详情
    movie_document = html.fromstring(movie_response.text)
    # 电影名称,年份，类型，。。。。
    movie_names = movie_document.xpath("/html/body/div[2]/main/section/div[2]/div/div/section/div[2]/section/div[1]/h2/a/text()")
    # print(movie_names)
    movie_years = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_dates = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    movie_types = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    movie_times = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    movie_scores = movie_document.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_languages = movie_document.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_directors = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movie_actors = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_slogans = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    movie_descriptions = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")
    # movie_date = movie_dates[0].strip() if movie_dates else ''
    # match = re.search(r"\d{4}/\d{2}/\d{2}", movie_date)
    # print(match.group() if match else '')
    # print(movie_dates[0].strip())
    # print(type(movie_dates))
    # 3.组装电影详情数据
    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else '',
        "年份": get_movie_years(movie_years),
        "上映时间": get_movie_dates(movie_dates),# get_movie_dates(movie_dates),
        "类型": ",".join(movie_types) if movie_types else '',
        "时长": get_movie_time(movie_times),
        "评分": movie_scores[0].strip() if movie_scores else '',
        "语言": movie_languages[0].strip() if movie_languages else '',
        "导演": ",".join(movie_directors) if movie_directors else '',
        "作者": ",".join(movie_actors) if movie_actors else '',
        "口号": movie_slogans[0].strip() if movie_slogans else '',
        "描述": movie_descriptions[0].strip() if movie_descriptions else '',
    }
    # print(movie_info)
    return movie_info

# 保存电影数据到CSV文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "作者", "口号", "描述"])
        writer.writeheader() # 写入表头
        writer.writerows(all_movies) # 写入多行数据

# 主函数，定义核心逻辑
def main():
    all_movies = []  # 用于存储所有电影信息的列表
    # 循环获取高分电影榜单数据(从第一页到第五页)
    for page_num in range(1, 6):
        print(f"发送请求，获取第{page_num}页的高分电影榜单数据...")
        # 1.发送请求，获取高分电影榜单数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                    f"air_date.gte=&air_date.lte=&certification=&certification_country=HK&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-03-18&show_me=undefined&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=HK&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400"
                                    ,timeout=60)
        # 2.解析数据，获取电影列表
        document = html.fromstring(response.text)
        if page_num == 1:
            # movie_list = document.xpath("/html/body/div[2]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div")
            movie_list = document.xpath("//*[@id='page_1']/div[1]/div/div")
        else:
            # movie_list = document.xpath(f"/html/body/div[2]/main/section/div/div/div/div[2]/div[2]/div/section/div/div[2*{page_num-1}]/div/div")
            movie_list = document.xpath(f"//*[@id='page_{page_num}']/div[1]/div/div")

        # 3.遍历电影列表，获取电影详情
        for movie in movie_list:
            movie_urls = movie.xpath("./div[1]/div/div[1]/a/@href")
            if movie_urls:
                # 电影详情的url
                movie_info_url = TMDB_BASE_URL + movie_urls[1]
                # print(movie_info_url)
                # 发送请求，获取电影详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    # 4.保存数据，写入CSV文件
    print("获取到所有电影数据，开始保存数据，写入CSV文件...")
    save_all_movies(all_movies)

if __name__ == '__main__':
   main()
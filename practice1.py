from urllib.request import urlopen
from bs4 import BeautifulSoup

week = ["mon", "tue", "web", "thu", "fri"]

whatDay = 1205


# 특정 요일 출력
def one_day_out(url, day):
    html = urlopen(url)
    bs_object = BeautifulSoup(html, "html.parser")

    find_day = bs_object.find('td', class_=day + " tch-has")
    find_num = find_day.find('span')
    # find_menu = find_day.find('li')

    print(find_num.text.strip() + "일\n")

    for findMenu in find_day.find_all('li'):
        print(findMenu.text.strip())


# 1주일 메뉴판 출력
def week_out(url, a):
    html = urlopen(url)
    bs_object = BeautifulSoup(html, "html.parser")

    for i in a:
        find_day = bs_object.find('td', class_=i + " tch-has")
        find_num = find_day.find('span')
        # findMenu = findDay.find('li')
        print("\n" + find_num.text.strip() + "일\n")
        for findMenu in find_day.find_all("li"):
            print(findMenu.text.strip())


# a태그 href인자의 값 부분 출력
def href_out(url, day):
    html = urlopen(url)
    bs_object = BeautifulSoup(html, "html.parser")

    find_day = bs_object.find('td', class_=day + " tch-has")
    find_link = find_day.find('a')
    link_data = find_link['href']

    print(len(link_data))
    print(link_data[32:])


week_out("https://school.use.go.kr/yaksa-h/M01030601/list?ymd=20221231",week)

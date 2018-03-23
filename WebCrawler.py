import requests
from bs4 import BeautifulSoup

def webCrawling(keyword, page_count):
    front_url =  "https://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q="
    back_url = "&p="
    result = []

    title = keyword + "_다음_뉴스"
    f = open(title, 'w')
    for i in range(1, page_count+1):
        f.write(str(i)+ " 페이지 : ")
        url = front_url + keyword + back_url + str(i)
        temp_result = requests.get(url)
        soup = BeautifulSoup(temp_result.text, "html.parser")

        titles = soup.select('a.f_link_b')

        for j in range(len(titles)):
            print(titles[j].text.strip())
            s = str(titles[j].text.strip())
            f.write(s+"\n")
            result.append(titles[j].text.strip())

    return temp_result


def main():
    keyword = input("enter the keyword you're looking for : ")
    page_count = int(input("검색할 페이지 수 입력"))

    result = webCrawling(keyword, page_count)
    print(result)

main()

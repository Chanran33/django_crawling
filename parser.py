from selenium import webdriver
from bs4 import BeautifulSoup
import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingproject.settings")
django.setup()
from crawling.models import NewsData

def parse_News():
    brower = webdriver.Chrome('./chromedriver.exe')

    data = []

    for n in range(5):
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%98%AC%EB%A6%BC%ED%94%BD%20%EC%97%AC%EC%9E%90%EB%B0%B0%EA%B5%AC&sort=0&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={0}'.format(1+(n*10))
        brower.get(url)

        html = brower.page_source
        soup = BeautifulSoup(html, 'html.parser')

        for i in range(10):
            title = soup.select('a.news_tit')[i]['title']
            content = soup.select('.news_dsc')[i].text
            data.append([title,content])
            
    return data

if __name__ == '__main__':
    data = parse_News()
    for i in range(len(data)):
        title = data[i][0]
        content = data[i][1]
        NewsData(title=title, content=content).save()

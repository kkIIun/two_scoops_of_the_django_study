import requests 
from bs4 import BeautifulSoup 
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/app')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")
import django
django.setup()
from ClientCrawling.models import Movie

def crawling():
    html = ''
    
    for i in range(20):
        url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20210305&page=' + str(i)
        response = requests.get(url)
        html += response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#old_content > table > tbody > tr > td.title > div > a')
    point = soup.select('#old_content > table > tbody > tr > td.point')
    data = {}
    for i in range(len(title)):
        data[title[i].get_text()] = point[i].get_text()
    return data

if __name__=='__main__':
    movie_data_dict = crawling()
    for t, l in movie_data_dict.items():
        Movie(title=t, point=l).save()
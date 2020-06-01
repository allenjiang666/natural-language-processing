from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import os

urls = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/',
        'https://codeup.com/data-science-myths/',
        'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
        'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
        'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']
def get_codeup_blogs(urls):
    blogs=[]
    for url in urls:
        headers = {'User-Agent': 'Codeup Data Science'}
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.text
        content = soup.find('div', class_='jupiterx-post-content').text
        blog={'title':title,'content':content}
        blogs.append(blog)
    return pd.DataFrame(blogs)

def acquire_codeup_blogs():
    if os.path.exists('codeup_blogs.csv'):
        df = pd.read_csv('codeup_blogs.csv',  index_col=0)
    else:
        df = get_codeup_blogs(urls)
        df.to_csv('codeup_blogs.csv')
    return df

def acquire_news(topic:str):
    url = 'https://inshorts.com/en/read/'+topic
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = get(url, headers=headers)
    news=[]
    for card in cards:
        title = card.find('span', itemprop='headline').text
        content = card.find('div', itemprop='articleBody').text
        author = card.find('span', class_='author').text
        article={
            'title': title,
            'author': author,
            'content': content,
            'category': topic
            }
        news.append(article)
    return news


def get_inshort_news():
    topics = ['business', 'sports', 'technology', 'entertainment']
    news=[]
    for topic in topics:
        news += acquire_news(topic)
    return pd.DataFrame(news)


def acquire_codeup_blogs():
    if os.path.exists('codeup_blogs.csv'):
        df = pd.read_csv('codeup_blogs.csv',  index_col=0)
    else:
        df = get_codeup_blogs(urls)
        df.to_csv('codeup_blogs.csv')
    return df
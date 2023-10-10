from django.shortcuts import render

from django.shortcuts import render
from .models import Post
import requests
from bs4 import BeautifulSoup

def scrape():
    response = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(response.text, 'html.parser')

    for post in soup.find_all('tr', class_='athing'):
        title = post.find('a', class_='storylink').text
        link = post.find('a', class_='storylink')['href']
        author = post.find_next_sibling('tr').find('a', class_='hnuser').text
        description = ''
        comments = ''

        Post.objects.create(
            title=title,
            author=author,
            description=description,
            comments=comments,
            link=link
        )

from fastapi import FastAPI
from enum import Enum
from Notifier.store_data_to_db import store_data_to_db
from Scraper.get_url import *
from Scraper.get_comment import *
import json

app = FastAPI()

class webpageName(str, Enum):
    tinhte = 'tinhte'
    genk = 'genk'
    vietnamnet = 'vietnamnet'
    haibongio = '24h'
    tuoitre = 'tuoitre'
    vnexpress = 'vnexpress'
    list_of_url = 'list_of_url'

class Playlist_or_list(str, Enum):
    playlist = 'playlist'
    list = 'list_of_url'

def convert_to_json(df):
    res = df.to_json(orient = 'records')
    parsed = json.loads(res)
    return parsed

@app.get("/Website")
def Website(webpage_name: webpageName, url: str):
    if webpage_name == 'tinhte':
        urls = tinhte(url)
        data = get_website_comment(urls)
        store_data_to_db.store_to_db(data)
    elif webpage_name == 'genk':
        urls = genk(url)
        data = get_website_comment(urls)
        store_data_to_db.store_to_db(data)
    elif webpage_name == 'vietnamnet':
        urls = vietnamnet(url)
        data = get_website_comment(urls)
        store_data_to_db.store_to_db(data)
    elif webpage_name == '24h':
        urls = haibongio(url)
        data = get_website_comment(urls)
        store_data_to_db.store_to_db(data)
    elif webpage_name == 'tuoitre':
        urls = tuoitre(url)
        data = get_website_comment(urls)
        store_data_to_db.store_to_db(data)
    elif webpage_name == 'vnexpress':
        urls = vnexpress(url)
        data = get_website_comment(urls)
        store_data_to_db.store_to_db(data)
    elif webpage_name == 'list_of_url':
        url= url.replace(" ","")
        urls = list(url.split(","))
        data = get_website_comment(urls)
        store_data_to_db.store_to_db(data)
    else:
        pass
    return convert_to_json(data)

@app.get("/Youtube")
def Youtube(playlist_or_List_of_url: Playlist_or_list, url: str, max_count: int, lookup_period: str):
    if playlist_or_List_of_url == 'playlist':
        urls = youtube(url)
        data = get_youtube_comment(urls, max_count, lookup_period)
        store_data_to_db.store_to_db(data)
    elif playlist_or_List_of_url == 'list_of_url':
        url = url.replace(" ","")
        urls = list(url.split(","))
        data = get_youtube_comment(urls, max_count, lookup_period)
        store_data_to_db.store_to_db(data)
    else:
        pass
    return convert_to_json(data)

@app.get("/Appstore")
def Appstore(url: str, max_count: int, lookup_period: str):
    url = url.replace(" ","")
    urls = list(url.split(","))
    data = get_appstore_comment(urls, max_count, lookup_period)
    store_data_to_db.store_to_db(data)
    return convert_to_json(data)

@app.get("/Playstore")
def Playstore(url: str, max_count: int, lookup_period: str):
    url = url.replace(" ","")
    urls = list(url.split(","))
    data = get_playstore_comment(urls, max_count, lookup_period)
    store_data_to_db.store_to_db(data)
    return convert_to_json(data)

@app.get("/Reddit")
def Reddit(url: str, max_count: int, lookup_period: str):
    data = get_reddit_comment(url, max_count, lookup_period)
    store_data_to_db.store_to_db(data)
    return convert_to_json(data)

@app.get("/Google_News")
def News(query: str, max_count: int, lookup_period: str, country: str, lang: str):
    data = get_google_news(query, max_count, lookup_period, country, lang)
    store_data_to_db.store_to_db(data)
    return convert_to_json(data)
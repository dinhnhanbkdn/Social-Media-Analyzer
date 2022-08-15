import sys
sys.path.append('.')
from Scraper.get_url import *
from Scraper.get_comment import *
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class store_data_to_db:
    def __init__(self, name=None, webpage_name=None, url=None, max_count=None, lookup_period=None, country=None, lang=None, query=None):
        self.name = name
        self.webpage_name = webpage_name
        self.url = url
        self.max_count = max_count
        self.lookup_period = lookup_period
        self.country = country
        self.lang = lang
        self.query = query

    def get_data(self):
        if self.name == 'Appstore':
            self.df = get_appstore_comment(self.url, self.max_count, self.lookup_period)
        elif self.name == 'Playstore':
            self.df = get_playstore_comment(self.url, self.max_count, self.lookup_period)
        elif self.name == 'Reddit':
            self.df = get_reddit_comment(self.url, self.max_count, self.lookup_period)
        elif self.name == 'News':
            self.df = get_google_news(self.query, self.max_count, self.lookup_period, self.country, self.lang)
        elif self.name == 'Youtube':
            urls = youtube(self.url)
            self.df = get_youtube_comment(urls, self.max_count, self.lookup_period)
        elif self.name == 'Website':
            if self.webpage_name=='tinhte':
                urls = tinhte(self.url)
                self.df = get_website_comment(urls)
            elif self.webpage_name=='genk':
                urls=genk(self.url)
                self.df=get_website_comment(urls)
            elif self.webpage_name=='techz':
                urls=techz(self.url)
                self.df=get_website_comment(urls)
            elif self.webpage_name=='vietnamnet':
                urls=vietnamnet(self.url)
                self.df=get_website_comment(urls)
            elif self.webpage_name=='24h':
                urls=haibongio(self.url)
                self.df=get_website_comment(urls)
            elif self.webpage_name=='tuoitre':
                urls=tuoitre(self.url)
                self.df=get_website_comment(urls)
            elif self.webpage_name=='vnexpress':
                urls=vnexpress(self.url)
                self.df=get_website_comment(urls)
            elif self.webpage_name=='thanhnien':
                urls=thanhnien(self.url)
                self.df = get_website_comment(urls)
            else:
                raise ValueError('We cannot crawl data from this website')
        else:
            raise ValueError('This platform is not supported! Type one in Playstore, Youtube, Appstore, Website, Reddit, News')
        return self.df
    def store_to_db(data):
        try:
            conn_string = 'postgresql://postgres:postgres@localhost:5432/postgres'
            db = create_engine(conn_string)
            conn = db.connect()
        except:
            raise ValueError ('Can not connect to databse. Check your conn_string value!')
        
        df = data
        df.to_sql('sma', con=conn, if_exists='replace', index=False)
        conn = psycopg2.connect(conn_string
                        )
        conn.autocommit = True
        cursor = conn.cursor()
  
        sql1 = '''select * from sma;'''
        cursor.execute(sql1)
        for i in cursor.fetchall():
            print(i)
  
        # conn.commit()
        conn.close()
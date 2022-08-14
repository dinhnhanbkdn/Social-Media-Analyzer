from Scraper.appstore_scrapper import AppStoreScrapperConfig, AppStoreScrapperSource
from Scraper.playstore_scrapper import PlayStoreScrapperConfig, PlayStoreScrapperSource
from Scraper.reddit_scrapper import RedditScrapperConfig, RedditScrapperSource
from Scraper.google_news_source import GoogleNewsConfig, GoogleNewsSource
from Scraper.youtube_scrapper import YoutubeScrapperSource, YoutubeScrapperConfig
from Scraper.website_crawler_source import TrafilaturaCrawlerConfig, TrafilaturaCrawlerSource
import pandas as pd

#get appstore comment
def get_appstore_comment(urls, max_count, lookup_period):
    try:
        id = []
        author_name=[]
        title = []
        content = []
        rating = []
        platform = []
        for url in urls:
            try:
                source_config = AppStoreScrapperConfig(
                    app_url = url,
                    lookup_period = lookup_period,
                    max_count = max_count
                )
                source = AppStoreScrapperSource()
                source_data = source.lookup(source_config)
                for i in range(0,max_count):
                    source_data[i]=dict(source_data[i])
                    id.append(source_data[i]["meta"]["id"])
                    author_name.append(source_data[i]["meta"]["author_name"])
                    title.append(source_data[i]["meta"]["title"])
                    content.append(source_data[i]["meta"]["content"])
                    rating.append(source_data[i]["meta"]["rating"])
                    platform.append('Appstore')
                df=pd.DataFrame(list(zip(id,author_name,title,content,rating,platform)),columns=['id','author','title','content','rating','source'])
            except:
                pass
    except:
        raise ValueError("Your configuration is not valid!")
    return df

#get playstore comment
def get_playstore_comment(urls, max_count, lookup_period):
    try:
        userName = []
        content = []
        rating = []
        id = []
        title = []
        platform = []
        for url in urls:
            try:
                source_config = PlayStoreScrapperConfig(  
                app_url = url,
                max_count = max_count, 
                lookup_period = lookup_period
                )
                source = PlayStoreScrapperSource()
                data = source.lookup(source_config)    
                for h in range (0, max_count):
                    data[h] = dict(data[h])
                    userName.append(data[h]["meta"]["userName"])
                    content.append(data[h]["meta"]["content"])
                    rating.append(data[h]["meta"]["score"])
                    id.append(data[h]["meta"]["reviewId"])
                    title.append(None)
                    platform.append('Playstore')
                df = pd.DataFrame(list(zip(id,userName,title,content,rating,platform)), columns=['id','author','title','content','rating','source'])
            except:
                pass
    except:
        raise ValueError("Your configuration is not valid!")
    return df

#get reddit comment
def get_reddit_comment(max_comment, url, period):
    source_config = RedditScrapperConfig(
    url=url,
    lookup_period=period
    )
    source = RedditScrapperSource()
    data_source = source.lookup(source_config)
    extracted_text = []
    author = []
    id = []
    title = []
    rating = []
    platform = []
    for i in range(1,max_comment):
      data_source[i]=dict(data_source[i])
      extracted_text.append(data_source[i]["meta"]["extracted_text"])
      author.append(data_source[i]["meta"]["author_name"])
      id.append(data_source[i]["meta"]["id"])
      title.append(None)
      rating.append(None)
      platform.append('Reddit')
    df=pd.DataFrame(list(zip(id,author,title,extracted_text,rating,platform)),columns=['id','author','title','content','rating','source'])

    return df

#Get google news comment
def get_google_news(query, max_results, lookup_period, language, country):
   try:
      userName = []
      content = []
      rating = []
      id = []
      title = []
      platform = []
      source_config = GoogleNewsConfig(
      query=query,
      max_results=max_results, 
      lookup_period=lookup_period,
      language=language,
      country=country
      )  
      source = GoogleNewsSource()
      data = source.lookup(source_config)
      for i in range(0, max_results):
         data[i]=dict(data[i])
         id.append(data[i]["meta"]["extracted_data"]["id"])
         userName.append(data[i]["meta"]["extracted_data"]["author"])
         title.append(data[i]["meta"]["extracted_data"]["title"])
         content.append(data[i]["meta"]["extracted_data"]["raw_text"])
         rating.append(None)
         platform.append(data[i]["meta"]["url"])
      df = pd.DataFrame(list(zip(id,userName,title,content,rating,platform)), columns=['id','author','title','content','rating','source'])
   except:
        raise ValueError("Your configuration is not valid! Try increasing the period value.")
   return df

#Get youtube comment
def get_youtube_comment(urls, max_count, lookup_period):
    try:
        text = []
        author = []
        id = []
        title = []
        rating = []
        platform = []
        for url in urls:
            try:
                ytb_config = YoutubeScrapperConfig(
                video_url = url,
                max_comments = max_count,
                lookup_period = lookup_period
                )
                ytb = YoutubeScrapperSource()
                ytb_response_list = ytb.lookup(ytb_config)
                for y in range (0, max_count):
                    ytb_response_list[y] = dict(ytb_response_list[y])
                    text.append(ytb_response_list[y]["meta"]["text"])
                    author.append(ytb_response_list[y]["meta"]["author"])
                    id.append(ytb_response_list[y]["meta"]["comment_id"])
                    title.append(None)
                    rating.append(None)
                    platform.append('Youtube')
            except:
                pass
        df = pd.DataFrame(list(zip(id,author,title,text,rating,platform)), columns=['id','author','title','content','rating','source'])
    except:
        raise ValueError("Your configuration is not valid!")
    return df

#Get website comment
def get_website_comment(urls):

    source_config = TrafilaturaCrawlerConfig(urls=urls)
    source=TrafilaturaCrawlerSource()
    source_response_list=source.lookup(source_config)

    id = []
    hostname = []
    title = []
    raw_text = []
    rating = []
    platform = []
    for i in range(0, len(source_response_list)):
        source_response_list[i] = dict(source_response_list[i])
        id.append(source_response_list[i]["meta"]["id"])
        hostname.append(source_response_list[i]["meta"]["author"])
        title.append(source_response_list[i]["meta"]["title"])
        raw_text.append(source_response_list[i]["meta"]["raw_text"])
        rating.append(None)
        platform.append(source_response_list[i]["meta"]["source"])
    df = pd.DataFrame(list(zip(id, hostname, title, raw_text,rating,platform)), columns=['id','author','title','content','rating','source'])
    return df
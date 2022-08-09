import requests
from bs4 import BeautifulSoup
import youtube_dl

#1. Get list of urls from a playlist on youtube
def youtube(playlist_url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
    playlist_url = playlist_url
    urls = []
    with ydl:
        result = ydl.extract_info(playlist_url, download=False) #We just want to extract the info
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries']
            #loops entries to grab each video_url
            for i, item in enumerate(video):
                urls.append(result['entries'][i]['webpage_url'])
    return urls

#2. Get list of urls from websites
#Tinhte.vn
def tinhte(webpage_url):
    #HTTP request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.get(webpage_url, headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    output = []
    label_class_list = [['h4','jsx-3501530503 thread-title'], ['div','jsx-2206250852 thread'],
    ['div','jsx-1673213166 item'], ['article','jsx-2238569880'], ['div','jsx-1462321135 slider tinhte'],
    ['div','jsx-1462321135 slider tinhte'], ['h3','searchResultTitle']]
    
    for label_class in label_class_list:
        try:
            titles = soup.findAll(label_class[0], class_=label_class[1])
            links = [link.find('a').attrs["href"] for link in titles]
            for link in links:
                output.append('https://tinhte.vn/'+link)
        except:
            pass
    return output

#Genk.vn
def genk(webpage_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.get(webpage_url, headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    output = []
    label_class_list = [['h3',''],['h2',''],['div','gknews_box gk_flx'],
    ['h4',''],['h4','knswli-title'],['li','relate-news-li'],['div','total']]

    for label_class in label_class_list:
        try:
            titles = soup.findAll(label_class[0], class_=label_class[1])
            links = [link.find('a').attrs["href"] for link in titles]
            for link in links:
                output.append('https://genk.vn/'+link)
        except:
            pass
    return output

#VietnamNet.vn
def vietnamnet(webpage_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.get(webpage_url, headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    output = []
    label_class_list = [['h3','horizontalPost-content__title vnn-title'],['h3','verticalPost-content__title vnn-title'],
    ['h3','slide-eventItem-content__title'], ['h3','title-box-photo'],['h3','horizontalRelatedPost-content__title vnn-title'],
    ['h3','horizontalFeaturePost-content__title vnn-title'],['h3','vnn-title'],
    ['h3','slide-horizontalItem-content__title'],['h3','subcate-bold__related-title vnn-title'],
    ['h3','subcate-bold-s__title vnn-title'],['h3','subcate-bold-s__related-title vnn-title'],
    ['h3','feature-box__content--title vnn-title'],['h2','vnn-title']]

    for label_class in label_class_list:
        try:
            titles = soup.findAll(label_class[0], class_=label_class[1])
            links = [link.find('a').attrs["href"] for link in titles]
            for link in links:
                output.append('https://vietnamnet.vn'+link)
        except:
            pass
    return output

#24h.vn
def haibongio(webpage_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.get(webpage_url, headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    output = []
    label_class_list =[['header','nwsTit cltitbxbdtt'], ['article','lstNml'],
    ['article','vdNml'], ['header','nwsTit titbxdoitrangchu'],['article','lstRdStr'],
    ['article','phtNml'],['header','nwsTit titbxwhome'],['article','icoInfo'],
    ['h3',''],['p','cate-24h-car-news-rand__name margin-bottom-10'],
    ['header','nwsTit'],['header','cate-24h-foot-box-adv-view-news__box--name']]

    for label_class in label_class_list:
        try:
            titles = soup.findAll(label_class[0], class_=label_class[1])
            links = [link.find('a').attrs["href"] for link in titles]
            for link in links:
                output.append(link)
        except:
            pass
    return output

#TuoiTre.vn
def tuoitre(webpage_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.get(webpage_url, headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    output = []
    label_class_list =[['h2','title-focus-title'], ['h2','title-name'],
    ['article','vdNml'], ['header','nwsTit titbxdoitrangchu'],['article','lstRdStr'],
    ['article','phtNml'],['header','nwsTit titbxwhome'],['article','icoInfo'],['h3','title-news'],
    ['h3',''],['h3','title-name-newsvideo w156'],['h3','name-title']]

    for label_class in label_class_list:
        try:
            titles = soup.findAll(label_class[0], class_=label_class[1])
            links = [link.find('a').attrs["href"] for link in titles]
            for link in links:
                output.append('https://tuoitre.vn/'+link)
        except:
            pass
    return output

#VnExpress.vn
def vnexpress(webpage_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.get(webpage_url, headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    output = []
    label_class_list =[['h3','title-news'], ['p','description']]

    for label_class in label_class_list:
        try:
            titles = soup.findAll(label_class[0], class_=label_class[1])
            links = [link.find('a').attrs["href"] for link in titles]
            for link in links:
                output.append(link)
        except:
            pass
    return output
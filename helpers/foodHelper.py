import wikipedia
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import urllib.request, json
from urllib.request import Request, urlopen
from unidecode import unidecode
import html2text
from requests.exceptions import HTTPError
import collections
import sys
from datetime import datetime, tzinfo, timedelta
#theme = "ajedrez"
class simple_utc(tzinfo):
    def tzname(self,**kwargs):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)
class foodHelper:
    def getIndex(self,theme):
        wikipedia.set_lang("es")
        try:
            page = wikipedia.page(theme)

        except wikipedia.DisambiguationError as e:
            theme = e.options[0]
            page = wikipedia.page(theme)

        title = page.title
        title = re.sub(r"\((.*)\)", "", title)
        url = page.url
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')

        for row in soup.find_all('div',attrs={"class" : "toc"}):
            index_theme =  (row.text)

        index_theme = re.sub(r"\d", "", index_theme)
        index_theme = index_theme.split("\n")
        index_theme = [x for x in index_theme if "." not in x]
        index_theme = [x for x in index_theme if "Índice" not in x]
        index_theme = [x for x in index_theme if x != ""]
        index_theme = [x for x in index_theme if x != " "]
        index_theme = [x for x in index_theme if "Notas" not in x]
        index_theme = [x for x in index_theme if "Referencias" not in x]
        index_theme = [x for x in index_theme if "Véase también" not in x]
        index_theme = [x for x in index_theme if "Enlaces externos" not in x]
        index_theme = [x for x in index_theme if "Bibliografía" not in x]
        index_theme.insert(0,title)
        
        return index_theme, url
        
    def getContent(self,theme):
        wikipedia.set_lang("es")
        page = wikipedia.page(title=theme, auto_suggest=True)
        url = page.url
        #categories = page.categories
        content = page.content
        #links = page.links
        references = page.references
        themes = re.findall(r'==(.*?)== ', content, re.DOTALL)
        #themes_n = []
        #for i in range(0, len(themes)):
        #   if themes[i].find("=") != 0:
        #       themes_n.append(str(i)+themes[i])
        #   else:
        #       themes_n.append(themes[i].replace("=",str(i-1) +"."+ str(i-(i-1))))

        #themes_n = "\n".join(themes_n)
        content = re.sub(r"\[\d+\]", "",content)
        #content = re.sub(r"\=\=?", "", content)
        title = page.title
        content = "== "+title+" =="+content
        return content   


    def getContentTheme(self,index_theme):
        getIndex = foodHelper().getIndex(index_theme)
        index_theme = getIndex[0]
        url_theme = getIndex[1]
        theme_dict = {}

        for theme in index_theme:
            content = foodHelper().getContent(index_theme[0])
            theme_content = re.search("(?<="+theme+" ==)([^==]+)", content)
            #theme_dict[theme]["content"] = theme_content
            theme_content_clear = theme_content.group(0).replace("\n","")
            
            if theme_content_clear is not "":
                theme_dict[theme] = theme_content_clear
        
        return theme_dict, url_theme

    def getFood(self,theme):


        # get the API KEY here: https://developers.google.com/custom-search/v1/overview
        API_KEY = "AIzaSyCSrZaUpabnmnyTDJyiod55crferj3uF_0"
        #API_KEY = "AIzaSyDUhIRiVvM4ihyb3Lvr_WeWfbODudgT8BU"

        # get your Search Engine ID on your CSE control panel
        SEARCH_ENGINE_ID = "018122160717511887441:kh7l2lp_nce"
        #SEARCH_ENGINE_ID = "018122160717511887441:vrpvcfj443i"

        # the search query you want
        index_list = foodHelper().getIndex(theme)[0]

        list_food = []
        d = collections.defaultdict(dict)
        j = 0
        for i in range(0, len(index_list)-1):

            index_list[i+1] = index_list[0] + (index_list[i+1]) 
            #index_list[i+1] = (index_list[i+1]) 

            query = "que es " + index_list[i] +"?"
            page = 1
            # constructing the URL
            # doc: https://developers.google.com/custom-search/v1/using_rest
            # calculating start, (page=2) => (start=11), (page=3) => (start=21)
            start = (page - 1) * 10 + 1
            url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
            
            data = requests.get(url).json()
            search_items = data.get("items")
            # iterate over 10 results found
            for i, search_item in enumerate(search_items, start=1):
                # get the page title
                title = search_item.get("title")
                # page snippet
                snippet = search_item.get("snippet")
                # alternatively, you can get the HTML snippet (bolded keywords)
                link = search_item.get("link")
         
                string_split = snippet.split()

                html_snippet = search_item.get("htmlSnippet")
                # extract the page url
                
                #html = urllib.request.urlopen(link).read()
                #html = str(html)
                #asnwer = re.findall(r"El ajedrez es*([^\n\r.]*)", html)
                #req = Request(link, None, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
                from requests.exceptions import ConnectionError
                #try:
                try:
                    r = requests.get(link, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}, allow_redirects=False, timeout=15)

                   
                except Exception as error:
                   print(repr(error))
                   continue
                    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
                    #html = urlopen(r.content).read()

                soup = BeautifulSoup(r.content, 'html.parser')
                body = soup.find('body')
                body = str(body)
                #list_p = re.match(r"\<p.+?(?=\.)", body)
                list_p = re.findall(r"\<p\>.+?(?=\<\/p\>)", body)

                if list_p is None or not list_p:
                    asnwer = snippet
                else:
                    string_space = " "
                    list_string = string_space.join(list_p)
                    asnwer= html2text.html2text(list_string)
     
                list_food.append(query)
                list_food.append(asnwer)

                
                d[str(j)]["id"] = ""
                d[str(j)]["text"] =  asnwer
                d[str(j)]["search_text"] = ""
                d[str(j)]["conversation"] = "training"
                d[str(j)]["persona"] = ""
                
                d[str(j)]["in_response_to"] = query
                d[str(j)]["search_in_response_to"] = query
                d[str(j)]["created_at"] = datetime.utcnow().replace(tzinfo=simple_utc()).isoformat()
                d[str(j)]["tags"] = [query]                
                j = j + 1
                dict_food = dict(d)

        return dict_food




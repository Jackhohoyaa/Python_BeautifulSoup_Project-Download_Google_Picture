import os
import requests as rq
from bs4 import BeautifulSoup as bs 
import time
def creatdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
def connect(url):
    resp=rq.get(url)
    content=resp.text
    return content
def bs4(con):
    soup=bs(con,"lxml")
    return soup
def search_links(soup):    
    img=soup.find_all("img")
    img_links=[]
    for link in img[1:]:
        img_links.append(link.get("src"))
    return img_links
def write_in():
    for i in range(len(links)):
        print("下載第" + str(i+1) + "張")
        with open(dirname + "/" + "第" + str(i+1) + "張" +".jpg","wb") as write_in:
            write_in.write(rq.get(links[i]).content)
            time.sleep(0.3)
    print("完成!!")    
            
if __name__ == "__main__":
    dirname="download"
    creatdir(dirname)
    url=input("請貼上Google搜尋圖片網址:")
    content=connect(url)
    soup=bs4(content)        
    links=search_links(soup)
    write_in()
    

# 파이썬 매뉴얼을 재귀적으로 다운받는 프로그램
# read module

from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

# 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {}

# html 내부 링크 추출 함수 
def enum_link(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']") # css
    links += soup.select("a[href]") # link
    result = []
    
    #href 속성 추출, 링크 절대경로로 변환 
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    
    return result

    # 파일을 다운받고 저장하는 함수
def download_file(url):
    o = urlparse(url)
    savepath = "./"+ o.netloc +o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    # download finish check
    if os.path.exists(savepath) : return savepath
    # make download folder 
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)

    #file download
    try:
        print("downlaod = ", url)
        urlretrieve(url, savepath)
        time.sleep(1) 
        return savepath
    
    except:
        print("download fail ", url)
        return None
    
def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return 
    proc_files[savepath] = True
    print("analyze_html ", url)

    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_link(html, url)
    
    for link_url in links:
        
        if link_url.find(root_url) != 0:
            
            if not re.search(r".css$", link_url): continue

        if re.search(r".(html|htm)$", link_url):
            print(link_url)
            analyze_html(link_url,root_url)
            continue
        
        download_file(link_url)

if __name__ == "__main__" : 
    url = "https://docs.python.org/3.5/library"
    root_url = "https://docs.python.org/3.5"
    analyze_html(url,root_url)
import requests
from bs4 import BeautifulSoup
import urllib.parse

search_word = "디오구 조타"
encoded = urllib.parse.quote(search_word)
url = f"https://search.naver.com/search.naver?where=news&query={encoded}"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# HTML 구조 확인용
print(soup.prettify())

# 뉴스 제목 크롤링
for a_tag in soup.select(".news_tit"):
    print(a_tag.text)
    print(a_tag["href"])

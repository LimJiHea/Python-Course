import requests
from bs4 import BeautifulSoup

# requests => html을 크롤링 
indeed_result = requests.get("https://www.indeed.com/jobs?q=Python&limit=50")

# BeautifulSoup => 가져온 html을 추출하는 패키지
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

#print(indeed_soup)

# find(name, attribute)  페이지 번호 추출
pagination = indeed_soup.find("div",{"class":"pagination"})

#print(pagination)

# a 태그 찾아주기 pages는 리스트다 
pages = pagination.find_all('a')
spans = [] #빈 array

#print(pages)

# a 태그 안에 span을 찾아주세요
# span을 찾아서 빈 array에다 더해준다.
for page in pages : 
  spans.append(page.find("span"))

# -1은 마지막에서부터 시작해서 첫 item을 나타낸다. 
# spans[:-1] => 마지막 제외
# [0:5] => 0~5까지 가져옴 
spans = spans[:-1]
# indeed 다시보기 
  
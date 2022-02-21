import requests
from bs4 import BeautifulSoup

INDEED_URL = "https://www.indeed.com/jobs?q=Python&limit=50"

#indeed 페이지를 추출하는 함수 
def extract_indeed_pages():
  result = requests.get(INDEED_URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div",{"class":"pagination"})
  
  links = pagination.find_all('a')
  pages = [] #빈 array
  for link in links[:-1]: 
    pages.append(int(link.string))  
   
  max_page = pages[-1] #마지막 페이지 숫자 찾기
  return max_page



def extract_indeed_jobs(last_pages)
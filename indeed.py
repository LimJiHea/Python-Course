import requests
from bs4 import BeautifulSoup

LIMIT = 50

URL = f"https://www.indeed.com/jobs?q=Python&limit={LIMIT}"

#indeed 페이지를 추출하는 함수 
def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div",{"class":"pagination"})
  
  links = pagination.find_all('a')
  pages = [] #빈 array
  for link in links[:-1]: 
    pages.append(int(link.string))  
   
  max_page = pages[-1] #마지막 페이지 숫자 찾기
  return max_page


#각 일자리를 나타냄
def extract_indeed_jobs(last_pages):
  jobs =[]
  #for page in range(last_pages):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results =soup.find_all("a", {"class" : "tapItem"})
  for result in results :
    title = result.find("h2", {"class":"jobTitle"}).find("span",title=True).string
    company = result.find("span",{"class":"companyName"})
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
    # title.find("span" ,title=True ) 은 title 이 있는 span 을 찾아라 입니다.
    company = company.strip()
    print("제목 :",title,"회사 : ",company)
  return jobs
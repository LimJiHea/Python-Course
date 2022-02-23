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

#title, company dictionary에 넣고 반환 
def extract_job(html):
   title = html.find("h2", {"class":"jobTitle"}).find("span",title=True).string
   company = html.find("span",{"class":"companyName"})
   company_anchor = company.find("a")
   if company_anchor is not None:
      company = str(company_anchor.string)
   else:
      company = str(company.string)
   company = company.strip()
   location = html.find("div",{"class":"companyLocation"}).string
   print(location)
   return{'title' : title,'company':company,'location':location}
  
  
#각 일자리를 나타냄
def extract_indeed_jobs(last_pages):
  jobs =[]
  #for page in range(last_pages):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results =soup.find_all("a", {"class" : "tapItem"})
  for result in results :
    job = extract_job(result)    #result 가 html을 담고있다.
    jobs.append(job)
  return jobs
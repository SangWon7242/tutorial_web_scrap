# 1. 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

# 2. 스크래핑할 URL 지정
url = "https://news.naver.com/section/105"

# 3. requests를 사용해 웹페이지의 HTML 정보 요청
resp = requests.get(url)

# 4. 응답이 성공적인지 확인 (상태 코드 200은 성공을 의미)
if resp.status_code == 200:      
  # print("요청 성공")
  # print(resp.url)
  # print(resp.text) # HTML 문서를 가져옴
  
  # 5. BeautifulSoup을 사용해 HTML 코드를 파싱 가능한 객체로 변환
  # 'lxml' 파서를 사용하도록 지정
  soup = BeautifulSoup(resp.text, 'lxml')
  # print(soup)
  
  # print(soup.find_all('strong', class_="sa_text_strong"))
  
  '''
  # find_all 문법을 사용하여 검색
  head_line_news_title_list = soup.find_all('strong', class_="sa_text_strong")
  
  for idx, title in enumerate(head_line_news_title_list):
    no = idx + 1
    print(f"{no} : {title.text}")
  '''    
  
  head_line_news_title_list = soup.select(".sa_text_strong")
  # print(head_line_news_title_list)
  
  for idx, title in enumerate(head_line_news_title_list):
    no = idx + 1
    print(f"{no} : {title.text}")
    
else:
  print(f"오류가 발생했습니다. 상태 코드: {resp.status_code}")


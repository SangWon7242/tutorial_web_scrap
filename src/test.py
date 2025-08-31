# 1. 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

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
  
  news_data_list = []
  for idx, title in enumerate(head_line_news_title_list):
    no = idx + 1
    print(f"{no} : {title.text}")
    news_data_list.append(title.text)  
    
   # pandas를 사용하여 데이터를 엑셀 파일로 저장
  if news_data_list: # 수집된 데이터가 있을 경우에만 실행
    # 리스트를 pandas DataFrame으로 변환
    # DataFrame은 엑셀 시트와 같은 표 형태의 데이터 구조
    df = pd.DataFrame(news_data_list)

    # DataFrame을 엑셀 파일로 저장
    # index=False 옵션: 엑셀 파일에 불필요한 인덱스(0, 1, 2...) 열이 생기는 것을 방지
    excel_filename = 'news_data.xlsx'
    
    save_path = f"D:\works\python_projects\scrap_data\{excel_filename}"
    
    df.to_excel(save_path, index=False, engine="openpyxl")
    
    print(f"'{excel_filename}' 파일로 저장이 완료되었습니다.")
  else:
      print("수집된 데이터가 없습니다.")   
    
else:
  print(f"오류가 발생했습니다. 상태 코드: {resp.status_code}")
# 1. 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

# 2. 스크래핑할 URL 지정
url = "https://naver.com"

# 3. requests를 사용해 웹페이지의 HTML 정보 요청
resp = requests.get(url)

# 4. 응답이 성공적인지 확인 (상태 코드 200은 성공을 의미)
if resp.status_code == 200:      
  print("요청 성공")
  print(resp.url)
  print(resp.text) # HTML 문서를 가져옴
else:
  print(f"오류가 발생했습니다. 상태 코드: {resp.status_code}")


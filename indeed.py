'''
각 프로젝트마다 각기 다른 모듈을 가질수 있게 해주는거 = 가상환경
python -m venv venv --> 가상환경 만들어주기
	venv = virtual environment --> venv [name]

pip install --upgrade pip 를 입력하여 pip를 업그레이드 해준다.
나같은경우는 업그레이드 permission이 계속 떠서
py -m pip install --upgrade pip를 입력해줌 (잘한건지는 의문)

'''

''' 
1. 웹사이트 접속
  2. 웹사이트 html 받아오기
  3. html에서 원하는 정보 찾기
  4. 수집
'''

#크롤링에 도움주는 라이브러리인 BeautifulSoup와 Requests 설치
''' BeautifulSoup = html 태그 등 컨텐츠 가져와서 파싱 도와주는 라이브러리
    Requests =  데이터를 요청하는 라이브러리 
    이 두개를 임포트 해서 문제가 없으면 코딩 시작하면 된다'''

import requests
from bs4 import BeautifulSoup

class Scraper() :
    def __init__(self) :
        self.url = "https://kr.indeed.com/jobs?q=python&limit=50"

    def getHTML(self) :
           
 #1. 웹사이트 접속
        res = requests.get(self.url + "&start=" + str(cnt * 50 ))   #str 사용 --> int형변수를 스트링으로 바꾸는 작업
        if res.status_code != 200 :
             print("request error : ", res.status_code)
#위의 jobs 자리는 원래 한글로 적혀있어서(%EC%B7%A8%EC%97%85라고 적혀있었음) ->영어로 바꿔주면 됌
#requests를 사용하여 홈페이지에 get메소드로 접속하고 코드로 뽑아냄
#response의 status code가 200이 아니면 request error라고 뜨게한다. 뒤에는 번호


        html = res.text   #html이라고 안해도된다.
        soup = BeautifulSoup(html, "html.parser")

        return soup
    

#태그와 태그 안에 있는 attribute(div, span etc)
    def getPages(self, soup) :

        pages = soup.select(".pagination > a")
        return len(pages)   #페이지 갯수 리턴
        

#카드 하나하나 데이터 받기 >> 같은 방법으로 확인하면 된다.
def getCards(self, soup) :
    jobCards = soup.find_all("div", class_ = "jobsearch-SerpJobCard")

    #id 받아와서 link클릭하면 상세보기 할 수 있게!

    jobID = []
    jobTitle = []
    jobLocation = []

    for j in jobCards:
         jobID.append("https://kr.indeed.com/viewjob?jk=" +["data-jk"])
         jobTitle.append(j.find("a").text.replace("\n", ""))       #replace("\n", "")는 \n을 ""으로 바꾸기 위한 것(공백)
        #append 사용하는 이유: 처음에 빈배열 사용했으니까, 빈배열은 값에 접근 불가
        #값을 append함수 씀 => 배열의 가장 마지막에 값을 추가해주는 함수
        if j.find("div", class_ = "location") != None :
            jobLocation.append(j.find("div", class_ = "location").text)
        elif j.find("span", class_ = "location") != None :
                jobLocation.append(j.find("span", class_ = "location").text)
    #location이 span이라는 태그로 묶여있음
      

    self.writeCSV(jobID, jobTitle, jobLocation, cnt)    

    def writeCSV(self, jobID, jobTitle, jobLocation) :
        file = open("indeed.csv", "a", newline="")  #공백라인 추가

        wr = csv.writer(file)
        for i in range(len(ID)) :
            wr.writerow([str(i +1 + (cnt + 50)), ID[i], Title[i], Location[i]])

        file.close

    def scrap(self) : 
         soupPage = self.getHTML(0) #첫페이지니 괄호 안의 값은 0
         pages = self.getPages(soupPage)

         file = open("indeed.csv", "w", newline="")   
    wr = csv.writer(file)
    wr.writerow(["No.", "Link", "Title", "Location"])
    file.close

    for i in range(pages) :
        soupCard = self.getHTML(i)
        self.getCards(soupCard, i)
        print("i, "번째 페이지 Done")
if __name__ == "__main__" :
    s = Scraper()
    s.scarp()

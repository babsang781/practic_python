from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd
from tqdm import tqdm_notebook

# 공고 페이지 미리보기 
# driver = wb.Chrome()
# driver.get('http://www.gamejob.co.kr/Recruit/joblist?menucode=duty')

# 크롤링 내용 함수 
def jobkorea_gamedev(page_num, csv_name)
    #잡코리아 게임 개발자 공고 페이지에서 공고 목록을 가져옵니다. 인수는 page 수와, 만들 파일의 이름을 받습니다.
    driver = wb.Chrome()
    time.sleep(0.5)

    driver.get('http://www.gamejob.co.kr/Recruit/joblist?menucode=duty')
    time.sleep(0.5)

    job_list=[]
    company_list=[]
    career_list=[]
    address_list=[]
    sortWork_list=[]
    contract_list=[]
    deadline_list=[]

    for i in tqdm_notebook(range(page_num)):

        job = driver.find_elements_by_css_selector('div.tit>a>strong')
        company = driver.find_elements_by_css_selector('div.company.noLogo>a>strong')
        career = driver.find_elements_by_css_selector('p.info>span:nth-child(1)')
        address = driver.find_elements_by_css_selector('p.info>span:nth-child(3)')
        sortWork = driver.find_elements_by_css_selector('p.info>span:nth-child(4)')
        contract = driver.find_elements_by_css_selector('p.info>span:nth-child(5)')
        deadline = driver.find_elements_by_css_selector('span.date')

        for j in range(len(job)):
            job_list.append(job[j].text)
            company_list.append(company[j].text)
            career_list.append(career[j].text)
            address_list.append(address[j].text)
            sortWork_list.append(sortWork[j].text)
            contract_list.append(contract[j].text)
            deadline_list.append(contract[j].text)

        pageBtn = driver.find_element_by_css_selector('span.btn.now+a')
        pageBtn.click()
        time.sleep(2)

    data = {'구인공고':job_list, '회사명':company_list, '구인경력':career_list, '소재지':address_list,'직무분류':sortWork_list,'계약형태':contract_list}
    df = pd.DataFrame(data)

    df.to_csv(f'{csv_name}.csv', encoding='euc-kr')


# 크롤링 실행 코드
page_num =int(input("수집할 게임 공고 페이지 수를 입력(10p 이상시 에러 가능)>>"))
csv_name=int(input("수집한 csv 파일의 이름 입력>>"))
jobkorea_gamedev(page_num, csv_name)

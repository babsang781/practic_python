import requests as req
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd
import shutil    # 삭제 라이브러리
from bs4 import BeautifulSoup as bs
import os    # 파일 시스템을 위한 라이브러리
from urllib.request import urlretrieve    # urlretrieve: 이미지의 경로를 파일로 저장시켜주는 라이브러리
from urllib import parse


os.mkdir('C:/Users/smhrd/Desktop/이미지')
os.mkdir('C:/Users/smhrd/Desktop/csv')

# 크롤링 페이지 이동
driver = wb.Chrome()
driver.get('http://cocomapet.com/product/list.html?cate_no=496')
time.sleep(1)

# 크롤링 담아줄 df 생성
dic={"num": [], "category": [], "title": [], "price":[],"brand": [], "option": [], "picture_count":[]}
cocomapet = pd.DataFrame(dic)
num=0

# 카테고리별 이동
for i in range(1, len(cate_list)+1):
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(1)
    category = driver.find_element_by_css_selector(f'#contents > div.xans-element-.xans-product.xans-product-menupackage > ul > li:nth-child({i}) > a').text
    driver.find_element_by_css_selector(f'#contents > div.xans-element-.xans-product.xans-product-menupackage > ul > li:nth-child({i}) > a').click()
    time.sleep(1.5)
    
    # 에러 없이 반복하기 -> 반복 횟수 구하기 
    count = int(driver.find_element_by_css_selector('#prdTotal > strong').text)
    if count > 8:
        count = 8
    
    # 세부 아이템 페이지 이동
    for j in range(count):
        num = num+1
        img = driver.find_elements_by_css_selector("img.thumb")
        img[j].click()
        time.sleep(1.5)

        # 세부 페이지 크롤링 제품명, 가격, 브랜드
        title = driver.find_element_by_css_selector(".detail-fixed-wrap > h3").text
        price = driver.find_element_by_css_selector(".product_price_css > td").text
        price = re.sub('원|,', "", price)
        brand = driver.find_element_by_css_selector(".prd_brand_css > td").text
        print(title)

        # 옵션이 있으면 -> 옵션 없이 바로 사이즈가 나오지 않으면
        try:
            temp = driver.find_element_by_css_selector(".detail-fixed-wrap > table > tbody > tr:first-child > th").text
            if temp != '사이즈' :
                options = driver.find_elements_by_css_selector(".ProductOption0 > option:nth-child(n+3)")
                for k in range(len(options)):
                    if k == len(options)-1:
                        option += options[k].text
                    else :
                        option += options[k].text + ','
            else :
                option = ''
        except:
            option = ''
            pass
        
        
        # 이미지 저장 : 폴더 생성 및 썸네일 저장, 
        os.mkdir(f'C:/Users/smhrd/Desktop/이미지/{num}')
        soup = bs(driver.page_source,'lxml')

        # thumnail 저장
        thumnail = soup.select('.BigImage')
        parse_src = parse.quote(thumnail[0]['src'])
        try:
            urlretrieve('http:'+ parse_src, f'C:/Users/smhrd/Desktop/이미지/{num}/thumnail.jpg')
            time.sleep(1.5)
        except:
            pass


        # 상세 설명 이미지 저장
        img = soup.select('#detailarea img')
        for k in range(len(img)):
            parse_src = parse.quote(img[k]['src'])
            try:
                urlretrieve('http://cocomapet.com' + parse_src, f'C:/Users/smhrd/Desktop/이미지/{num}/{k}.jpg')
                time.sleep(1.5)
            except:
                pass             
        picture_count = len(img)

        # df 저장
        one_row={"num": num, "category": category, "title": title, "price": price,"brand": brand, "option": option, "picture_count": picture_count}
        cocomapet = cocomapet.append(one_row, ignore_index = True)
       
        driver.back()
        time.sleep(1.5)
        
    cocomapet.to_csv(f'C:/Users/smhrd/Desktop/csv/cocomapet{num}.csv',encoding='euc-kr')
        
driver.quit()


# 삭제 코드
# import shutil
# shutil.rmtree('C:/Users/smhrd/Desktop/이미지')
#

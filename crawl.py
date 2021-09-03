from selenium import webdriver
import pandas as pd
import datetime

h000='//label[@for="ztree1_3_a"]'
h003='//label[@for="ztree1_4_a"]'
h006='//label[@for="ztree1_5_a"]'
h009='//label[@for="ztree1_6_a"]'

hour_l=[h000,h003,h006,h009]

def crawl(h,name):
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645")
    btn='/html/body/div/div/div/div/div/div/div/form/div/button'

    driver.find_element_by_xpath(h).click()
    driver.find_element_by_xpath(btn).click()

    table=driver.find_element_by_class_name('tbl')
    thead=table.find_element_by_tag_name('thead')
    thr=thead.find_elements_by_tag_name('tr')


    for i,v in enumerate(thr):
        col=v.text.split()
        

    tbody=table.find_element_by_tag_name('tbody')
    tbr=tbody.find_elements_by_tag_name('tr')

    ll=[]
    for i,v in enumerate(tbr):  
        l=v.text.split()
        ll.append(l)
        
    df=pd.DataFrame(ll,columns=col)
    print(df)
    
    df.to_csv('{}'.format(name), encoding='utf-8')

    driver.close()

for i in range(len(hour_l)):
    print(i)
    t=i*3
    name='h00{}_{}.csv'.format(t,datetime.datetime.now().strftime("%Y-%m-%d-%H"))

    crawl(hour_l[i],name)
#coding=utf-8 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

print 'ok'
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By  

import pymysql






def login(browser):
    browser.get('https://passport.threatbook.cn/login?service=s&callbackURL=https%3A%2F%2Fs.threatbook.cn%2Fuser')
    input_items=browser.find_elements_by_class_name('input')
    input_items[0].send_keys(username)
    input_items[1].send_keys(passwd)
    check=browser.find_elements_by_class_name('captcha-zone')[0]
    check.click()
    login=browser.find_elements_by_xpath("//input[@type='submit']")[0]
    login.click()
    print 'login success...'

    
    # picture check ohohoh >_<    ....remain completed



    


def one_page(browser):
    WebDriverWait(browser,20,0.5).until(
    EC.presence_of_element_located((By.LINK_TEXT, u'下一页')))


    result=[]
    for tr in browser.find_elements_by_tag_name('tr'):
        one_piece=[]
        for td in tr.find_elements_by_tag_name('td'):
            one_piece.append(td.text)
        if one_piece!=[]:
            result.append(one_piece)
    ref_list=browser.find_elements_by_xpath("//*[@href]")[7:-5]
    i=0
    counter=0   #counter for logging the matched num
    print 'name num:',len(result),'ref num:',len(ref_list)
    for ref in ref_list:
       '''
       if ref.text==result[i][0]:
           result[i].append(ref.get_attribute('href'))
       else:
           print '[ERROR] Not Matched href and information'
           print '[!]',ref.text
           print '[!]',result[i][0]
       i+=1
       '''
       result[counter].append(ref.get_attribute('href'))
       counter+=1
           
           
    print 'matched:',counter
    return result

def goto_next_page(browser):
        
    browser.find_elements_by_link_text(u"下一页")[0].click()
    return 0


def sql_save():
    db=pymysql.connect('127.0.0.1','root','root','threatbook')

option = webdriver.ChromeOptions()
#option.add_argument("headless")
browser= webdriver.Chrome(chrome_options=option)
url="https://s.threatbook.cn/sample"
browser.get(url)

pages=1
while(pages<4):
    out=one_page(browser)
    print 'page:',pages,' , itmes num:',len(out)
    print '********************************************'
    for i in out:
        print '======'
        print i
    pages+=1
    goto_next_page(browser)#go to next page
raw_input('press any key...')
browser.quit()

        
    

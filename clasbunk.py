from list_cal import geturlcal,getnamecal
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.chrome.options import Options
from whatsapp import sendmsg
import datetime
from cifo import cinfo

def msgchk():
    msg = driver.find_elements_by_xpath('//div[@data-message-text]')
    for m in msg:
        m = m.text
        if ('forms.gle' in m):
            sendmsg(m)
            msgchk.__code__ = (lambda : None).__code__
        else:
            print(m)

def noatnd():
    elm = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]')
    atnd = elm.text
    atnd = atnd.replace('(','')
    atnd = atnd.replace(')','')
    return int(atnd)

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })
url = geturlcal()
name = getnamecal()
driver = webdriver.Chrome(chrome_options=opt)
username = cinfo("email")
password = cinfo("password")

if url == 'nut':
    url = input('Enter url: ')

if (url != 'nut' and 'MataAuto' in name) :
    driver.get('https://calendar.google.com/')
    time.sleep(2)

    elem = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)

    elem = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.get(remove_html_tags(url))
    elem = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div')
    elem.click()
    elem = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div')
    elem.click()
    time.sleep(5)
    elem = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span')
    elem.click()
    #joined meet
    # time.sleep(10)
    # elem = driver.find_element(By.xpath("//span[contains(@class, 'myclass')"))
    # elem.click()
    name = name.replace('MataAuto','')
    msg = name + ' lecture started' 
    '''open chat box'''
    sendmsg(msg)
    time.sleep(10)
    elem = driver.find_elements_by_xpath('//span[@class="l4V7wb Fxmcue"]/span[@class="NPEfkd RveJvd snByac"]/div[@class="ZaI3hb"]/div[@class="HKarue"]')
    elem[0].click()

    minatn = cinfo("minatn")

    '''participants check'''
    time.sleep(2)
    aln = noatnd()
    time.sleep(900)
    while (aln>minatn):
        '''Edit the sleep'''
        time.sleep(600)
        print('No. of participants:- ')
        print(aln)
        msgchk()
        aln = noatnd()
    print('Less than 2')
    sendmsg('Lecutre ended')
    driver.quit()
    quit()

else:
    driver.quit()
    quit()
    print('No link') 

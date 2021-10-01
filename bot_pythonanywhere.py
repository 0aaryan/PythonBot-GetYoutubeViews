from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
import smtplib
import time


def get_views(browser, url, your_id):
    browser.get(url)
    tv = {}
    for video in browser.find_elements_by_id('video-title'):
        title = video.get_attribute('aria-label').split('by')[0]
        views = video.get_attribute('aria-label').split()[-2]
        tv[title] = views
    gmailId='gmail id from which you want to send mail'  #change this line
    passWord='password of gmail id from which you want to send mail'  #change this line
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmailId, passWord)
    message = '\nHi, This Bot is Created By Aryan\nGithub:0aaryan\n\n'
    i=1
    for key in tv:
        message+=str(i)+') '+key+' views= '+tv[key]+'\n'
        i+=1
    s.sendmail(gmailId, your_id, message.encode())
    s.quit()
def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    # url of channel
    url = 'https://www.youtube.com/channel/UCsn-vyCh1doEFSCyXJOxC-w/videos'  #change this line
    #id where you want to recive mail
    your_id='yourmail@gmail.com' #change this line
    get_views(browser, url,your_id)


main()

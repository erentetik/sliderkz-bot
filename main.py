

from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from data import track_list


PATH = 'PATH OF CHROMEDRIVER'
options = webdriver.ChromeOptions();
options.add_argument('--disable-logging') 
driver = webdriver.Chrome(PATH, chrome_options=options)

driver.get('https://slider.kz')
popup = driver.find_element_by_xpath('//*[@id="fullwrapper"]/div')
popup.click()
failed_songs = []







for i in range (len(track_list)):
    artist_name = track_list[i][0]
    if artist_name == 'Various Artists':
        artist_name = ''
    track_name = artist_name +' '+ track_list[i][1]
    

    search = driver.find_element_by_xpath('//*[@id="buttonSearch"]/input')
    search.send_keys(track_name)
    search_button = driver.find_element_by_xpath('//*[@id="searchButton"]')
    search_button.click()
    
    time.sleep(5)
    download_button = driver.find_element_by_xpath('//*[@id="liveaudio"]/div[2]/div[2]/div[2]/a/img')
    download_button.click
    time.sleep(2)

    


    refresh = driver.find_element_by_xpath('//*[@id="logo"]')
    refresh.click()
    time.sleep(2) 


time.sleep(180)
driver.quit
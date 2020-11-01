import requests
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




def authINSTA(browser, login, password):
    browser.get('https://instagram.com')
    x_path = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
    #index_email = browser.find_element_by_xpath('')
    #
    #index_pass = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
    #index_pass.send_keys(str(password))
    #index_email.send_keys(Keys.RETURN)

    try:
        wait = WebDriverWait(browser, 10)
        # Likes.showLikes(this, 'photo478213627_457257241', {})
        # element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="like_btn like _like"]')))
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
    except:
        if element is None:
            print('not found')
    element.send_keys(login)
    #time.sleep(5)
    x_path = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
    try:
        wait = WebDriverWait(browser, 10)
        # Likes.showLikes(this, 'photo478213627_457257241', {})
        # element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="like_btn like _like"]')))
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
    except:
        if element is None:
            print('not found')
    element.send_keys(password)
    #time.sleep(5)

    x_path ='/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]'
    try:
        wait = WebDriverWait(browser, 10)
        # Likes.showLikes(this, 'photo478213627_457257241', {})
        # element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="like_btn like _like"]')))
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
    except:
        if element is None:
            print('not found')
    #element.send_keys(password)
    element.click()
    time.sleep(3)

    x_path = '/html/body/div[1]/section/main/div/div/div/div/button'
    try:
        wait = WebDriverWait(browser, 10)
        # Likes.showLikes(this, 'photo478213627_457257241', {})
        # element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="like_btn like _like"]')))
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element.click()
    except:
        if element is None:
            print('not found')

def likeINSTA(browser, post_url):
    browser.get(post_url)
    element = None
    try:
        x_path = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span/svg/path'
        # wait = WebDriverWait(browser, 10)
        #time.sleep(3)
        # element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="like_btn like _like"]')))
        # element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
    except:
        if element is None:
            print('not found')

    element.click()
    #browser.execute_script("arguments[0].click();", element)
    #time.sleep(5)

def subINSTA(browser, url):
    browser.get(url)
    element = None
    try:
        x_path = '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button'
        wait = WebDriverWait(browser, 10)
        #time.sleep(3)
        # element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="like_btn like _like"]')))
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
        element.click()
    except:
        if element is None:
            print('not found')


    #browser.execute_script("arguments[0].click();", element)
    #time.sleep(5)

def INSTAliking(login, password, url):
    browser = Firefox()


    # 02001554689644:Xxxx555444
    authINSTA(browser, str(login), str(password))
    likeINSTA(browser, url)
    browser.close()






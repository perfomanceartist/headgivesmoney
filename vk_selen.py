import requests
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def authVK(browser, login, password, sleep=5):
    browser.get('https://vk.com')
    index_email = browser.find_element_by_id('index_email')
    index_email .send_keys(login)
    index_pass = browser.find_element_by_id('index_pass')
    index_pass.send_keys(password)
    index_email.send_keys(Keys.RETURN)
    time.sleep(sleep)


def likeVK(browser, post_url,action):
    browser.get(post_url)
    element = None
    if action == 'Лайкнуть фотографию' or action == 'Лайкнуть запись на стене':
        texts = post_url.split('m/')
        post = texts[1]
        attr = "Likes.showLikes(this, '" + str(post) + "', {})"
        x_path = '//a[@onmouseover="{}"]'.format(attr)
        try:
            wait = WebDriverWait(browser, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
            browser.execute_script("arguments[0].click();", element)
        except:
            if element is None:
                print('not found')


def VKrepost(browser, post_url):
    browser.get(post_url)
    element = None
    texts = post_url.split('m/')
    if post_url.find('market') != -1:
        print('market')
        try:
            x_path = '/html/body/div[14]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[1]/div/div/div[1]/a[2]'
            wait = WebDriverWait(browser, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
            browser.execute_script("arguments[0].click();", element)
            element.click()
        except:
            if element is None:
                print('not found')

    elif post_url.find('photo') != -1:
        print('photo')
        try:
            x_path = '/html/body/div[4]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[3]/div/div[1]/a[2]'
            wait = WebDriverWait(browser, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
            browser.execute_script("arguments[0].click();", element)
            element.click()
        except:
            if element is None:
                print('not found')

    elif post_url.find('video') != -1:
        print('video')
        try:
            x_path = '/html/body/div[13]/div/div[2]/div/div[6]/div[1]/div/div[1]/div[2]/div/div/div/div[1]/a[2]'
            wait = WebDriverWait(browser, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
            browser.execute_script("arguments[0].click();", element)
            element.click()
        except:
            if element is None:
                print('not found')

    else:

        post = texts[1]
        attr = "Likes.showShare(this, '" + str(post) + "');"
        x_path = '//a[@onmouseover="{}"]'.format(attr)
        try:
            wait = WebDriverWait(browser, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
            browser.execute_script("arguments[0].click();", element)
        except:
            if element is None:
                print('not found')


    try:
        attr = "if (!hasClass(this, 'disabled')) ShareBox.rbChanged(this, 0);"
        x_path = '//div[@onclick="{}"]'.format(attr)
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element.click()
    except:
        if element is None:
            print('not found')


    try:
        attr = "cur.sbSend()"
        x_path = '//button[@onclick="{}"]'.format(attr)
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element.click()
    except:
        if element is None:
            print('not found')

def VKgroupFollow(browser, post_url):
    browser.get(post_url)
    attr = "join_button"
    x_path = '//button[@id="{}"]'.format(attr)
    element = None
    try:
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element.click()
    except:
        if element is None:
            print('not found')

def VKpublicSubscribe(browser, post_url):
    browser.get(post_url)
    attr = "public_subscribe"
    x_path = '//button[@id="{}"]'.format(attr)
    element = None
    try:
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element.click()
    except:
        if element is None:
            print('not found')

def VKuserSubscribe(browser, post_url):
    browser.get(post_url)
    attr = "flat_button button_wide"
    x_path = '//button[@class="{}"]'.format(attr)
    element = None
    try:
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        element.click()
    except:
        if element is None:
            print('not found')


def VKliking(urls, actions):
    #options = Options()
    #options.headless = True
    browser = Firefox()
    #02001554689644: Xxxx555444
    authVK(browser, '02001554689644', 'Xxxx555444')
    i = 0
    for url in urls:
        likeVK(browser, url, actions[i])
        i += 1
    browser.close()

def VKfollowing(browser, url, action):
    if action.find('Вступить в группу') != -1:
        VKgroupFollow(browser, url)
    elif action.find('Подписаться на страницу') != -1:
        VKpublicSubscribe(browser, url)
    elif action.find('Подписаться на пользователя') != -1:
        VKuserSubscribe(browser, url)
    else:
        print('error in VKfollowing')

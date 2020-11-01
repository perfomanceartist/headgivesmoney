import bosslike as bl
import vk_selen as vk
import time
import accsdb
from selenium import webdriver
import insta_selen
import sqlite3
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
def checkIP():
    pass
    #ip = requests.get('http://checkip.dyndns.org').content
    #soup = BeautifulSoup(ip, 'html.parser')
    #print(soup.find('body').text)



def regaccount(email, password, refer, vk, vkpass, insta, instapass):
    token = bl.create_user(email, password, referer_id= refer)
    bl1 = bl.Bosslike(bl.token)
    accsdb.add_account(email, password, token, vk, vkpass, insta, instapass)
    #add proxy
    browser = vk.Firefox()
    vk.authVK(browser, vk, vkpass)
    token = bl1.acc_check('https://vk.com/' + vk, type=1)
    if token is not None:
        task = bl1.show_like(token)
    else:
        print('error')
    if task is not None:
        vk.likeVK(browser, task.url, task.action)
        bl1.check_like(task.id)
    else:
        print('error')

    insta_selen.authINSTA(browser, insta, instapass)
    token = bl1.acc_check('https://instagram.com/' + insta, type=3)
    if token is not None:
        task = bl1.show_like(token)
    else:
        print('error')
    if task is not None:
        insta_selen.likeINSTA(browser, task.url)
        bl1.check_like(task.id)
    else:
        print('error')


def firefox_proxy(proxy):
    #proxy = '5.101.87.190:8000'

    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_capabilities['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy
    }
    return firefox_capabilities

def work():
    num = 1
    info = list(accsdb.get_account(num))
    bl1 = bl.Bosslike(info[3])
    browser = vk.Firefox(capabilities = firefox_proxy('5.101.87.190:8000'))
    vk.authVK(browser, info[4], info[5])
    vk_tasks = bl1.get_tasks(1, 1)
    for task in vk_tasks:
        if task.action == 'Лайкнуть фотографию' or task.action == 'Лайкнуть запись на стене':
            url = bl1.task_init(task.id)
            if url is not None:
                vk.likeVK(browser, url, task.action)
                bl1.task_check(task.id)
                time.sleep(5)
    vk_tasks = bl1.get_tasks(1, 2)

    for task in vk_tasks:
        if task.action != 'Рассказать друзьям о фотографии' and task.action != 'Рассказать друзьям о видео':
            url = bl1.task_init(task.id)
            if url is not None:
                vk.VKrepost(browser, url)
                bl1.task_check(task.id)
                time.sleep(5)
    vk_tasks = bl1.get_tasks(1, 3)
    for task in vk_tasks:
        if task.action != 'Рассказать друзьям о фотографии' and task.action != 'Рассказать друзьям о видео':
            url = bl1.task_init(task.id)
            if url is not None:
                vk.VKfollowing(browser, url, task.action)
                bl1.task_check(task.id)
                time.sleep(5)



def instawork():
    bl1 = bl.Bosslike(bl.API_KEY)
    browser = vk.Firefox()
    insta_selen.authINSTA(browser, 'Itachi_besthero', 'naruto1337')
    tasks = bl1.get_tasks(3, 1)
    for task in tasks:
        url = bl1.task_init(task.id)
        if url is not None:
            insta_selen.likeINSTA(browser, url)
            time.sleep(3)
            bl1.task_check(task.id)
            time.sleep(2)

    tasks = bl1.get_tasks(3, 3)
    for task in tasks:
        url = bl1.task_init(task.id)
        if url is not None:
            insta_selen.subINSTA(browser, url)
            time.sleep(3)
            bl1.task_check(task.id)
            time.sleep(2)






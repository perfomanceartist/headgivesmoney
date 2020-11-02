import bosslike as bl
import vk_selen as vk
import time
import json
import accsdb
from selenium import webdriver
import insta_selen
def checkIP():
    pass
    #ip = requests.get('http://checkip.dyndns.org').content
    #soup = BeautifulSoup(ip, 'html.parser')
    #print(soup.find('body').text)



def regaccount(email, password, refer, vklogin, vkpass, insta, instapass):
    token = bl.create_user(email, password)
    bl1 = bl.Bosslike(token)
    accsdb.add_account(email, password, token, vklogin, vkpass, insta, instapass)
    #add proxy
    browser = vk.Firefox()
    vk.authVK(browser, vk, vkpass)
    token = bl1.acc_check('https://vk.com/' + vklogin, type=1)
    task = None
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

def vkliking(bl1, browser, task):
    if task.action == 'Лайкнуть фотографию' or task.action == 'Лайкнуть запись на стене':
        url = bl1.task_init(task.id)
        if url is not None:
            vk.likeVK(browser, url, task.action)
            bl1.task_check(task.id)


def instaliking(bl1, browser, task):
    url = bl1.task_init(task.id)
    if url is not None:
        insta_selen.likeINSTA(browser, url)
        bl1.task_check(task.id)

def vkwork(bl1, browser):
    #num = 1
    #info = list(accsdb.get_account(num))
    #bl1 = bl.Bosslike(info[3])
    #browser = vk.Firefox(capabilities = firefox_proxy('5.101.87.190:8000'))
    #vk.authVK(browser, info[4], info[5])
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
    # bl1 = bl.Bosslike(bl.API_KEY)
    # browser = vk.Firefox()
    # insta_selen.authINSTA(browser, 'Itachi_besthero', 'naruto1337')
    # tasks = bl1.get_tasks(3, 1)
    # for task in tasks:
    #     url = bl1.task_init(task.id)
    #     if url is not None:
    #         insta_selen.likeINSTA(browser, url)
    #         time.sleep(3)
    #         bl1.task_check(task.id)
    #         time.sleep(2)
    #
    # tasks = bl1.get_tasks(3, 3)
    # for task in tasks:
    #     url = bl1.task_init(task.id)
    #     if url is not None:
    #         insta_selen.subINSTA(browser, url)
    #         time.sleep(3)
    #         bl1.task_check(task.id)
    #         time.sleep(2)


    starttime = time.time()
    lastwork = 0
    lastaction = ''
    likedelay = 30 #sec
    subdelay = 130 #sec
    absdelay = 120 #sec
    #maxlike =
    while(starttime + 25*60 < time.time()):
        if time.time() - lastwork >= likedelay:
            #do like
            pass



class Acc:
    proxy = ''
    key = ''
    vk = ''
    vkpass = ''
    insta = ''
    instapass = ''

def start():
    proxies = []
    accs = []
    id = 0
    for proxy in proxies:
        acc = Acc()
        acc.proxy = proxy
        accdb = accsdb.get_account(id)
        acc.key = accdb[3]
        acc.vk = accdb[4]
        acc.vkpass = accdb[5]
        acc.insta = accdb[7]
        acc.instapass = accdb[8]
        accs.append(acc)
        id += 1
    return accs


def working_withgroup():
    with open("vkstrat.json", "r") as write_file:
        vkstrategy = json.load(write_file)
    with open("instastrat.json", "r") as write_file:
        instastrategy = json.load(write_file)
    accs = start()
    sessions = []
    instastats = []
    vkstats = []
    bls = []
    for acc in accs:
        session = vk.Firefox(firefox_proxy(acc.proxy))
        sessions.append(session)
        vk.authVK(session, acc.vk, acc.vkpass)
        insta_selen.authINSTA(session, acc.insta, acc.instapass)
        _bl = bl.Bosslike(acc.key)
        bls.append(_bl)
        stat = {}
        stat['totaltime'] = 0
        stat['likes'] = 0
        stat['reposts'] = 0
        stat['subs'] = 0
        stat['lastworktime'] = time.time()
        stat['lastlike']  = 0
        stat['lastsub'] = 0
        stat['workingtime'] = 0
        stat['status'] = 'resting'
        vkstats.append(stat)
        instastats.append(stat)
    accs_num = len(accs)

    for i in range(accs_num):
        if vkstats[i]['lastworktime'] + vkstrategy['resttime'] * 60 < time.time() and vkstats[i]['totaltime'] < vkstrategy['maxworktime']:
            vkstats[i]['workingtime'] = time.time()
            while time.time() -  vkstats[i]['workingtime'] < vkstrategy['worktime']:
                if vkstats[i]['likes'] < vkstrategy['like']['limit'] :
                    if vk_tasks is None:
                        vk_tasks = bls[i].get_tasks(1, 1)
                    vkliking(bls[i], sessions[i], vk_tasks.pop(0))
                    vkstats[i]['likes'] += 1
                    #vkstats[i]['lastlike'] = time.time()
                    time.sleep(vkstrategy['like']['delay'])
            vkstats[i]['lastworktime'] = time.time()



        if instastats[i]['lastworktime'] + instastrategy['resttime'] * 60 < time.time() and instastats[i]['totaltime'] < instastrategy['maxworktime']:
            instastats[i]['workingtime'] = time.time()
            while time.time() -  instastats[i]['workingtime'] < instastrategy['worktime']:
                if instastats[i]['likes'] < instastrategy['like']['limit'] :
                    if insta_tasks is None:
                        insta_tasks = bls[i].get_tasks(1, 1)
                    instaliking(bls[i], sessions[i], vk_tasks.pop(0))
                    instastats[i]['likes'] += 1
                    #vkstats[i]['lastlike'] = time.time()
                    time.sleep(instastrategy['like']['delay'])


        if vkstats[i]['lastworktime'] + vkstrategy['resttime'] * 60 < time.time() and vkstats[i]['totaltime'] < vkstrategy['maxworktime']:
            if time.time() - vkstats['lastworktime']< vkstrategy['delay']:
                time.sleep(vkstrategy['delay'] + vkstats['lastworktime'] -  time.time() )
            vkstats[i]['workingtime'] = time.time()
            while time.time() -  vkstats[i]['workingtime'] < vkstrategy['worktime']:
                if vkstats[i]['subs'] < vkstrategy['sub']['limit'] :
                    if vk_tasks is None:
                        vk_tasks = bls[i].get_tasks(1, 3)
                    vkliking(bls[i], sessions[i], vk_tasks.pop(0))
                    vkstats[i]['subs'] += 1
                    # vkstats[i]['totaltime'] += time.time() - vkstats[i]['lastworktime']
                    vkstats[i]['lastsub'] = time.time()
                time.sleep(vkstrategy['sub']['delay'])

        if instastats[i]['lastworktime'] + instastrategy['resttime'] * 60 < time.time() and instastats[i]['totaltime'] < instastrategy['maxworktime']:
            instastats[i]['workingtime'] = time.time()
            while time.time() -  instastats[i]['workingtime'] < instastrategy['worktime']:
                if instastats[i]['likes'] < instastrategy['like']['limit'] :
                    if insta_tasks is None:
                        insta_tasks = bls[i].get_tasks(1, 1)
                    instaliking(bls[i], sessions[i], vk_tasks.pop(0))
                    instastats[i]['likes'] += 1
                    #vkstats[i]['lastlike'] = time.time()
                    time.sleep(instastrategy['like']['delay'])



def working_roundrobin():
    with open("strat.json", "r") as write_file:
        strategy = json.load(write_file)
    accs = start()
    sessions = []
    instastats = []
    vkstats = []
    bls = []
    for acc in accs:
        session = vk.Firefox(firefox_proxy(acc.proxy))
        sessions.append(session)
        vk.authVK(session, acc.vk, acc.vkpass)
        insta_selen.authINSTA(session, acc.insta, acc.instapass)
        _bl = bl.Bosslike(acc.key)
        bls.append(_bl)
        stat = {}
        stat['totaltime'] = 0
        stat['likes'] = 0
        stat['reposts'] = 0
        stat['subs'] = 0
        stat['lastworktime'] = time.time()
        stat['lastlike']  = 0
        stat['lastsub'] = 0
        stat['status'] = 'resting'
        vkstats.append(stat)
        instastats.append(stat)
    accs_num = len(accs)

    for i in range(accs_num):
        if vkstats[i]['lastworktime'] + strategy['resttime'] * 60 >= time.time():
            continue
        if vkstats[i]['totaltime'] >= strategy['maxworktime']:
            continue
        if vkstats[i]['likes'] < strategy['like']['limit'] and vkstats[i]['lastlike'] + strategy['like']['delay'] < time.time():
            vk_tasks = bls[i].get_tasks(1, 1)
            vkliking(bls[i], sessions[i], vk_tasks.pop(0))
            vkstats[i]['likes'] += 1
            #vkstats[i]['totaltime'] += time.time() - vkstats[i]['lastworktime']
            vkstats[i]['lastlike'] = time.time()

            #do likes
        if vkstats[i]['subs'] < strategy['sub']['limit'] and vkstats[i]['lastsub'] + strategy['sub']['delay'] < time.time():
            vk_tasks = bls[i].get_tasks(1, 3)
            vkliking(bls[i], sessions[i], vk_tasks.pop(0))
            vkstats[i]['subs'] += 1
            # vkstats[i]['totaltime'] += time.time() - vkstats[i]['lastworktime']
            vkstats[i]['lastsub'] = time.time()


def makestrategy():
    strategy = {}
    strategy['worktime'] = 10 #min
    strategy['resttime'] = 10 #min
    strategy['maxworktime'] = 2*60 #min
    strategy['delay'] = 5 #sec
    strategy['like'] = {}
    strategy['repost'] = {}
    strategy['sub'] = {}
    strategy['like']['delay'] = 5 #sec
    strategy['like']['limit'] = 2000 # за сутки максимально сделает 2000 заданий
    strategy['repost']['delay'] = 5  # sec
    strategy['repost']['limit'] = 2000  # за сутки максимально сделает 2000 заданий
    strategy['sub']['delay'] = 5  # sec
    strategy['sub']['limit'] = 2000  # за сутки максимально сделает 2000 заданий
    with open("strat.json", "w") as write_file:
        json.dump(strategy, write_file)

# import requests
# url = 'https://api-public.bosslike.ru/v1/bots/tasks'
# params = {'service_type': 3, 'task_type': 4}
# headers = {'Accept': 'application/json', 'X-Api-Key': bl.API_KEY}
# responce = requests.get(url, params=params, headers=headers)
# json_answer = responce.json()
# #print(json_answer)
# tasks = []
#
# items = json_answer['data']['items']
# id = items[1]['id']
# url = 'https://api-public.bosslike.ru/v1/bots/tasks/' + str(id) + '/do'
# headers = {'Accept': 'application/json', 'X-Api-Key': bl.API_KEY}
# responce = requests.get(url, headers=headers)
#
# print(responce.json())


# import yt_selen as yt
#
# browser = vk.Firefox()
#
# yt.YT_Auth(browser, 'kreltinman', 'ArgentumMeiDomini1685GO')




regaccount('natomocu@legsadesi.bizml.ru', 'AUzOxwh', '-', '79535669576', 'hacked12345', 'zarakorytko', '1W3VjjJ7Y6r818')

#molnimlima@plecmager.bizml.ru:uQ0sREtUVs
#79869524136:natalove)#hacked12345

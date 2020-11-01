import requests
API_KEY = '4ec13103faf2bf758cc1b0d719fb6815e452fa261941a0e9'
#API KEY for g.climt : 1ed142becce1c1f2cdf37d332275d5c6930ab81ab8a06d39

class Task:
    service = 1
    task_type = 1
    id = 0
    action = 'Лайкнуть'

class Bosslike:
    def __init__(self, key):
        self.API_KEY = key

    def get_tasks(self, service=1, task_type=0):
        url = 'https://api-public.bosslike.ru/v1/bots/tasks'
        params = {'service_type': service, 'task_type': task_type}
        headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
        responce = requests.get(url, params=params, headers=headers)
        json_answer = responce.json()
        tasks = []
        if responce.status_code != 200:
            print('error while getting tasks')
            print(responce.json())
        items = json_answer['data']['items']
        for item in items:
            task = Task()
            task.id = item['id']
            task.action = item['name']['action']
            task.service = service
            task.task_type = item['task_type']
            tasks.append(task)

        return tasks

    def task_init(self, id):
        url = 'https://api-public.bosslike.ru/v1/bots/tasks/' + str(id) + '/do'
        headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
        responce = requests.get(url, headers=headers)
        if responce.status_code != 200:
            print(responce.json())
        else:
            return responce.json()['data']['url']

    def task_check(self, id):
        url = 'https://api-public.bosslike.ru/v1/bots/tasks/' + str(id) + '/check'
        headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
        params = {'id':int(id)}
        responce = requests.get(url, params=params, headers=headers)
        print(responce.url)
        if responce.status_code != 200:
            print(responce.json())
        else:
            print('ok')

    def make_tasks(self):
        for i in range(1, 8):
            # return list of tasks_id
            tasks = self.get_tasks()
            for task in tasks:
                id = task.id
                # returns url of task
                url = self.task_init(id)

                # make the job
                # here would be selenium function

                self.task_check(id)


    def acc_check(self, link, type=3):
        url = 'https://api-public.bosslike.ru/v1/bots/users/me/social/auth/like/check-profile'
        data = {'url': link, 'type': type}
        headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
        responce = requests.post(url, headers=headers, data=data)
        if responce.status_code == 200:
            print('ok')
            return responce.json()['data']['token']
        else:
            print('error while checking account ' + str(responce.status_code))
            print(responce.json())
            return None

    def show_like(self, token):
        url = 'https://api-public.bosslike.ru/v1/bots/users/me/social/auth/like/show-like'
        params = {'token': token}
        headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
        responce = requests.get(url, headers=headers, params=params)
        if responce.status_code == 200:
            print('ok')
            print(responce.json()['data']['url'])
            print(responce.json()['data']['token'])
            return responce.json()['data']['token']
        else:
            print('error while getting url : ' + str(responce.status_code))
            return None

    def check_like(self, token):
        url = 'https://api-public.bosslike.ru/v1/bots/users/me/social/auth/like/check-like'
        params = {'token': token}
        headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
        responce = requests.get(url, headers=headers, params=params)
        if responce.status_code == 201:
            print('ok')
        else:
            print('error while checking completed action: ' + str(responce.status_code))

    def account_attach(self, nicknames):
        urls = []
        urls[0] = 'https://vk.com/' + nicknames[0]
        urls[1] = 'https://instagram.com' + nicknames[1]
        urls[2] = 'https://twitter.com' + nicknames[2]
        type = 1
        for url in urls:
            token = self.acc_check(url, type=type)
            if token is not None:
                token = self.show_like(token)
            else:
                print('error')

            if token is not None:
                pass
                #check_like(token)
            else:
                print('error')

            type += 2


def create_user(email, password='password1234', referer_id = None):
    if referer_id is None:
        data = {'email':email, 'password':password, 'password_repeat':password}
    else:
        data = {'email': email, 'password': password, 'password_repeat': password, 'referer_id':referer_id}

    url = 'https://api-public.bosslike.ru/v1/bots/users/create/'
    responce = requests.post(url, data=data)
    print(responce.status_code)
    if responce.status_code == 201:
        token = responce.json()['data']['token']['key']
        print(token)
        return token
    else:
        print(responce.json())


# import requests
#
# API_KEY = '4ec13103faf2bf758cc1b0d719fb6815e452fa261941a0e9'
# #API KEY for g.climt : 1ed142becce1c1f2cdf37d332275d5c6930ab81ab8a06d39
#
#
# class Task:
#     service = 1
#     task_type = 1
#     id = 0
#     action = 'Лайкнуть'
#
# class Bosslike:
#     def __init__(self, key):
#         self.API_KEY = key
#
#     def get_tasks(self, service=1, task_type=0):
#         url = 'https://api-public.bosslike.ru/v1/bots/tasks'
#         params = {'service_type': service, 'task_type': task_type}
#         headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
#         responce = requests.get(url, params=params, headers=headers)
#         json_answer = responce.json()
#         tasks = []
#         if responce.status_code != 200:
#             print('error while getting tasks')
#             print(responce.json())
#         items = json_answer['data']['items']
#         for item in items:
#             task = Task()
#             task.id = item['id']
#             task.action = item['name']['short_action']
#             task.service = service
#             task.task_type = item['task_type']
#             tasks.append(task)
#
#         return tasks
#
#     def task_init(self, id):
#         url = 'https://api-public.bosslike.ru/v1/bots/tasks/' + str(id) + '/do'
#         headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
#         responce = requests.get(url, headers=headers)
#         print(responce.url)
#         if responce.status_code != 200:
#             print(responce.json())
#         else:
#             #print('task inited')
#             print(responce.json()['data']['url'])
#             return responce.json()['data']['url']
#
#     def task_check(self, id):
#         url = 'https://api-public.bosslike.ru/v1/bots/tasks/' + str(id) + '/check'
#         headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
#         responce = requests.get(url, headers=headers)
#         print(responce.url)
#         # json_answer = responce.json()
#         if responce.status_code != 200:
#             print(responce.status_code)
#         else:
#             print('ok')
#
#     def make_tasks(self):
#         for i in range(1, 8):
#             # return list of tasks_id
#             tasks = self.get_tasks()
#             for task in tasks:
#                 id = task.id
#                 # returns url of task
#                 url = self.task_init(id)
#
#                 # make the job
#                 # here would be selenium function
#
#                 self.task_check(id)
#
#
#     def acc_check(self, link, type=3):
#         url = 'https://api-public.bosslike.ru/v1/bots/users/me/social/auth/like/check-profile'
#         data = {'url': link, 'type': type}
#         headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
#         responce = requests.post(url, headers=headers, data=data)
#         if responce.status_code == 200:
#             print('ok')
#             return responce.json()['data']['token']
#         else:
#             print('error while checking account ' + str(responce.status_code))
#             print(responce.json())
#             return None
#
#     def show_like(self, token):
#         url = 'https://api-public.bosslike.ru/v1/bots/users/me/social/auth/like/show-like'
#         params = {'token': token}
#         headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
#         responce = requests.get(url, headers=headers, params=params)
#         if responce.status_code == 200:
#             print('ok')
#             print(responce.json()['data']['url'])
#             print(responce.json()['data']['token'])
#             return responce.json()['data']['token']
#         else:
#             print('error while getting url : ' + str(responce.status_code))
#             return None
#
#     def check_like(self, token):
#         url = 'https://api-public.bosslike.ru/v1/bots/users/me/social/auth/like/check-like'
#         params = {'token': token}
#         headers = {'Accept': 'application/json', 'X-Api-Key': self.API_KEY}
#         responce = requests.get(url, headers=headers, params=params)
#         if responce.status_code == 201:
#             print('ok')
#         else:
#             print('error while checking completed action: ' + str(responce.status_code))
#
#     def account_attach(self, nicknames):
#         urls = []
#         urls[0] = 'https://vk.com/' + nicknames[0]
#         urls[1] = 'https://instagram.com' + nicknames[1]
#         urls[2] = 'https://twitter.com' + nicknames[2]
#         type = 1
#         for url in urls:
#             token = self.acc_check(url, type=type)
#             if token is not None:
#                 token = self.show_like(token)
#             else:
#                 print('error')
#
#             if token is not None:
#                 pass
#                 #check_like(token)
#             else:
#                 print('error')
#
#             type += 2
#
#
# def create_user(email, password='password1234', referer_id = None):
#     if referer_id is None:
#         data = {'email':email, 'password':password, 'password_repeat':password}
#     else:
#         data = {'email': email, 'password': password, 'password_repeat': password, 'referer_id':referer_id}
#
#     url = 'https://api-public.bosslike.ru/v1/bots/users/create/'
#     responce = requests.post(url, data=data)
#     print(responce.status_code)
#     if responce.status_code == 201:
#         token = responce.json()['data']['token']['key']
#         print(token)
#         return token
#     else:
#         print(responce.json())
#
#
#
#
# #example 1:
# #doing the task
# #take token from accounts database
# acc1_token = 'token'
# #with token create bosslike instance
# bosslike1 = Bosslike(acc1_token)
#
# bosslike1.make_tasks()
#
#
#
#
# #example 2:
# #registering new accounts
# #returns token of new registered account
# acc2_token = create_user('email@email.com', 'password1234')
#
# bosslike2 = Bosslike(acc2_token)
#
# accs = ['https://vk.com/...'
#         'https://instagram.com/...'
#         'https://twitter.com/...']
#
# bosslike2.account_attach(accs)

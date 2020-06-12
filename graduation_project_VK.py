import requests
import time
import json

token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
url_gloups = 'https://api.vk.com/method/groups.get'
url_friends = 'https://api.vk.com/method/friends.get'
url_groups_count_people = 'https://api.vk.com/method/groups.getMembers'
url_not_user_in_group = "https://api.vk.com/method/groups.isMember"

data = []

class User():
    """Определение групп пользователя. Парсинг друзей пользователя. Поиск групп, в которых остоит только User"""

    def __init__(self, us_id):
        self.us_id = us_id

        try:
             #поиск id, если основной пользователь ввел имя пользователя
            url_id = 'https://api.vk.com/method/utils.resolveScreenName'
            params_id = {'v': 5.61,
                         'access_token': token,
                         'screen_name': us_id, }
            user_id = requests.get(url_id, params=params_id)

            us_id = user_id.json()['response']['object_id']
            self.us_id = us_id
        except:
            pass

        self.params_group = {'v': 5.61,
                             'access_token': token,
                             'user_id': us_id,
                             'extended': 1, }

        self.params_id_friends = {'v': 5.61,
                                  'access_token': token,
                                  'user_id': us_id,
                                  }

    def groups_user(self):
        # id, name группы конкретного человека записываеться в список
        time.sleep(0.5)
        group_file = requests.get(url_gloups, params=self.params_group)
        try:
            items = group_file.json()['response']['items']
            self.list_group = []
            for el in items:
                personal_group = el['id'], el['name']
                self.list_group.append(list(personal_group))
            return self.list_group
        except:
            print(f'Нет групп или ограничен доступ к vk.com/id{self.us_id}\nИдет итерация...' )

    def count_people_in_group(self, id_group):
        # Количество пользователей в группе
        for group in self.list_group:
            time.sleep(0.2)
            id_group = group[0]
            params_count_group = {'v': 5.61,
                            'access_token': token,
                            'group_id': id_group,
                             }
            try:
                group_file = requests.get(url_groups_count_people, params=params_count_group)
                group_count_people_list = group_file.json()['response']['count']
                print(f'\tvk.com/public{id_group}, с количеством пользователей {group_count_people_list}')
                return group_count_people_list
            except:
                print(group_file.json())
                print(f'\t проблемы с vk.com/public{id_group} ')

    def id_friends(self):
        # № 1 id друзей User
        friends_file = requests.get(url_friends, params=self.params_id_friends)

        id_list = friends_file.json()['response']['items']
        self.groups_user() #узнаем группы основного пользователся
        return id_list

    def groups_friends(self):
        # итерация по списку c id пользователей, с возвращением находиться ли подписчик в группе или нет

        id_list = list(self.id_friends())
        for group in self.groups_user():
            scroe_frinds_no_group = 0
            print(scroe_frinds_no_group)
            self.id_group = group[0]

            for id_user in id_list:
                time.sleep(0.5)
                params_group = {'v': 5.61,
                                'access_token': token,
                                'group_id': self.id_group,
                                'user_id': id_user, }
                res = requests.get(url_not_user_in_group, params=params_group)
                test_problem = res.json() # фильтр, если было много обращений к API
                if 'error' in test_problem:
                    time.sleep(3)
                    res = requests.get(url_not_user_in_group, params=params_group)
                    # иногда все равно выдает "Too many requests per second", поэтому 2 фильтр
                    if 'error' in res.json():
                        print('Повтор обращения к API')
                        time.sleep(5)
                        res = requests.get(url_not_user_in_group, params=params_group)
                        print(res.json())

                if [0] == list((res.json()).values()): #если пользователя нет в группе основного пользователя
                    scroe_frinds_no_group += 1
                    print(len(id_list),'/',scroe_frinds_no_group)
                    print('Search')
                    if len(id_list) == scroe_frinds_no_group:
                        print(f'В vk.com/public{self.id_group} нет никого из друзей ')
                        self.user_alone_in_group()
                elif [1] == list((res.json()).values()):
                    print(f'\t минимум 1 друг есть в vk.com/public{self.id_group}')
                    break # прекращение интерации если хотя бы 1 человек из друзей есть в группе

        with open('group.json', 'w', encoding='utf-8') as file: #сохранение файла
            json.dump(data, file, ensure_ascii=False, indent=2)

    def user_alone_in_group(self):
        # Фсохранение данных с группами, где только основной пользователь в список
        group_file = requests.get(url_gloups, params=self.params_group)
        items = group_file.json()['response']['items']

        for el in items:
            if el['id'] == self.id_group:
                count_people = self.count_people_in_group(self.id_group) # сохр. кол-во пользователей группы
                data_group = {"name": el['name'], "gid": el['id'], 'members_count': count_people}
                global data #сохранение всех данных в список
                data.append(data_group)

user1 = User('eshmargunov')

user1.groups_friends()






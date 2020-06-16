import json
import requests
import time

token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
url_gloups = 'https://api.vk.com/method/groups.get'
url_groups_count_people = 'https://api.vk.com/method/groups.getMembers'
url_friends = 'https://api.vk.com/method/friends.get'

class User():

    def __init__(self, us_id):
        self.us_id = us_id
        try:
            # поиск id, если основной пользователь ввел никнейм
            url_id = 'https://api.vk.com/method/utils.resolveScreenName'
            params_id = {'v': 5.61,
                         'access_token': token,
                         'screen_name': us_id, }
            user_id = requests.get(url_id, params=params_id)
            us_id = user_id.json()['response']['object_id']
            self.us_id = us_id
        except:
            pass

        self.params_id_friends = {'v': 5.61,
                               'access_token': token,
                               'user_id': us_id
                                  }
        self.params_group = {'v': 5.61,
                             'access_token': token,
                             'user_id': self.us_id,
                             'extended': 1, }

    def friends_user(self):

        friends_file = requests.get(url_friends, params=self.params_id_friends)
        self.id_friends =  friends_file.json()['response']['items']
        self.get_groups(self.id_friends)

    def get_groups(self, id_friends):
        #Поиск групп основго пользователя

        group_file = requests.get(url_gloups, params=self.params_group)
        items = group_file.json()['response']['items']
        self.list_group = []
        set_personal_group_user = []
        for el in items:
            personal_group = {"name": el['name'], "gid": el['id']}
            self.list_group.append(personal_group)
            set_personal_group_user.append(el['id'])
        set_personal_group_user = set(set_personal_group_user)

        #Поиск групп друзей
        scroe_frinds_no_group = 0
        list_group_friends = []
        set_group_friends = []
        for id_fr in id_friends:
            time.sleep(0.3)
            params_friends_group = {'v': 5.61,
                                 'access_token': token,
                                 'user_id': id_fr,
                                 'extended': 1,
                                 'count':1000}
            group_file = requests.get(url_gloups, params=params_friends_group)
            try:
                friends_items = group_file.json()['response']['items']
                for el in friends_items:
                    personal_group = {"name": el['name'], "gid": el['id']}
                    list_group_friends.append(personal_group)
                    set_group_friends.append(el['id'])
                scroe_frinds_no_group += 1
                print(len(id_friends), '/', scroe_frinds_no_group)
            except:
                print(f'Нет групп или ограничен доступ к vk.com/id{id_fr}')
                # print(group_file.json())
        set_group_friends = set(set_group_friends)

        data = set_personal_group_user.difference(set_group_friends)
        self.cound_user_group_and_file_save(data)

    def cound_user_group_and_file_save(self,data):
        data_group = []
        for el in self.list_group:

            if el["gid"] in data:
                print(el["gid"])
                print(el)
                params_count_group = {'v': 5.61,
                                  'access_token': token,
                                  'group_id': el["gid"],
                                  }
                time.sleep(0.3)
                group_file = requests.get(url_groups_count_people, params=params_count_group)
                group_count_people = group_file.json()['response']['count']
                print(f'\tvk.com/public{el["gid"]}, с количеством пользователей {group_count_people}')
                el['members_count'] = group_count_people
                print(el)
                data_group.append(el)
        print(data_group)
        with open('group_test.json', 'w', encoding='utf-8') as file:  # сохранение файла
            json.dump(data_group, file, ensure_ascii=False, indent=2)



user = User('171691064')
user.friends_user()


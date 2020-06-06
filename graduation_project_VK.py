import requests
import time

token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
url_gloups = 'https://api.vk.com/method/groups.get'
url_friends = 'https://api.vk.com/method/friends.get'
account_succses = 0
class User():
    """Определение групп пользователя. Парсинг друзей пользователя. Поиск групп, в которых остоит только User"""

    def __init__(self,us_id):

        self.us_id = us_id
        self.params_group = {'v': 5.61,
                       'access_token': token,
                       'user_id': us_id,
                       'extended': 1, }
        self.params_id_friends = {'v': 5.61,
                   'access_token': token,
                   'user_id': us_id,
                   }

    def groups_user(self):
        # id, name,screen_name группы конкретного человека записываеться в список
        time.sleep(1)
        group_file = requests.get(url_gloups, params=self.params_group)
        try:
            items = group_file.json()['response']['items']
            list_group = []

            for el in items:
                personal_group = el['id'], el['name'], el['screen_name']
                list_group.append(list(personal_group))

            print(len(list_group))
            global account_succses
            account_succses += 1
            return list_group
        except:
            print(f'Нет групп или ограничен доступ к vk.com/id{self.us_id}' )

    def id_friends(self):
        # id друзей User

        friends_file = requests.get(url_friends, params=self.params_id_friends)
        id_list = friends_file.json()['response']['items']
        return id_list

    def groups_friends(self):
        # итерация по списку c id пользователей, с возвращением групп каждого пользователся

        id_list = list(self.id_friends())
        for id_user in id_list:
            # print(id_user)
            self.friend = f'user{id_user}'
            self.friend = User(f'{id_user}')
            self.friend.groups_user()










user1 = User('171691064')
user1.groups_friends()
print(f'СТОЛЬКО челов ЕБАТЬ {account_succses}')
# user2 = User('552934290')
# print(user2.groups_user())



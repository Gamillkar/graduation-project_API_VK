import json
import requests
import time

url_gloups = 'https://api.vk.com/method/groups.get'
url_not_friends_in_group = "https://api.vk.com/method/groups.isMember"
url_friends = 'https://api.vk.com/method/friends.get'
url_groups_count_people = 'https://api.vk.com/method/groups.getMembers'

token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"

class User_group():

    def __init__(self, us_id):
        self.us_id = us_id
        try:
            # поиск id, если основной пользователь ввел имя пользователя
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
        """Получение всех групп пользователя"""
        group_file = requests.get(url_gloups, params=self.params_group)
        try:
            items = group_file.json()['response']['items']
            self.list_group = []
            for el in items:
                personal_group = el['id'], el['name']
                self.list_group.append(list(personal_group))
            return self.list_group
        except:
            print(f'Нет групп или ограничен доступ к vk.com/id{self.us_id}\nИдет итерация...')

    def id_friends(self):
        """Получение id друзей"""
        friends_file = requests.get(url_friends, params=self.params_id_friends)
        print(friends_file)
        id_list = friends_file.json()['response']['items']
        id_list = str(id_list)
        self.str_id_list = "".join(id_list)
        return self.str_id_list

    def user_alone_in_group(self):
        """Определение групп, где пользователь один"""
        self.id_friends()
        score = 0
        data_file = []
        for  group in self.groups_user():
            time.sleep(0.4)
            id_group = group[0]
            self.params_not_friends_in_group = {'v': 5.61,
                                                'access_token': token,
                                                'group_id': id_group,
                                                'user_ids': self.str_id_list,
                                                }
            res = requests.get(url_not_friends_in_group, params=self.params_not_friends_in_group)
            score += 1
            for friends in res.json().values():
                score_user_alone_in_group = 0
                print('...')
                for friends_data in friends:
                    if friends_data['member'] == 0:
                        score_user_alone_in_group += 1
                        if score_user_alone_in_group == len(friends):
                            account = self.cound_user_group(id_group)
                            personal_group = {"name": group[1], "gid": group[0], 'members_count': account}
                            data_file.append(personal_group)
                            print(personal_group)
                    elif friends_data['member'] != 1:
                        print(friends_data, group)
        print('End of operation. Resualt:')
        print(data_file)
        self.file_save(data_file)

    def cound_user_group(self,id_group):
        """Подсчет количество пользователей в группе"""

        params_count_group = {'v': 5.61,
                          'access_token': token,
                          'group_id': id_group,
                          }
        time.sleep(0.4)
        group_file = requests.get(url_groups_count_people, params=params_count_group)
        group_count_people = group_file.json()['response']['count']
        return group_count_people

    def file_save(self,data_file):
        """Сохранение файла в json-формате"""
        with open('group_v3.json', 'w', encoding='utf-8') as file:
            json.dump(data_file, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    user = User_group('171691064')
    user.user_alone_in_group()

import requests
token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
url_gloups = 'https://api.vk.com/method/groups.get'
url_friends = 'https://api.vk.com/method/friends.get'
list_group = []
params_group = {'v': 5.61,
                       'access_token': token,
                       'user_id': 144253,
                       'extended': 1, }
group_file = requests.get(url_gloups, params=params_group)
print(group_file.json())
items = group_file.json()['response']['items']
print(items)
for el in items:
    personal_group = el['id'], el['name'], el['screen_name']
    list_group.append(list(personal_group))
print(len(list_group))
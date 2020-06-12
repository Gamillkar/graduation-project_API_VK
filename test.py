import json
token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
url_gloups = 'https://api.vk.com/method/groups.get'
# url_friends = 'https://api.vk.com/method/friends.get'
# url_groups_count_people = 'https://api.vk.com/method/groups.getMembers'
#
# возвращает группы человека
# list_group = []
# params_group = {'v': 5.61,
#                        'access_token': token,
#                        'user_id': 171691064,
#                        'extended': 1, }
# group_file = requests.get(url_gloups, params=params_group)
#
# items = group_file.json()['response']['items']
#
# for el in items:
#
#     if el['id'] == 8564:
#         count_people = self.count_people_in_group(id_group)
#         personal_group = el['id'], el['name']
#         data_group = {"name": el['name'], "gid": el['id'], 'members_count': count_people}
#         with open('group.json', 'a', encoding='utf-8') as file:
#
#             json.dump(data_group, file, ensure_ascii=False, indent=2 )




# возвращает количество человек в сообществе

# count_people_in_group = []
# params_group = {'v': 5.61,
#                        'access_token': token,
#                        'group_id': 8564,
#                        'extended': 1, }
# group_file = requests.get(url_groups_count_people, params=params_group)
# print(group_file.json()['response']['count'])
# group_count_people_list = group_file.json()['response']['count']
# for count_people in group_count_people_list:
#     personal_group = count_people
#     list_group.append(list(personal_group))
# print(len(list_group))



# # есть ли пользователь в группе.
# url = "https://api.vk.com/method/groups.isMember"
# params_group = {'v': 5.61,
#                        'access_token': token,
#                        'group_id': 8564,
#                        'user_id': 94762191, }
# # 171691064
#
# res = requests.get(url, params=params_group)
#
# print(list((res.json()).values()) == 0)





# a = {1: 'D', 2: 'B', 5: 'A', 3: 'B', 4: 'E'}
# print(sorted({1: 'D', 2: 'B', 5: 'A', 3: 'B', 4: 'E'}))
# print(sorted("This is a test string from Andrew".split(), key=str.lower))

# class Student:
#         def __init__(self, name, grade, age):
#             self.name = name
#             self.grade = grade
#             self.age = age
#         def __repr__(self):
#             return repr((self.name, self.grade, self.age))
#         def weighted_grade(self):
#             return 'CBA'.index(self.grade) / self.age
#
# student_objects = [
#         Student('john', 'A', 15),
#         Student('jane', 'B', 12),
#         Student('dave', 'B', 10),
#     ]
# print(sorted(student_objects, key=lambda student: student.age))



# s = 'ab'
# t = (20,10 , 30)
#
# print(sorted((s,t), key=len))
#
#
# import os
#
# print(os.getcwd())

#
# def a(name):
#     if name == str:
#         url_gloupsss = 'https://api.vk.com/method/utils.resolveScreenName'
#         params_group = {'v': 5.61,
#                                'access_token': token,
#                                'screen_name': name, }
#         group_file = requests.get(url_gloupsss, params=params_group)
#         print(group_file.json()['response']['object_id'])
#     else:
#         print('hehe')
# a(214124)



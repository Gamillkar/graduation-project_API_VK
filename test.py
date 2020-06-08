# import requests
# token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
# url_gloups = 'https://api.vk.com/method/groups.get'
# url_friends = 'https://api.vk.com/method/friends.get'
# url_groups_count_people = 'https://api.vk.com/method/groups.getMembers'
#
# # возвращает группы человека
# list_group = []
# params_group = {'v': 5.61,
#                        'access_token': token,
#                        'user_id': 171691064,
#                        'extended': 1, }
# group_file = requests.get(url_gloups, params=params_group)
# # print(group_file.json())
# items = group_file.json()['response']['items']
# # print(items)
# for el in items:
#     personal_group = el['id'], el['name']
#     list_group.append(list(personal_group))
# print(len(list_group))
# print(list_group)


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







#
# a = {1: 'D', 2: 'B', 5: 'A', 3: 'B', 4: 'E'}
# print(sorted({1: 'D', 2: 'B', 5: 'A', 3: 'B', 4: 'E'}))
# print(sorted("This is a test string from Andrew".split(), key=str.lower))

class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age
        def __repr__(self):
            return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
            return 'CBA'.index(self.grade) / self.age

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]
print(sorted(student_objects, key=lambda student: student.age))
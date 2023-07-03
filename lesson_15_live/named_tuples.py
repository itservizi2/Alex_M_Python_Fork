from collections import namedtuple

#
# user_tuple = tuple(['marius_tuple','30011998', 'marius@gmail.com'])
#
#
# print(user_tuple[0], user_tuple[1], user_tuple[2])

User = namedtuple('User', ['username', 'dateofbirth', 'email'])

marius_user = User(username="marius", dateofbirth='30011998', email='marius@gmail.com')

print(marius_user[0], marius_user[1], marius_user[2])

print(marius_user.username, marius_user.dateofbirth, marius_user.email)

# marius_user.username = 'ion'

marius_list = list(marius_user)
marius_list.pop(0)

marius_user = User(*marius_list)

print(marius_user)

user_dict = {
    "username": 'Marius',
    "dateofbirth": '30011998',
    "email": '@gmail.com',
}

print(user_dict['username'], user_dict['email'])

users = [
    dict(
        username='mt',
        deleted=False
    ), dict(
        username='anton',
        deleted=False
    ), dict(
        username='ion',
        deleted=False
    )
]

users_copy = users.copy()
users_copy.append(dict(un='new-user', delted=False))


def delete_user(user: dict):
    user = user.copy()
    user['deleted'] = True
    return user


marius = users_copy[0]
new_marius = delete_user(marius)
users_copy[0] = new_marius
print(marius)
print(users)
print(users_copy)

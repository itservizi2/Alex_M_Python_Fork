all_list_elements = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']


# for el in all_list_elements:
#    if el == el[::-1]:
#       print(f"Cuvintele palindrome sunt {el}")

def palindrom():
    return [el for el in all_list_elements if el == el[::-1]]


print(palindrom())

my_dict = dict()

also_my_dict = my_dict

print(also_my_dict, my_dict)

also_my_dict['Ion'] = [1, 2, 3]

print(also_my_dict, my_dict)

for key in also_my_dict:
    print("Key", key)
    print("Value", also_my_dict[key])
    also_my_dict['Ion'] = 123

for key in also_my_dict:
    print("Key", key)
    print("Value", also_my_dict[key])
    also_my_dict['Ion'] = 123

all_current_keys = list(also_my_dict)
# Extragem cheile
print("All keys", all_current_keys)

for key in all_current_keys:
    also_my_dict['NewKey'] = 1

print(also_my_dict)

values = [also_my_dict[key] for key in also_my_dict]
print(values)

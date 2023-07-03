import os

print(os.cpu_count())

print(os.getcwd())

print(os.listdir(os.getcwd()))

path_to_calned = os.path.join(os.getcwd(), 'calend.py')
print(path_to_calned)
new_path_to_calned = os.path.join(os.getcwd(), 'calend.py')

os.rename(path_to_calned, new_path_to_calned)

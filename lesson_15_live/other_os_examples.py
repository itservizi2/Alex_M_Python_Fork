import os
import platform

print(os.getcwd())
path_to_example_folder = os.path.join(os.getcwd(), 'example')
print(os.listdir(path_to_example_folder))

filename = input('filename to create: ')

path_to_new_file = os.path.join(path_to_example_folder, filename)
open(path_to_new_file, 'w')

for filename in os.listdir(path_to_example_folder):
    file_to_remoev = os.path.join(path_to_example_folder, filename)
    print(file_to_remoev)
    os.remove(file_to_remoev)

os.rmdir(path_to_example_folder)



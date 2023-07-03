import shutil
import os.path

folder_to_backup = input('Path to folder to backup')
backup_destination_folder = input("Backup Dest folder:")

shutil.copy(os.path.join(folder_to_backup), os.path.join(backup_destination_folder))

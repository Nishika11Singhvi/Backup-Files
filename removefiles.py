import os
import shutil
import time

def main():

	deletedFoldersCount = 0
	deletedFilesCount = 0
	path = "/delete"
	days = 30
	seconds = time.time() - (days*24*60*60)

	if os.path.exists(path):

		for rootfolder, folders, files in os.walk(path):

			if seconds >= get_file_or_folder_age(rootfolder):

				remove_folder(rootfolder)
				deletedFoldersCount += 1 
				break

			else:

				for folder in folders:

					folderPath = os.path.join(rootfolder, folder)

					if seconds >= get_file_or_folder_age(folderPath):

						remove_folder(folderPath)
						deletedFoldersCount += 1 

				for file in files:

					filePath = os.path.join(rootfolder, file)

					if seconds >= get_file_or_folder_age(filePath):

						remove_file(filePath)
						deletedFilesCount += 1 

		else:

			if seconds >= get_file_or_folder_age(path):

				remove_file(path)
				deletedFilesCount += 1 

	else:

		print(f'"{path}" is not found')
		deletedFilesCount += 1 

	print(f"Total folders deleted: {deletedFoldersCount}")
	print(f"Total files deleted: {deletedFilesCount}")


def remove_folder(path):

	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		print(f"Unable to delete the " + path)



def remove_file(path):

	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the " + path)


def get_file_or_folder_age(path):

	ctime = os.stat(path).st_ctime

	return ctime


if __name__ == '__main__':
	main()

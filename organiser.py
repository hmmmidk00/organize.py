import os
import shutil
#os.listdir()--> list all files on that directory
for item in os.listdir():
	#get the name and the extension of a file
	filename, file_extension = os.path.splitext(item)
	if file_extension==".pdf":
		#move item to pdf directory
		shutil.move(f"C:/Users/root/Downloads/{item}", f"C:/Users/root/Downloads/pdf/{item}")
	if file_extension==".mp4":
		#move item to mp4 directory
		shutil.move(f"C:/Users/root/Downloads/{item}", f"C:/Users/root/Downloads/mp4/{item}")
	if file_extension==".exe":
		shutil.move(f"C:/Users/root/Downloads/{item}", f"C:/Users/root/Downloads/exe/{item}")
	if file_extension==".txt":
		shutil.move(f"C:/Users/root/Downloads/{item}", f"C:/Users/root/Downloads/txt/{item}")
	if file_extension==".iso" or file_extension=="ISO" :
		shutil.move(f"C:/Users/root/Downloads/{item}", f"C:/Users/root/Downloads/iso/{item}")



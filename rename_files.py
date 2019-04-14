import os

#to remove numbers from filename
def rename_files():
    #get file names from folder
    file_list=os.listdir(r"C:\Users\Lin-Desktop\AppData\Local\Programs\Python\Python37\Udacity\changing filenames\prank")
    #print(file_list)
    #save current directory
    saved_path = os.getcwd()
    #change directory to prank folder
    os.chdir(r"C:\Users\Lin-Desktop\AppData\Local\Programs\Python\Python37\Udacity\changing filenames\prank")
    
    #change name of files
    for name in file_list:
        print("Old Name- " +name)
        print("New Name- " +name.translate(name.maketrans('','',"0123456789")))
        os.rename(name, name.translate(name.maketrans('','',"0123456789")))
        
    #change directory back
    os.chdir(saved_path)

rename_files()

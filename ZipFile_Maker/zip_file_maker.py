import zipfile as zf
import os, shutil

#dst is where your zip file will be saved, so change to where you want ur zipfile to be saved
dst = os.path.join("C:/", "Users","Dimitriy Kruglikov","Desktop","Python","ZipFile_Maker","ZipFiles")
os.chdir(dst)
files_to_zip = ["Tori Black", "Alexis Texas"]

def makeZips(file_name):
    file_name = file_name + ".zip" # make this an arg later
    zip_archive = zf.ZipFile(file_name, "a")

    for item in files_to_zip:
        full_name = item + ".txt" # full file name
        makeFile = open(full_name, "a") # w+ creates the files
        makeFile.write("test")
        makeFile.close()
        zip_archive.write(full_name)
        os.remove(full_name)
    zip_archive.close()

makeZips("gay")
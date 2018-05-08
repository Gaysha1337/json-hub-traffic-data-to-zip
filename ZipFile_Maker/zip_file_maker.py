import zipfile as zf
import os, shutil, glob
import get_json_data as gjd

dirname = os.path.dirname(__file__)
json_file_dir = os.path.join(dirname, "JSON files")
files_to_zip = []

#files_to_zip = ["Tori Black", "Alexis Texas"]

def getFileNamesAndPaths():
    """
    Get all the txt files in JSON files dir
    """
    os.chdir(json_file_dir)
    files_in_JSON_dir = os.listdir(json_file_dir)
    for file in glob.glob("*.txt"):
        files_to_zip.append(file)

def makeZips(file_name):
    """
    make zip file based on paramter file_name
    """

    if not ".zip" in file_name:
        file_name = file_name + ".zip"
        
    os.chdir(json_file_dir)
    zip_archive = zf.ZipFile(file_name, "a")

    for item in files_to_zip:
        full_name = item # full file name
        makeFile = open(full_name, "a") # w+ creates the files
        makeFile.write("test")
        makeFile.close()
        zip_archive.write(full_name)
        os.remove(full_name) #remove if want these files to stay in this folder(JSON file)
    zip_archive.close()

if __name__ == "__main__":
    url = "" #url needs to have JSON data to requested
    filename = "JSON_data.txt" # filename is where your JSON data will be saved to
    zipfile_name = "zipped_files" # the name of the zipfile where are your files will be zipped to
    gjd.makeRequestAndGetJSON(url, filename) 
    getFileNamesAndPaths() # Gets all txt files from JSON dir
    makeZips(zipfile_name) # you can .zip if you want, it is optional


import requests, json, os, shutil

dirname = os.path.dirname(__file__)
src = os.getcwd()
dst = os.path.join(dirname, "JSON files")

def makeRequestAndGetJSON(url, filename="JSON.txt"):
    """
    url is the request url, needs to be able to get json data\n
    filename is the file where the json data will be stored
    """
    os.chdir(dst)
    r = requests.get(url).json()
    with open(filename, "w") as f:
        json.dump(r,f,indent=4)
    os.chdir(src)
    return r


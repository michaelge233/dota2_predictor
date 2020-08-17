import dota2api
import urllib.request
import os.path
import json


fo=open("steam_api_key.txt","r")
steam_api_key=fo.read()
fo.close()

fo=open("id_name.json","r")
id_name_dic=json.loads(fo.read())
fo.close()

api = dota2api.Initialise(steam_api_key)
heroes=api.get_heroes()["heroes"]
print("Downloading...")
i=0
for hero in heroes:
    file_name=str(hero["id"])+" "+hero["localized_name"]+".png"
    try:

        if not os.path.isfile(".\\hero_images\\"+file_name):
            req = urllib.request.Request(hero["url_small_portrait"])
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')
            response = urllib.request.urlopen(req,timeout=5)
            fo=open(".\\hero_images\\"+file_name,"wb")
            fo.write(response.read())
            fo.close()
            i=i+1
    except:
        print(file_name+" fail")

print(i,"images were downloaded")
print("You can run this scripe again if any images download failed")
input("Press ENTER to exit")

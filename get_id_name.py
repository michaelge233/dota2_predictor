import dota2api
import json

fo=open("steam_api_key.txt","r")
steam_api_key=fo.read()
fo.close()

api = dota2api.Initialise(steam_api_key)
print("Downloading...")
hero_dict = api.get_heroes()
heroes = hero_dict['heroes']
hero_id={}
for i in heroes:
    hero_id[i["id"]]=i["localized_name"]

fo=open("id_name.json","w")
fo.write(json.dumps(hero_id))
fo.close()
print("Finished")
input("Press ENTER to exit")

import dota2api
import json

api = dota2api.Initialise("317D0CD131B4DB6D6A6CE5F1843DEB5A")
hero_dict = api.get_heroes()
heroes = hero_dict['heroes']
hero_id={}
for i in heroes:
    hero_id[i["id"]]=i["localized_name"]

fo=open("id_name.json","w")
fo.write(json.dumps(hero_id))
fo.close()
print(hero_id)


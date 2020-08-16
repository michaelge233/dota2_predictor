import dota2api
import json
import numpy as np
import csv

fo=open("steam_api_key.txt","r")
steam_api_key=fo.read()
fo.close()

fo=open("our_ids.txt","r")
we_list=fo.readlines()
fo.close()
for i in range(0,len(we_list)):
   we_list[i]=int(we_list[i])

fo=open("id_name.json","r")
id_name_dic=json.loads(fo.read())
fo.close()
hero_num=0
for i in id_name_dic:
   if(int(i)>hero_num):
       hero_num=int(i)

api = dota2api.Initialise(steam_api_key)

match_id_list=[]
fm=open("matches.json","r")
already_id_list=json.loads(fm.read())
fm.close()

search_match_num=input("How many matches per person?\n")

for we in we_list:
   hist = api.get_match_history(account_id=we,matches_requested=search_match_num)

   for match in hist["matches"]:
      if not (match["match_id"] in match_id_list or match["match_id"] in already_id_list):
         match_id_list.append(match["match_id"])

print("Totally",len(match_id_list),"matches have not downloaded")

fo=open("X.csv","a",newline='')
writer=csv.writer(fo)
effect_num=0
for match_id in match_id_list:
    match=api.get_match_details(match_id=match_id)
    if not match["game_mode"] in (1,2,22):
        continue
    
    is_radiant=True
    for player in match["players"]:
        if player["account_id"] in we_list:
            if player["player_slot"]<5:
                is_radiant=True
                break
            else:
                is_radiant=False
                break

    is_win=False
    if is_radiant:
        is_win=match["radiant_win"]
    else:
        is_win= not match["radiant_win"]

    our_side=[]
    other_side=[]
    if is_radiant:
        for player in match["players"]:
            if player["player_slot"]<5:
                our_side.append(player["hero_id"])
            else:
                other_side.append(player["hero_id"])
    else:
        for player in match["players"]:
            if player["player_slot"]<5:
                other_side.append(player["hero_id"])
            else:
                our_side.append(player["hero_id"])
                
    row=our_side+other_side
    row.append(int(is_win))
    writer.writerow(row)
    already_id_list.append(match_id)
    effect_num=effect_num+1
    if effect_num%10==0:
        print(effect_num,"matches already")

fm=open("matches.json","w")
fm.write(json.dumps(already_id_list))
fm.close()
fo.close()
print("Totally",effect_num,"effective matches were added to the dataset")
input("Press ENTER to exit")    

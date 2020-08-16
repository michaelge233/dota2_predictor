import dota2api
import json
import numpy as np
import csv

fo=open("id.json","r")
id_dic=json.loads(fo.read())
fo.close()

fo=open("id_name.json","r")
id_name_dic=json.loads(fo.read())
fo.close()
hero_num=0
for i in id_name_dic:
   if(int(i)>hero_num):
       hero_num=int(i)

api = dota2api.Initialise(id_dic["apikey"])

match_id_list=[]
fm=open("matches.json","r")
already_id_list=json.loads(fm.read())
fm.close()


we_list=["cccpccc","prince","wzh","wjl","ljy","wzp"]
we_id_list=[]
for we in we_list:
   we_id_list.append(id_dic[we])
   hist = api.get_match_history(account_id=id_dic[we],matches_requested=10)

   for match in hist["matches"]:
      if not (match["match_id"] in match_id_list or match["match_id"] in already_id_list):
         match_id_list.append(match["match_id"])

print("共",len(match_id_list),"场待查")

fo=open("X.csv","a",newline='')
writer=csv.writer(fo)
effect_num=0
for match_id in match_id_list:
    match=api.get_match_details(match_id=match_id)
    if not match["game_mode"] in (1,2,22):
        continue
    
    is_radiant=True
    for player in match["players"]:
        if player["account_id"] in we_id_list:
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
        print("已添加",effect_num,"场")

fm=open("matches.json","w")
fm.write(json.dumps(already_id_list))
fm.close()
fo.close()
print("共添加",effect_num,"场")
input()    

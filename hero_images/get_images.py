import dota2api
import urllib.request

#获取英雄图片的脚本

api = dota2api.Initialise("317D0CD131B4DB6D6A6CE5F1843DEB5A")
heroes=api.get_heroes()["heroes"]
for hero in heroes:
    try:
        #可以修改该判断条件以部分爬取
        if(hero["id"]>0):
            req = urllib.request.Request(hero["url_small_portrait"])
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')
            response = urllib.request.urlopen(req,timeout=5)
            file_name=str(hero["id"])+" "+hero["localized_name"]+".png"
            fo=open(file_name,"wb")
            fo.write(response.read())
            fo.close()
    except:
        print(str(hero["id"])+" "+hero["localized_name"]+" "+"fail")

from django.shortcuts import render,redirect
from django.urls import reverse
import requests
import json ,random
# Set variable
ScoreList = [["pong",7,"1eQTM2gSBc9ARw1Pst4V72"],["mata",8,"1eQTM2gSBc9ARw1Pst4V72"],["time",6,"1eQTM2gSBc9ARw1Pst4V72"],["nut",10,"1eQTM2gSBc9ARw1Pst4V72"]]
# Create your views here.
def index(request):
    return render(request,'games/index.html')

def play(request):
    
    playList = request.POST['playList']    
    if (playList == ""):
        playList = "1eQTM2gSBc9ARw1Pst4V72"
    listMusic,listNameMusic = getPlayList(playList)
    for i in range(len(listMusic)):
        randomList = listNameMusic.copy()
        random.shuffle(randomList)
        randomList.remove(listMusic[i]["nameMusic"])
        listMusic[i]["choice"] = [listMusic[i]["nameMusic"],randomList[0],randomList[1]]
        random.shuffle(listMusic[i]["choice"])
    return render(request,'games/play.html',{"listMusic":listMusic,"numberMusic":len(listMusic),"playlist": playList })

def score(request):
    if request.method == 'POST':
        name = request.POST['name']
        score = request.POST['score']
        playlist = request.POST['playlist']
        ScoreList.append([name,int(score),playlist])
    listcopy = sorted(ScoreList,key=lambda x: x[1],reverse=True)
    
    return render(request,'games/score.html',{'ScoreList':listcopy})
#function use in view

def getToken():
    auth_response = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type': 'client_credentials',
    'client_id': "ea9aa69cb3e14c3ca66c44370e1fa016",
    'client_secret': "ae4273c117f2437e82ff8e2dad346742",
    })

    # save the access token
    access_token = auth_response.json()['access_token']
    return access_token 

def getAlbum(SID):
    access_token = getToken()
    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    BASE_URL = 'https://api.spotify.com/v1/'
    OPTION_URL ='albums/'
    # actual GET request with proper header
    r = requests.get(BASE_URL + OPTION_URL + SID , headers=headers)
    r = r.json()
    print(r)
    return r

def getPlayList(SID):
    access_token = getToken()
    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    BASE_URL = 'https://api.spotify.com/v1/'
    OPTION_URL ='playlists/'
    # actual GET request with proper header
    r = requests.get(BASE_URL + OPTION_URL + SID , headers=headers)

    listNameMusic = [] 
    json_data = []
    temp = r.json()["tracks"]["items"]
    random.shuffle(temp)
    for i in range(len(r.json()["tracks"]["items"])):
        json_data.append({  "preview_url" : temp[i]["track"]["preview_url"],
                            "nameMusic":  temp[i]["track"]["name"] ,
                            "img" : temp[i]["track"]["album"]["images"][0]["url"],
                            "index":i+1
                            })
        listNameMusic.append(temp[i]["track"]["name"])
    return json_data, listNameMusic


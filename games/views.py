from django.shortcuts import render,redirect
from django.urls import reverse
import requests
import json ,random

# Create your views here.
def index(request):
    return render(request,'games/index.html')

def play(request):
    listMusic,listNameMusic = getPlayList("1eQTM2gSBc9ARw1Pst4V72")
    for i in range(len(listMusic)):
        randomList = listNameMusic.copy()
        random.shuffle(randomList)
        randomList.remove(listMusic[i]["nameMusic"])
        listMusic[i]["choice"] = [listMusic[i]["nameMusic"],randomList[0],randomList[1]]
        random.shuffle(listMusic[i]["choice"])
    return render(request,'games/play.html',{"listMusic":listMusic,"numberMusic":len(listMusic)})

def score(request):
    return render(request,'games/score.html')
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
    for i in range(len(r.json()["tracks"]["items"])):
        json_data.append({  "preview_url" : r.json()["tracks"]["items"][i]["track"]["preview_url"],
                            "nameMusic":  r.json()["tracks"]["items"][i]["track"]["name"] ,
                            "img" : r.json()["tracks"]["items"][i]["track"]["album"]["images"][0]["url"],
                            "index":i+1
                            })
        listNameMusic.append(r.json()["tracks"]["items"][i]["track"]["name"])

    return json_data, listNameMusic


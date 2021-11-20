from django.shortcuts import render,redirect
from django.urls import reverse
import requests
import json

# Create your views here.
def index(request):
    getPlayList("1eQTM2gSBc9ARw1Pst4V72")
    return render(request,'games/index.html',)

def play(request):
    return render(request,'games/play.html')

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
    json_data = r.json()
    #json_data = json.dumps(r, indent=1)
    print(json_data['tracks']['items'])
    return json_data #json_data

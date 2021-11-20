import requests
# POST
auth_response = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type': 'client_credentials',
    'client_id': "ea9aa69cb3e14c3ca66c44370e1fa016",
    'client_secret': "ae4273c117f2437e82ff8e2dad346742",
})

# save the access token
access_token = auth_response.json()['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '6y0igZArWVi6Iz0rj35c1Y'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()
print(r)
print(r["uri"])


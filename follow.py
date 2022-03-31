import requests
import json

channel = input("Channel: ").strip()
headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': 'g5zg0400k4vhrx2g6xi4hgveruamlv',
}
r = requests.get(f'https://api.twitch.tv/kraken/users?login={channel}', headers=headers)
zero = json.loads(r.text)

if (zero['_total']) == 1:
    channel_id = (zero['users'][0]['_id'])
elif (zero['_total']) == 0:
    print(f"{channel} not found")



arquivo = open(input("Accounts Text file: ").strip())
conta = arquivo.read().splitlines()
for c in conta:
        acc = c.split(":")
        nick = acc[3]
        oauth = acc[1]
        user_id = acc[5]
        url = f'https://api.twitch.tv/kraken/users/{user_id}/follows/channels/{channel_id}'
        payload = {}
        headers = {
                'Accept': 'application/vnd.twitchtv.v5+json',
                'Client-ID': 'g5zg0400k4vhrx2g6xi4hgveruamlv',
                'Authorization': f'OAuth {oauth}',
                }
        r = requests.put(url,headers=headers, data=payload)
        if r.status_code == 401:
                print ("Error Token Invalid")
        elif r.status_code == 200:
                print (f"{nick} has followed") 
        
                
arquivo.close()
      

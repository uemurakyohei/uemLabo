import requests
import json

# from plotly.graph_objs import Scattergeo,Layout
# from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

r = requests.get(url)

print(f"ステータスコード: {r.status_code}")


response_dict = r.json()
readable_file = 'data/readble_hn_data.json'

with open(readable_file,'w') as f:
	json.dump(response_dict,f,indent=4)
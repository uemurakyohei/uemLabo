from operator import itemgetter

import requests


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)

print(f"ステータスコード: {r.status_code}")


submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
	url = f"https://hacker-news.firebaseio.com/v0/itm/{submission_id}.json"
	r = requests.get(url)
	print(f"id:{submission_id}\tstatus:{r.status_code}")
	response_dict = r.json()

	submission_dict = {
		'title':response_dict['title'],
		'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
		'comments':response_dict['descendants']
	}

	submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse=True)



with open(readable_file,'w') as f:
	json.dump(submission_ids,f,indent=4)


for submission_dict in submission_dicts:
	print(f"\nタイトル:{submission_dict['title']}")	
	print(f"\nリンク:{submission_dict['hn_link']}")	
	print(f"\nコメント数:{submission_dict['comments']}")	

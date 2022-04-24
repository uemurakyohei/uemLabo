import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=starsPyGithub/PyGithub'

headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)

print(f"ステータスコード:{r.status_code}")

response_dict = r.json()
print(f"全リポジトリ数:{response_dict['total_count']}")


repo_dicts = response_dict['items']

print(f"情報が返されたリポジトリ数:{len(repo_dicts)}")



repo_dicts = repo_dicts[0]
# print(f"\nキーの数:{len(repo_dicts)}")

# for key in sorted(repo_dicts.keys()):
# 	print(key)


print(repo_dicts['created_at'],repo_dicts['updated_at'])

# for key in sorted(repo_dicts.items()):
# 	print(key)

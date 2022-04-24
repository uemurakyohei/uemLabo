import requests

from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:python&sort=starsPyGithub/PyGithub'

headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)


response_dict = r.json()


repo_dicts = response_dict['items']
repo_links,stars,labels = [],[],[]

for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	stars.append(repo_dict['stargazers_count'])


data = [{
	'type' : 'bar',
	'x' : repo_links,
	'y' : stars,
}]


my_layout = {
	'title' : 'GitHubで最も多くのスターがついているPythonプロジェクト',
	'xaxis' : {'title' : 'リポジトリ'},
	'yaxis' : {'title' : 'スターの数'},
}

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')


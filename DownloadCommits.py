import json
import os
import requests
GithubToken = os.environ.get('GITHUB_TOKEN')
if GithubToken is None:
    raise ValueError("The environment variable GITHUB_TOKEN is not set.")
headers = {'Authorization': f'token {GithubToken}'}
history=[]
flag=1
i=0
url = "https://api.github.com/repos/langchain-ai/langchain/commits"
while flag :
    params = {'per_page': '100',
              'page': {i}}
    response = requests.get(url,verify = False,headers=headers,params = params)
    if response.status_code == 200:
        commits = response.json()
        if len(commits) == 0:
            break
        history.extend(commits)
        print(f'page {i} finished')
        i = i + 1
    else:
        flag=0
        print(f"Failed to retrieve commits: {response.text}")
with open(f'./commits','w',encoding = 'utf-8')as file:
    json.dump(history,file, ensure_ascii=False, indent=4)
import json
import os
import requests
# from dotenv import find_dotenv,load_dotenv

# load_dotenv(dotenv_path=r".vscode\.env", verbose=True) #从.env文件中获取运行时环境变量(vscode)
# 从环境变量中获取 GitHub Token
GithubToken = os.environ.get('GITHUB_TOKEN')
if GithubToken is None:
    raise ValueError(
        "环境变量 GITHUB_TOKEN 未设置。\n"
        "请按照以下步骤设置：\n"
        "1.在github Settings->Developer settings->Personal access tokens中获取你的GITHUB_TOKEN：\n"
        "2. 在终端中运行:export GITHUB_TOKEN=你的GitHub Token(Linux/macOS)\n"
        "或 set GITHUB_TOKEN=你的GitHub Token(Windows)。\n"
        "3. 确保在运行脚本之前设置环境变量。\n"
        "4.如您需临时使用，也可直接对GithubToken赋值"
    )

# 设置请求头，用于 GitHub API 的身份验证
headers = {'Authorization': f'token {GithubToken}'}

# 初始化变量
history = []  # 用于存储所有获取到的提交记录
flag = 1      # 控制循环的标志，初始值为 1
i = 0         # 当前页码，初始值为 0
url = "https://api.github.com/repos/langchain-ai/langchain/commits"  # GitHub API 的提交记录接口

# 分页获取提交记录
while flag:
    # 设置请求参数：每页 100 条记录，当前页码为 i
    params = {'per_page': '100', 'page': i}  # 修正：{i} 改为 i
    # 发送 GET 请求，获取提交记录
    response = requests.get(url, verify=False, headers=headers, params=params)
    
    # 如果请求成功（状态码为 200）
    if response.status_code == 200:
        # 解析返回的 JSON 数据
        commits = response.json()
        
        # 如果当前页没有提交记录，说明已经获取完所有记录，退出循环
        if len(commits) == 0:
            break
        
        # 将当前页的提交记录添加到 history 列表中
        history.extend(commits)
        print(f'page {i} finished')  # 打印当前页完成的信息
        i = i + 1  # 翻到下一页
    else:
        # 如果请求失败，设置 flag 为 0 以退出循环，并打印错误信息
        flag = 0
        print(f"Failed to retrieve commits: {response.text}")

# 将提交记录保存到 JSON 文件
with open(f'./commits.json', 'w', encoding='utf-8') as file:
    # 使用 json.dump 将 history 列表写入文件
    json.dump(history, file, ensure_ascii=False, indent=4)

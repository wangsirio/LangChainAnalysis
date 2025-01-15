import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

chinese_fonts = ['SimHei']
font_found = False
for font_name in chinese_fonts:
    try:
        plt.rcParams['font.sans-serif'] = [font_name]
        fm.findfont(font_name)
        font_found = True
        break
    except:
        continue


plt.rcParams['axes.unicode_minus'] = False

def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(e)

file_path = './commits'
json_data = read_json_file(file_path)

if json_data is not None:
    author_dict = {}
    commit_date_dict = {}

    for dic in json_data:
        author_name = dic['commit']['author']['name']
        commit_date_str = dic['commit']['author']['date']

        if author_name in author_dict:
            author_dict[author_name] += 1
        else:
            author_dict[author_name] = 1

        dt = datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ")
        commit_date = dt.date()

        if commit_date in commit_date_dict:
            commit_date_dict[commit_date] += 1
        else:
            commit_date_dict[commit_date] = 1

    sorted_authors = sorted(author_dict.items(), key=lambda x: x[1], reverse=True)
    commits_by_author = [item[1] for item in sorted_authors]
    authors = [item[0] for item in sorted_authors]

    total_commits = sum(commits_by_author)
    commits_percentage = [commit/total_commits * 100 for commit in commits_by_author]
    
    fig1, ax1 = plt.subplots(figsize=(20, 6))
    ax1.bar(range(len(commits_percentage)), commits_percentage, color='skyblue', edgecolor='black', linewidth=0.5)

    total_authors = len(authors)
    if total_authors > 20:
        step = (total_authors - 1) / 19
        tick_positions = [int(i * step) for i in range(20)]
        ax1.set_xticks(tick_positions)
        ax1.set_xticklabels([authors[i] for i in tick_positions], rotation=45, ha='right')
    else:
        ax1.set_xticks(range(total_authors))
        ax1.set_xticklabels(authors, rotation=45, ha='right')

    ax1.set_title(f'所有作者提交次数占比统计（共{total_authors}位作者）')
    ax1.set_xlabel('作者')
    ax1.set_ylabel('提交次数占比(%)')
    
    plt.tight_layout()
    fig1.savefig('commits_by_author.png', dpi=300, bbox_inches='tight')

    dates = list(commit_date_dict.keys())
    commits_by_date = list(commit_date_dict.values())

    start_date = min(dates)
    end_date = max(dates)
    from datetime import timedelta
    all_dates = []
    current_date = start_date
    while current_date <= end_date:
        all_dates.append(current_date)
        current_date += timedelta(days=1)

    complete_commits = [commit_date_dict.get(date, 0) for date in all_dates]

    total_days = len(all_dates)
    
    fig2, ax2 = plt.subplots(figsize=(20, 6))
    ax2.plot(all_dates, complete_commits, marker='', linestyle='-', color='black', linewidth=0.5)
    ax2.set_title(f'提交次数按日期统计（{start_date.strftime("%Y-%m-%d")}至{end_date.strftime("%Y-%m-%d")}，共{total_days}天）')
    ax2.set_xlabel('日期')
    ax2.set_ylabel('提交次数')
    ax2.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    fig2.savefig('commits_by_date.png', dpi=300, bbox_inches='tight')
    plt.show()
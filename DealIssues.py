import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 设置 matplotlib 的字体和负号显示，以支持中文和负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 读取 JSON 文件的函数
def read_json_file(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(e)


# 指定 Issues 数据文件路径
file_path = './issues.json'
# 读取 JSON 文件
json_data = read_json_file(file_path)


# 如果成功读取 JSON 数据
if json_data is not None:
    daily_open_issues = {}
    daily_new_issues = {}

    # 遍历 JSON 数据中的 Issue 记录
    for issue in json_data:
        created_date = datetime.strptime(issue['created_at'], "%Y-%m-%dT%H:%M:%SZ").date()
        closed_date = None
        if issue['closed_at']:
            closed_date = datetime.strptime(issue['closed_at'], "%Y-%m-%dT%H:%M:%SZ").date()
        if created_date in daily_new_issues:
            daily_new_issues[created_date] += 1
        else:
            daily_new_issues[created_date] = 1

    # 获取所有 Issue 创建日期并排序
    all_dates = sorted(daily_new_issues.keys())
    start_date = min(all_dates)
    end_date = max(all_dates)

    # 生成从起始日期到结束日期的所有日期列表
    current_date = start_date
    date_list = []
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    open_count = 0
    for date in date_list:
        if date in daily_new_issues:
            open_count += daily_new_issues[date]
        for issue in json_data:
            if issue['closed_at']:
                closed_date = datetime.strptime(issue['closed_at'], "%Y-%m-%dT%H:%M:%SZ").date()
                if closed_date == date:
                    open_count -= 1
        daily_open_issues[date] = open_count
    fig1, ax1 = plt.subplots(figsize=(20, 6))
    ax1.plot(date_list, [daily_open_issues[date] for date in date_list], 
             color='blue', linewidth=1)
    ax1.set_title(f'每日处于Open状态的Issue数量统计（{start_date}至{end_date}，共{len(date_list)}天）')
    ax1.set_xlabel('日期')
    ax1.set_ylabel('Open状态的Issue数量')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    fig1.savefig('daily_open_issues.png', dpi=300, bbox_inches='tight')

    fig2, ax2 = plt.subplots(figsize=(20, 6))
    new_issues_count = [daily_new_issues.get(date, 0) for date in date_list]
    ax2.plot(date_list, new_issues_count, color='green', linewidth=1)
    ax2.set_title(f'每日新创建的Issue数量统计（{start_date}至{end_date}，共{len(date_list)}天）')
    ax2.set_xlabel('日期')
    ax2.set_ylabel('新创建的Issue数量')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    fig2.savefig('daily_new_issues.png', dpi=300, bbox_inches='tight')

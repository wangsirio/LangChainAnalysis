import json
from datetime import datetime
import matplotlib.pyplot as plt

# 设置 matplotlib 的字体为 SimHei（黑体），以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 定义一个函数，用于读取 JSON 文件
def read_json_file(file_path):
    try:
        # 打开文件并读取内容
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        # 如果读取失败，打印错误信息
        print(e)

# 指定 JSON 文件的路径
file_path = './commits.json'
# 调用函数读取 JSON 文件
json_data = read_json_file(file_path)

# 如果成功读取到数据
if json_data is not None:
    # 初始化两个字典，用于存储作者提交次数和提交日期统计
    author_dict = {}  # 作者提交次数统计
    commit_date_dict = {}  # 提交日期统计

    # 遍历 JSON 数据中的每个提交记录
    for dic in json_data:
        # 获取作者名字
        author_name = dic['commit']['author']['name']
        # 获取提交日期字符串
        commit_date_str = dic['commit']['author']['date']

        # 统计每个作者的提交次数
        if author_name in author_dict:
            author_dict[author_name] += 1
        else:
            author_dict[author_name] = 1

        # 将日期字符串转换为 datetime 对象
        dt = datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ")
        # 提取日期部分
        commit_date = dt.date()

        # 统计每个日期的提交次数
        if commit_date in commit_date_dict:
            commit_date_dict[commit_date] += 1
        else:
            commit_date_dict[commit_date] = 1

    # 对作者提交次数进行排序（从高到低）
    sorted_authors = sorted(author_dict.items(), key=lambda x: x[1], reverse=True)
    # 提取排序后的提交次数和作者名字
    commits_by_author = [item[1] for item in sorted_authors]
    authors = [item[0] for item in sorted_authors]

    # 计算总提交次数
    total_commits = sum(commits_by_author)
    # 计算每个作者的提交次数占比
    commits_percentage = [commit / total_commits * 100 for commit in commits_by_author]

    # 创建第一个图表：作者提交次数占比统计
    fig1, ax1 = plt.subplots(figsize=(20, 6))
    # 绘制柱状图
    ax1.bar(range(len(commits_percentage)), commits_percentage, color='skyblue', edgecolor='black', linewidth=0.5)

    # 设置 X 轴刻度标签
    total_authors = len(authors)
    if total_authors > 20:
        # 如果作者数量超过 20，只显示部分标签
        step = (total_authors - 1) / 19
        tick_positions = [int(i * step) for i in range(20)]
        ax1.set_xticks(tick_positions)
        ax1.set_xticklabels([authors[i] for i in tick_positions], rotation=45, ha='right')
    else:
        # 如果作者数量少于 20，显示所有标签
        ax1.set_xticks(range(total_authors))
        ax1.set_xticklabels(authors, rotation=45, ha='right')

    # 设置图表标题和坐标轴标签
    ax1.set_title(f'所有作者提交次数占比统计（共{total_authors}位作者）')
    ax1.set_xlabel('作者')
    ax1.set_ylabel('提交次数占比(%)')

    # 调整布局，避免标签重叠
    plt.tight_layout()
    # 保存图表为 PNG 文件
    fig1.savefig('commits_by_author.png', dpi=300, bbox_inches='tight')

    # 提取提交日期和对应的提交次数
    dates = list(commit_date_dict.keys())
    commits_by_date = list(commit_date_dict.values())

    # 计算日期范围
    start_date = min(dates)
    end_date = max(dates)
    from datetime import timedelta
    # 生成从开始日期到结束日期的所有日期列表
    all_dates = []
    current_date = start_date
    while current_date <= end_date:
        all_dates.append(current_date)
        current_date += timedelta(days=1)

    # 补全所有日期的提交次数（如果某天没有提交，则记为 0）
    complete_commits = [commit_date_dict.get(date, 0) for date in all_dates]

    # 计算总天数
    total_days = len(all_dates)

    # 创建第二个图表：提交次数按日期统计
    fig2, ax2 = plt.subplots(figsize=(20, 6))
    # 绘制折线图
    ax2.plot(all_dates, complete_commits, marker='', linestyle='-', color='black', linewidth=0.5)
    # 设置图表标题和坐标轴标签
    ax2.set_title(f'提交次数按日期统计（{start_date.strftime("%Y-%m-%d")}至{end_date.strftime("%Y-%m-%d")}，共{total_days}天）')
    ax2.set_xlabel('日期')
    ax2.set_ylabel('提交次数')
    # 设置 X 轴日期格式
    ax2.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
    # 旋转 X 轴标签
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

    # 调整布局，避免标签重叠
    plt.tight_layout()
    # 保存图表为 PNG 文件
    fig2.savefig('./commits_by_date.png', dpi=300, bbox_inches='tight')

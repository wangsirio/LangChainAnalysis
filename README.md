对LangChain库进行分析，使用REST api获取了LangChain库issue commit pullRequests的数据并进行了可视化

仓库中的数据格式有错误，如需运行请重新运行以获取数据
# LangChain GitHub 数据分析工具

本项目用于分析 [LangChain](https://github.com/langchain-ai/langchain) GitHub 仓库数据，包括 `Commits`、`Issues` 和 `Pull Requests`，并通过图表进行可视化。

## 功能

1. **数据下载**
   - 使用 GitHub API 下载 Commits、Issues 和 Pull Requests 数据。
   - 自动保存数据为 JSON 文件。

2. **数据分析**
   - 提交记录 (Commits)
     - 统计作者提交次数、日期分布。
     - 关键词提取与词云展示。
   - Issues 和 Pull Requests
     - 统计每日新建数量与 Open 状态数量。

3. **可视化**
   - 柱状图和折线图展示数据统计。
   - 关键词词云展示提交信息的核心内容。
## 使用方法

### 1. 环境准备

- 安装依赖：
  ```bash
  pip install -r requirements.txt


## 项目结构

```text
LangChainAnalysis
├── .gitignore                 # 忽略文件
├── commits.json               # 保存的 commits 数据
├── issues                     # 保存的 issues 数据
├── pullRequests               # 保存的 pull requests 数据
├── DealCommits.py             # 处理 commits 数据的脚本
├── DealIssues.py              # 处理 issues 数据的脚本
├── DealPulls.py               # 处理 pull requests 数据的脚本
├── DownloadCommits.py         # 下载 commits 数据的脚本
├── DownloadIssues.py          # 下载 issues 数据的脚本
├── DownloadPulls.py           # 下载 pull requests 数据的脚本
├── commits_High_frequency_word_analysis.py # 提取关键词的脚本
├── README.md                  # 项目说明文档
├── 图片文件                   # 自动生成的图表

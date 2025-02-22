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

4.**文本分析**
   - 对提交记录中的消息进行文本预处理和词频统计,提取高频关键词并进行可视化，包括绘制柱状图和生成词云
## 使用方法
   - 运行main.py。
## 项目结构

```text
LangChainAnalysis
├── .gitignore                 # 忽略文件
├── DealCommits.py             # 处理 commits 数据的脚本
├── DealIssues.py              # 处理 issues 数据的脚本
├── DealPulls.py               # 处理 pull requests 数据的脚本
├── DownloadCommits.py         # 下载 commits 数据的脚本
├── DownloadIssues.py          # 下载 issues 数据的脚本
├── DownloadPulls.py           # 下载 pull requests 数据的脚本
├── commits_High_frequency_word_analysis.py # 提取关键词的脚本
├── README.md                  # 项目说明文档
├── main.py                  # 主文件，直接运行即可
├── 图片文件                   # 自动生成的图表
```
## 项目优势
   - 功能丰富：实现了从数据获取、统计分析到可视化的完整流程，能够全面地展示项目的相关数据和信息。
   - 模块化设计：代码结构清晰，各个功能模块相对独立，便于阅读、理解和维护。
   - 可视化直观：使用matplotlib绘制的图表直观地展示了数据的变化趋势和分布情况，有助于快速理解数据特征。
## 项目缺点
   - 错误处理不完善：在获取数据的过程中，虽然对请求失败进行了简单的错误处理，但对于其他可能出现的异常情况（如网络连接中断、JSON解析错误等）没有进行更详细的处理。
   - 代码重复：在统计每日新创建和处于Open状态的问题和拉取请求数量时，存在部分重复的代码逻辑，可以进行进一步的封装和优化。
   - 可扩展性有限：如果需要对不同的项目或不同的API进行数据获取和分析，可能需要对代码进行较大的修改，代码的可扩展性有待提高。

import json
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string

# 下载 NLTK 停用词数据
nltk.download('stopwords')

# 加载 Commit 数据
with open('./commits.json', 'r', encoding='utf-8') as file:
    commits_data = json.load(file)

# 提取 Commit 消息
commit_messages = [commit['commit']['message'] for commit in commits_data]

# 文本预处理函数
def preprocess_text(text):
    # 转换为小写
    text = text.lower()
    # 去除标点符号
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 分词
    words = text.split()
    # 去除停用词
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

# 对所有 Commit 消息进行预处理
all_words = []
for message in commit_messages:
    all_words.extend(preprocess_text(message))

# 统计词频
word_freq = Counter(all_words)

# 提取前 20 个高频关键词
top_keywords = word_freq.most_common(20)
print("Top 20 Keywords:")
for word, freq in top_keywords:
    print(f"{word}: {freq}")

# 可视化高频关键词
def plot_top_keywords(top_keywords):
    words, frequencies = zip(*top_keywords)
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.title('Top 20 Keywords in Commit Messages')
    plt.xticks(rotation=90)
    plt.savefig('./commits_Top20_Keywords', dpi=300, bbox_inches='tight')


# 绘制柱状图
plot_top_keywords(top_keywords)

# 生成词云
def generate_wordcloud(word_freq):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Commit Messages')
    plt.savefig('./commits_Word_Cloud', dpi=300, bbox_inches='tight')
    

# 绘制词云
generate_wordcloud(word_freq)

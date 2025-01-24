import os
import subprocess


def check_and_run(file_to_check, script_to_run):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_to_check)
    if not os.path.exists(file_path):
        print(f"文件 {file_to_check} 不存在，将执行 {script_to_run}.")
        script_path = os.path.join(current_dir, script_to_run)
        try:
            os.system(f"python {script_to_run}")
        except subprocess.CalledProcessError as e:
            print(f"执行 {script_to_run} 时出错: {e}")
    else:
        print(f"文件 {file_to_check} 存在.")


check_and_run('commits.json', 'DownloadCommits.json')
check_and_run('issues.json', 'DownloadIssues.json')
check_and_run('pullRequests.json', 'DownloadPulls.json')
os.system(f"python DealCommits.py")
os.system(f"python DealIssues.py")
os.system(f"python DealPulls.py")
os.system(f"python commits_High_frequency_word_analysis.py")
print("代码执行完毕")
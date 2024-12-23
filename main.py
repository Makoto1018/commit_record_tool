import requests
# from t.t import GITHUB_TOKEN, REPO_OWNER, REPO_NAME # api的東西

headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# 獲取提交歷史
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contributors"
response = requests.get(url, headers=headers)

# 檢查狀態碼
if response.status_code == 200:
    contributors = response.json()
    for contributor in contributors:
        print(f"{contributor['login']}: {contributor['contributions']} commits")
else:
    # 顯示錯誤訊息
    print("Failed to fetch contributors:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

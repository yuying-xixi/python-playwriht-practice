import requests
import json

import json
import requests

# 发送 JSON 数据
url = "https://www.suitanglian.com:3018/api/selection_strategy/unifiedUpdateDecision"
data = {
    "decision": {
        "decision": [
            "BALL",
            "Stick",
            "Cartoon",
            "Piece",
            "Customized Shape",
            "Drop",
            "Rectangle",
            "CUBE",
            "Block",
            "Cartoon Rabbit Ears"
        ]
    },
    "decision_key": "Decision_1",
    "is_sure": False,
    "record_id": "19086",
    "step": 1
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Content-Type": "application/json;charset=utf-8",
    "Referer": "https://www.suitanglian.com:3018/crossBorder.html",
    "Origin": "https://www.suitanglian.com:3018",
    "Cookie": "ydtsession=0f175760-659bbc05-f0c0-40f3-a344-17871711a570"
}

# 关键：必须用 data=json.dumps(data)，不能用 json=data！
response = requests.post(url, data=json.dumps(data), headers=headers)

print(f"状态码: {response.status_code}")
print(f"响应: {response.text}")

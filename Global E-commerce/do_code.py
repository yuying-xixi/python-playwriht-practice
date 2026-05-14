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
    "x-token": "009a04e154b9a9e36f21cc9a8881ec136f224d92d0160ecedfcf399d52715763cded43a8096445aaa93891e0ccab80b0e9d6b89dfbd7a6edb9102168b2990d2b56f200d23630018445a089fb979ed708a3cc3af7bc7738a7e9758c4f129290fdeacf88f5dbc9e3af755f49f26a4f23969c59877da037951deb9bb8f798f940c9eadf8cd17ed070cc01f6f238ee28740872fe62d1cb0cc9313f7dbd975a8032fe"
}

# 关键：必须用 data=json.dumps(data)，不能用 json=data！
response = requests.post(url, data=json.dumps(data), headers=headers)

print(f"状态码: {response.status_code}")
print(f"响应: {response.text}")


def do_question_3112():
    with open("./answer_bank/bank_3112.js", "r", encoding="utf-8") as f:
        python_code = json.load(f)

    url = f'https://py.suitanglian.com:3000/api/contents/307-19086-241438010104/main.ipynb'
    # 发送 JSON
    response = requests.put(
        url=url,
        json=json.loads(python_code)  # requests 会自动处理 JSON 序列化
    )

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

do_question_3112()

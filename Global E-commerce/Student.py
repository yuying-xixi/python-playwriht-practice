import json
import requests

class Student:
    def __init__(self, username: int, password: int):
        self.username = username
        self.password = password

    def do_question_3112(self):

        with open("./answer_bank/data_3112.json", "r", encoding="utf-8") as f:
            python_code = json.load(f)

        url = f'https://py.suitanglian.com:3000/api/contents/307-19086-{self.username}/main.ipynb'
        # 发送 JSON
        response = requests.put(
            url = url,
            json=python_code  # requests 会自动处理 JSON 序列化
        )

        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text}")

    def do_question_3122(self, token):
        print(f"{self.username}进行项目三任务一第二模块练习")
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
            "x-token": f"{token}"
        }

        # 用 data=json.dumps(data)转json格式
        response = requests.post(url, data=json.dumps(data), headers=headers)

        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text}")

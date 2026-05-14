import json

import requests

class Student:
    def __init__(self, username: int, password: int):
        self.username = username
        self.password = password

    # 发送put请求
    @staticmethod
    def response_put(data_name :str, aim_url :str, headers):
        """
        将答案通过put请求发送给目标地址
        :param data_name: 对应答案json
        :param headers: 请求头
        :param aim_url: 目标地址
        :return: 请求状态
        """

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        # 发送 JSON
        response = requests.put(
            url = aim_url,
            json=answer,
            headers=headers
        )

        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text}")

    # 发送post请求
    @staticmethod
    def response_post(data_name :str, aim_url :str, headers):
        """
        将答案通过post请求发送给目标地址
        :param data_name: 对应答案json
        :param aim_url: 目标地址
        :param headers: 请求头
        :return: 请求状态
        """

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        # 发送 JSON
        response = requests.post(
            url = aim_url,
            json=answer,
            headers=headers
        )

        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text}")

    # 作答311
    def do_question_3112(self):
        data_name = "data_3112.json"
        aim_url = f"https://py.suitanglian.com:3000/api/contents/307-19086-{self.username}/main.ipynb"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'
        }

        self.response_put(data_name, aim_url, headers)

    # 作答312
    def do_question_3122(self, headers):
        data_name = "data_3122.json"
        aim_url = r"https://www.suitanglian.com:3018/api/selection_strategy/unifiedUpdateDecision"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}",
            "origin": f"{headers['origin']}",
            "referer": f"{headers['referer']}"
        }
        self.response_post(data_name, aim_url, headers)
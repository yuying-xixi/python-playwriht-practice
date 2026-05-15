import json

import requests

class Student:
    def __init__(self, username: int, password: int):
        self.username = username
        self.password = password

    # 发送put请求
    @staticmethod
    def response_put(answer :dict, aim_url :str, headers):
        """
        将答案通过put请求发送给目标地址
        :param answer: 传递给服务器的答案
        :param headers: 请求头
        :param aim_url: 目标地址
        :return: 请求状态
        """

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
    def response_post(answer:dict, aim_url :str, headers):
        """
        将答案通过post请求发送给目标地址
        :param answer: 传递服务器的答案
        :param aim_url: 目标地址
        :param headers: 请求头
        :return: 请求状态
        """

        # 发送 JSON
        response = requests.post(
            url = aim_url,
            json=answer,
            headers=headers
        )

        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text}")

    # 作答211(表格题)
    def do_question_2112(self, headers):
        data_name = "data_2112.json"
        aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}",
            "origin": f"{headers['origin']}",
            "referer": f"{headers['referer']}"
        }

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_post(answer, aim_url, headers)

    # 作答222(连线题)
    def do_question_2222(self, headers_cookie):
        data_name = "data_2222.json"
        aim_url = r"https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes"

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        answer["student_id"] = f"{self.username}"
        answer["group_key"] = f"cross_border01-18874-{self.username}"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Cookie": f"{headers_cookie['cookie']}",
            "Host": "bi.suitanglian.com:3012",
            "Origin": "https://bi.suitanglian.com:3012",
            "Pasign": f"{headers_cookie['pasign']}",  # 关键！
            "Referer": "https://bi.suitanglian.com:3012/bi_tools.html",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0"
        }

        print(answer)
        self.response_post(answer, aim_url, headers)

    # 作答231(表格题)
    def do_question_2312(self, headers):
        data_name = "data_2312.json"
        aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}",
            "origin": f"{headers['origin']}",
            "referer": f"{headers['referer']}"
        }

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_post(answer, aim_url, headers)

    # 作答311(代码题)
    def do_question_3112(self):
        data_name = "data_3112.json"
        aim_url = f"https://py.suitanglian.com:3000/api/contents/307-19086-{self.username}/main.ipynb"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'
        }

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_put(answer, aim_url, headers)

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

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_post(answer, aim_url, headers)
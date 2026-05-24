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

    # 作答112(填空题)
    def do_question_1122(self, headers):
        data_name_collection = ["data_1122_A.json", "data_1122_B.json"]
        aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}",
            "origin": f"{headers['origin']}",
            "referer": f"{headers['referer']}"
        }

        for data_name in data_name_collection:
            with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
                answer = json.load(f)

            self.response_post(answer, aim_url, headers)

    # 作答122(填空题)
    def do_question_1222(self, headers):
        data_name_collection = ["data_1222_A.json", "data_1222_B.json", "data_1222_C.json", "data_1222_D.json"]
        aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}",
            "origin": f"{headers['origin']}",
            "referer": f"{headers['referer']}"
        }

        for data_name in data_name_collection:
            with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
                answer = json.load(f)

            self.response_post(answer, aim_url, headers)

    # 作答212(表格题)
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

    # 作答232(填空题)
    def do_question_2322(self, headers):
        data_name = "data_2322.json"
        aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}"
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

    # 作答312(填空题)
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

    # 作答321(代码题)
    def do_question_3212(self):
        data_name = "data_3212.json"
        # https://py.suitanglian.com:3000/api/contents/308-19087-231416100122/main.ipynb
        aim_url = f"https://py.suitanglian.com:3000/api/contents/308-19087-{self.username}/main.ipynb"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'
        }

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_put(answer, aim_url, headers)

    # 作答322(填空题)
    def do_question_3222(self, headers):
        data_name = "data_3222.json"
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

    # 作答331(代码题)
    def do_question_3312(self):
        data_name = "data_3312.json"
        # https://py.suitanglian.com:3000/api/contents/309-19088-231416100122/main.ipynb
        # https://py.suitanglian.com:3000/api/contents/309-19088-231416100122/main.ipynb
        aim_url = f"https://py.suitanglian.com:3000/api/contents/309-19088-{self.username}/main.ipynb"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'
        }

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_put(answer, aim_url, headers)

    # 作答332(填空题)
    def do_question_3322(self, headers):
        data_name = "data_3322.json"
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

    # 作答432
    def do_question_4323(self, headers):
        data_name = "data_4323.json"
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

    # 作答433
    def do_question_4333(self, headers):
        data_name = "data_4333.json"
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

    # 作答442
    def do_question_4423(self, headers):
        data_name = "data_4423.json"
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

    # 作答443
    def do_question_4433(self, headers):
        data_name = "data_4433.json"
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

    # 作答511
    def do_question_5112(self):
        data_name = "data_5112.json"
        # https://py.suitanglian.com:3000/api/contents/310-19518-231416100122/main.ipynb
        aim_url = f"https://py.suitanglian.com:3000/api/contents/310-19518-{self.username}/main.ipynb"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'
        }

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_put(answer, aim_url, headers)

    # 作答512
    def do_question_5122(self, headers):
        data_name = "data_5122.json"
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

    # 作答521
    def do_question_5212(self, headers):
        data_name = "data_5212.json"
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

        # 第二题
        data_name = "data_5212_A.json"

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_post(answer, aim_url, headers)

    #  作答522
    def do_question_5222(self, headers):
        # 作答结果分析
        data_name = "data_5222_B.json"
        aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
        print(headers)
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "accept": "application/json, text/plain, */*",
            "x-token": headers["x-token"],
            "origin": headers["origin"],
            "referer": headers["referer"]
        }

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_post(answer, aim_url, headers)

        # 作答excel表格
        data_name = "data_5222_A.json"
        aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)

        self.response_post(answer, aim_url, headers)

    # 作答611(表格题)
    def do_question_6112(self, headers):
        data_name = "data_6112.json"
        aim_url = r"https://www.suitanglian.com:3015/api/cross/submitDecision"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}"
        }

        get_url = r"https://www.suitanglian.com:3015/api/common_func/commonTable/getStepInfoByUserId?record_id=267139"
        group_id = requests.get(get_url, headers=headers).json().get("data", {}).get('group_id')

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)
            answer['group_id'] = group_id

        self.response_post(answer, aim_url, headers)

    # 作答612
    def do_question_6122(self, headers):
        data_name = "data_6122.json"
        aim_url = r"https://www.suitanglian.com:3015/api/cross/submitInterpret"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "x-token": f"{headers['x-token']}"
        }

        get_url = r"https://www.suitanglian.com:3015/api/common_func/commonTable/getStepInfoByUserId?record_id=267139"
        group_id = requests.get(get_url, headers=headers).json().get("data", {}).get('group_id')

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)
            answer['group_id'] = group_id

        self.response_post(answer, aim_url, headers)

    # 作答631(表格题)
    def do_question_6312(self, headers):
        data_name = "data_6312.json"
        aim_url = r"https://www.suitanglian.com:3015/api/cross/submitDecision"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "x-token": f"{headers['x-token']}"
        }

        get_url = r"https://www.suitanglian.com:3015/api/common_func/commonTable/getStepInfoByUserId?record_id=267141"
        group_id = requests.get(get_url, headers=headers).json().get("data", {}).get('group_id')
        print(group_id)

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)
            answer['group_id'] = group_id

        self.response_post(answer, aim_url, headers)

    # 作答632
    def do_question_6322(self, headers):
        data_name = "data_6322.json"
        aim_url = r"https://www.suitanglian.com:3015/api/cross/submitInterpret"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
            "x-token": f"{headers['x-token']}"
        }

        get_url = r"https://www.suitanglian.com:3015/api/common_func/commonTable/getStepInfoByUserId?record_id=267141"
        group_id = requests.get(get_url, headers=headers).json().get("data", {}).get('group_id')
        print(group_id)

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)
            answer['group_id'] = group_id

        self.response_post(answer, aim_url, headers)

    # 作答641(连线题)
    def do_question_6412(self, headers_cookie):
        data_name = "data_6412.json"
        aim_url = r"https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes"

        with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
            answer = json.load(f)
            answer['group_key'] = f"cross_border14-19519-{self.username}"
            answer['student_id'] = f"{self.username}"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
            "Origin": "https://bi.suitanglian.com:3012",
            "Referer": "https://bi.suitanglian.com:3012/bi_tools.html",
            "Host": "bi.suitanglian.com:3012",
            "Cookie": headers_cookie["cookie"],
            "Pasign": headers_cookie["pasign"]
        }

        self.response_post(answer, aim_url, headers)

    # 作答642
    def do_question_6422(self, headers):
        data_name = "data_6422.json"
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
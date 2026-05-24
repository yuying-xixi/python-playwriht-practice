import json
import requests



# 表格题
def do_2112():
    with open("./answer_bank/data_2112.json", "r", encoding="utf-8") as f:
        answer = json.load(f)

    # 发送 JSON
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
        "accept": "application/json, text/plain, */*",
        "x-token": "009a04e154b9a9e36f21cc9a8881ec136f224d92d0160ecedfcf399d52715763cded43a8096445aaa93891e0ccab80b0e9d6b89dfbd7a6edb9102168b2990d2b56f200d23630018445a089fb979ed708a3cc3af7bc7738a7e9758c4f129290fdeacf88f5dbc9e3af755f49f26a4f23969c59877da037951deb9bb8f798f940c9eadf8cd17ed070cc01f6f238ee287408abbbea639d8a46a5abb106dead778617",
        "origin": "https://www.suitanglian.com:3018",
        "referer": "https://www.suitanglian.com:3018/"
    }

    response = requests.post(
        url="https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData",
        json=answer,
        headers=headers
    )

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")
# 连线题
def do_2222():
    with open("./answer_bank/data_2222.json", "r", encoding="utf-8") as f:
        answer = json.load(f)

    # 发送 JSON
    headers = {
        'host': 'bi.suitanglian.com:3012',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'undefined',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'content-type': 'application/json;charset=utf-8',
        'pasign': 'a35f3bd0-5071-11f1-98dd-61702fe24b2f',
        'content-length': '113',
        'origin': 'https://bi.suitanglian.com:3012',
        'connection': 'keep-alive',
        'referer': 'https://bi.suitanglian.com:3012/bi_tools.html',
        'cookie': 'io=MRd_cQ_5OuMYB-41ABBN',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }

    response = requests.post(
        url="https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes",
        json=answer,
        headers=headers
    )

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

def do_2322():
    data_name = "data_2322.json"
    aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
        "accept": "application/json, text/plain, */*",
        "x-token": "009a04e154b9a9e36f21cc9a8881ec136f224d92d0160ecedfcf399d52715763cded43a8096445aaa93891e0ccab80b0e9d6b89dfbd7a6edb9102168b2990d2b56f200d23630018445a089fb979ed708a3cc3af7bc7738a7e9758c4f129290fdeacf88f5dbc9e3af755f49f26a4f23969c59877da037951deb9bb8f798f940c9eadf8cd17ed070cc01f6f238ee2874087de9cb18557cbbeded4456c363f8dab4"
    }

    with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
        answer = json.load(f)

    response = requests.post(json=answer, url=aim_url, headers=headers)
    print(response.status_code)
    print(response.text)

# 代码题
def do_3112():
    with open("./answer_bank/data_3112.json", "r", encoding="utf-8") as f:
        answer = json.load(f)

    # 发送 JSON
    response = requests.put(
        url="https://py.suitanglian.com:3000/api/contents/307-19086-241537011123/main.ipynb",
        json=answer
    )

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

def do_3122():
    with open("./answer_bank/data_3122.json", "r", encoding="utf-8") as f:
        answer = json.load(f)

    # 发送 JSON
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
        "accept": "application/json, text/plain, */*",
        "x-token": "009a04e154b9a9e36f21cc9a8881ec136f224d92d0160ecedfcf399d52715763cded43a8096445aaa93891e0ccab80b0e9d6b89dfbd7a6edb9102168b2990d2b56f200d23630018445a089fb979ed708a3cc3af7bc7738a7e9758c4f129290fdeacf88f5dbc9e3af755f49f26a4f23969c59877da037951deb9bb8f798f940c9eadf8cd17ed070cc01f6f238ee287408fdc0384b4d6792a3edf8f4efba4d324d",
        "origin": "https://www.suitanglian.com:3018",
        "referer": "https://www.suitanglian.com:3018/"
    }

    response = requests.post(
        url="https://www.suitanglian.com:3018/api/selection_strategy/unifiedUpdateDecision",
        json=answer,
        headers=headers
    )

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

# 表格题
def do_4323():
    with open("./answer_bank/data_4323.json", "r", encoding="utf-8") as f:
        answer = json.load(f)
    url = "https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"

    headers = {
        "x-token": "009a04e154b9a9e36f21cc9a8881ec13dbf0a54e83b1b0550588b003e19485168f484b1f488125d66f6ca1e3e910d1c5965460b8bbbc9c5a15f7805562bdc747bf4ef91ecb03de6df88f7a546568d6afe1d6d19cbd902cadeb0ac16ed9ef38658698a3c0cffb0a95ead33f750912a49d1a1bf022a56e0781ccd9971487aa640394764e253e4cfa9d76ef1d7e895e888b117bac5396116c5298ec2c8d47b98d23"
    }

    response = requests.post(headers=headers, url=url, json=answer)
    print(response.status_code)
    print(response.text)

def do_4423():
    with open("./answer_bank/data_4423.json", "r", encoding="utf-8") as f:
        answer = json.load(f)
    url = "https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"

    headers = {
        "x-token": "009a04e154b9a9e36f21cc9a8881ec13dbf0a54e83b1b0550588b003e19485168f484b1f488125d66f6ca1e3e910d1c5965460b8bbbc9c5a15f7805562bdc747bf4ef91ecb03de6df88f7a546568d6afe1d6d19cbd902cadeb0ac16ed9ef38658698a3c0cffb0a95ead33f750912a49d1a1bf022a56e0781ccd9971487aa640394764e253e4cfa9d76ef1d7e895e888b117bac5396116c5298ec2c8d47b98d23"
    }

    response = requests.post(headers=headers, url=url, json=answer)
    print(response.status_code)
    print(response.text)

def get_6112_id(aim_url :str, headers, aim_value):
    """
    将答案通过put请求发送给目标地址
    :param headers: 请求头
    :param aim_url: 目标地址
    :return: aim_value对应的值
    """

    # 发送 JSON
    response = requests.get(
        url = aim_url,
        headers=headers
    )
    result = response.json()

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")
    print(f"响应 JSON: {result.get("data", {}).get(aim_value)}")

def do_6222():
    data_name = "data_6222.json"
    aim_url = r"https://www.suitanglian.com:3015/api/cross/submitInterpret"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": "ydtsession=d6c8ab80-07a33a15-dc5d-47db-ba3b-6a9396ffc28c",
        "Origin": "https://www.suitanglian.com:3015",
        "Referer": "https://www.suitanglian.com:3015/cross_report.html",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "x-token": "009a04e154b9a9e36f21cc9a8881ec13dbf0a54e83b1b0550588b003e19485168f484b1f488125d66f6ca1e3e910d1c5965460b8bbbc9c5a15f7805562bdc747bf4ef91ecb03de6df88f7a546568d6afe1d6d19cbd902cadeb0ac16ed9ef38658698a3c0cffb0a95ead33f750912a49d1a1bf022a56e0781ccd9971487aa640394764e253e4cfa9d76ef1d7e895e888b9642de119c0cd9a332f1f8f886730e32"
    }

    get_url = r"https://www.suitanglian.com:3015/api/common_func/commonTable/getStepInfoByUserId?record_id=267139"
    group_id = requests.get(get_url, headers=headers).json().get("data", {}).get('group_id')
    print(group_id)

    with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
        answer = json.load(f)
        answer['group_id'] = group_id

    response = requests.post(aim_url, json=answer,  headers=headers)

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

def do_task_3_3():
    data_name = "data_3312.json"

    aim_url = "https://py.suitanglian.com:3000/api/contents/309-19088-231416100122/main.ipynb"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'
    }

    with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
        answer = json.load(f)

    response = requests.put(aim_url, json=answer, headers=headers)

    print(response.status_code)
    print(response.text)


def do_5222():
    data_name = "data_5222_A.json"
    aim_url = r"https://www.suitanglian.com:3018/api/traditional/financial/submitGroupData"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Length": "84",
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": "ydtsession=d4368f70-c375ba63-567d-4e6f-ad40-37672b2e974f",
        "Host": "www.suitanglian.com:3018",
        "Origin": "https://www.suitanglian.com:3018",
        "Priority": "u=0",
        "Referer": "https://www.suitanglian.com:3018/crossBorder.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "x-token": "009a04e154b9a9e36f21cc9a8881ec136f224d92d0160ecedfcf399d52715763cded43a8096445aaa93891e0ccab80b0e9d6b89dfbd7a6edb9102168b2990d2b56f200d23630018445a089fb979ed708a3cc3af7bc7738a7e9758c4f129290fdeacf88f5dbc9e3af755f49f26a4f23969c59877da037951deb9bb8f798f940c9eadf8cd17ed070cc01f6f238ee287408100fee8feba82ef83feffbc8c652ffec"
    }

    with open(f"./answer_bank/{data_name}", "r", encoding="utf-8") as f:
        answer = json.load(f)

    response = requests.post(aim_url, json=answer,  headers=headers)

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")


if __name__ == "__main__":
    do_5222()

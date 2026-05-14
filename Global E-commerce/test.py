import requests
import json

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

do_3112()
do_3122()

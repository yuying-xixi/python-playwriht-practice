import json
import requests

def do_question_3112(student_name:int):
    # 代码
    python_code = r'''

    '''

    url = f'https://py.suitanglian.com:3000/api/contents/307-19086-{student_id}/main.ipynb'
    # 直接发送 JSON
    response = requests.put(
        url = url,
        json=json.loads(python_code)  # requests 会自动处理 JSON 序列化
    )

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")


from Task import Task
from time import sleep
# student = Task(241438010104, 123456)
# student = Task(231416100122, 123456)
# student = Task(241537011123, 123456)

with Task(231416100122, 123456) as student:
    print("进入实验主页")

    # ══════════════════════════════════════════
    #  项目六任务四
    # ══════════════════════════════════════════

    print("准备进入实验主页")
    print("准备进入!项目六任务四")
    student_task = student.choose_project_task(6, 4)
    headers = student.get_headers_token(student_task)
    sleep(5)
    student_task_2 = student.start_practice(student_task, 1, 2)
    sleep(10)
    cookie = student.get_headers_cookie(page=student_task_2, x=1200, y=80,url_keyword="https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes")
    student.do_question_6412(cookie)
    student_task.reload()
    sleep(2)
    student.do_question_6422(headers)
    sleep(3)
    student.start_practice(student_task, 2, 2)
    print("准备提交!项目六任务四")
    student.submit_and_confirm(student_task, (1120, 80), (1140, 180))
    print("提交完成!!!")
    print("完成!项目六任务四")
    student.close_current_and_return()




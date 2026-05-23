from Task import Task
from time import sleep

# student = Task(241438010104, 123456)
# student = Task(231416100122, 123456)
# student = Task(241537011123, 123456)

with Task(241537011432, 123456) as student:
    print("进入实验主页")

    # ══════════════════════════════════════════
    #  项目二任务一
    # ══════════════════════════════════════════

    print("进入实验主页")
    print("准备进入!项目二任务一")
    student_task = student.choose_project_task(2, 1)
    headers = student.get_headers_token(student_task)
    student.do_question_2112(headers)
    sleep(5)
    student.start_practice(student_task, 2, 2)
    print("准备提交!项目二任务一")
    student.submit_and_confirm(student_task, (1220, 80), (1220, 170))
    print("提交完成!!!")
    print("完成!项目二任务一")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目二任务二
    # ══════════════════════════════════════════

    print("准备进入实验主页")
    print("准备进入!项目二任务二")
    student_task = student.choose_project_task(2, 2)
    sleep(5)
    student_task_2 = student.start_practice(student_task, 2, 2)
    sleep(5)
    cookie = student.get_headers_cookie(page=student_task_2, x=1120, y=80, url_keyword="https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes")
    student.do_question_2222(cookie)
    student_task.reload()
    sleep(5)
    print("准备提交!项目二任务二")
    student.start_practice(student_task, 2, 2)
    student.submit_and_confirm(student_task, (1220, 80), (1220, 170))
    print("提交完成!!!")
    print("完成!项目二任务二")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目二任务三
    # ══════════════════════════════════════════

    print("准备进入!项目二任务三")
    student_task = student.choose_project_task(2, 3)
    headers = student.get_headers_token(student_task)
    student.do_question_2312(headers)
    student_task.reload()
    student_task_2 = student.start_practice(student_task, 1, 2)

    # 提交模块一
    sleep(5)
    print("准备提交!项目二任务三")
    student.submit_and_confirm(student_task, (1200, 100), (1240, 190))
    print("第一模块提交完成!!!")
    sleep(2)
    student.do_question_2322(headers)
    print("######需要手动提交项目二任务三第二模块#####")
    print("第二模块提交完成!!!")
    print("完成!项目二任务三")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目三任务一
    # ══════════════════════════════════════════

    print("准备进入!项目三任务一")
    student_task = student.choose_project_task(3, 1)
    headers = student.get_headers_token(student_task)
    student.do_question_3112()
    student.do_question_3122(headers)
    student_task.reload()
    student.start_practice(student_task, 2, 2)
    print("准备提交!项目三任务一")
    student.submit_and_confirm(student_task, (860, 80), (890, 180))
    print("提交完成!!!")
    print("完成!项目三任务一")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目三任务二
    # ══════════════════════════════════════════

    print("准备进入!项目三任务二")
    student_task = student.choose_project_task(3, 2)
    token = student.get_headers_token(student_task)
    student.do_question_3212()
    student.do_question_3222(token)
    student_task.reload()
    student.start_practice(student_task, 2, 2)
    print("准备提交!项目三任务二")
    student.submit_and_confirm(student_task, (1130, 80), (1150, 180))
    print("提交完成!!!")
    print("完成!项目三任务二")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目三任务三
    # ══════════════════════════════════════════

    print("准备进入!项目三任务三")
    student_task = student.choose_project_task(3, 3)
    token = student.get_headers_token(student_task)
    student.do_question_3312()
    student.do_question_3322(token)
    student_task.reload()
    student.start_practice(student_task, 2, 2)
    print("准备提交!项目三任务三")
    student.submit_and_confirm(student_task, (1130, 80), (1150, 180))
    print("提交完成!!!")
    print("完成!项目三任务三")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目四任务三
    # ══════════════════════════════════════════

    print("准备进入!项目四任务三")
    task = student.choose_project_task(4, 3)
    token = student.get_headers_token(task)
    sleep(1)

    # 作答第二模块
    student.do_question_4323(token)

    # 提交第二模块
    student.start_practice(task, 2, 3)
    sleep(3)
    student.submit_and_confirm(task, (1220, 80), (1240, 170))
    sleep(2)

    # 作答第三模块
    student.do_question_4323(token)
    print("######需要手动提交项目四任务三第三模块#####")
    sleep(2)

    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目四任务四
    # ══════════════════════════════════════════

    print("准备进入!项目四任务四")
    task = student.choose_project_task(4, 4)
    token = student.get_headers_token(task)
    sleep(1)

    # 作答第二模块
    student.do_question_4323(token)

    # 提交第二模块
    student.start_practice(task, 2, 3)
    sleep(3)
    student.submit_and_confirm(task, (1220, 80), (1240, 170))
    sleep(2)

    # 作答第三模块
    student.do_question_4323(token)
    print("######需要手动提交项目四任务四第三模块#####")
    sleep(1)

    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目五任务一
    # ══════════════════════════════════════════

    print("准备进入!项目五任务一")
    student_task = student.choose_project_task(5, 1)
    token = student.get_headers_token(student_task)
    student.do_question_5112()
    student.do_question_5122(token)
    student_task.reload()
    sleep(5)
    student.start_practice(student_task, 2, 2)
    print("准备提交!项目五任务一")
    sleep(5)
    student.submit_and_confirm(student_task, (1130, 80), (1150, 180))
    print("提交完成!!!")
    print("完成!项目五任务一")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目五任务二
    # ══════════════════════════════════════════

    print("准备进入!项目五任务二")
    student_task = student.choose_project_task(5, 2)
    token = student.get_headers_token(student_task)
    student.do_question_5212(token)
    student_task.reload()
    sleep(5)
    student.start_practice(student_task, 1, 2)

    # 提交模块一
    sleep(3)
    print("准备提交!项目二任务三")
    student.submit_and_confirm(student_task, (1200, 100), (1240, 190))
    print("第一模块提交完成!!!")
    student.do_question_5222(token)

    # 提交模块二
    sleep(2)
    student.start_practice(student_task, 2, 2)
    sleep(2)
    student.submit_and_confirm(student_task, (1200, 100), (1240, 190))

    print("提交完成!!!")
    print("完成!项目五任务二")
    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目六任务一
    # ══════════════════════════════════════════

    print("准备进入!项目六任务一")
    student_task = student.choose_project_task(6, 1)
    headers = student.get_headers_token(student_task)
    sleep(5)
    print(headers)
    student.do_question_6112(headers)
    student.start_practice(student_task, 1, 2)
    sleep(3)
    print("准备提交!项目六任务一模块一")
    student.submit_and_confirm(student_task, (1220, 60), (1230, 160))
    print("模块一提交完成!!!")
    sleep(1)
    student.do_question_6122(headers)
    student_task = student.start_practice(student_task, 2, 2)
    print("准备提交!项目六任务一模块二")
    student.submit_and_confirm(student_task, (210, 430), (300, 380))
    print("完成!项目六任务一")

    student.close_current_and_return()

    # ══════════════════════════════════════════
    #  项目六任务三
    # ══════════════════════════════════════════

    print("准备进入!项目六任务三")
    student_task = student.choose_project_task(6, 3)
    headers = student.get_headers_token(student_task)
    sleep(5)
    print(headers)
    student.do_question_6312(headers)
    student.start_practice(student_task, 1, 2)
    sleep(3)
    print("准备提交!项目六任务三模块一")
    student.submit_and_confirm(student_task, (1220, 60), (1230, 160))
    print("模块一提交完成!!!")
    sleep(1)
    student.do_question_6322(headers)
    student_task = student.start_practice(student_task, 2, 2)
    print("准备提交!项目六任务三模块二")
    student.submit_and_confirm(student_task, (210, 290), (300, 230))
    print("完成!项目六任务三")

    student.close_current_and_return()

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
    cookie = student.get_headers_cookie(page=student_task_2, x=1200, y=80,
                                        url_keyword="https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes")
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

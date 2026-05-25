from Task import Task
from time import sleep


# ══════════════════════════════════════════
#  项目一任务一
# ══════════════════════════════════════════
def task_1_1(student):
    print("进入 实验主页")
    print("进入 项目一任务一")
    
    # 作答模块2
    student_task = student.choose_project_task(1, 1)
    token = student.get_headers_token(student_task)
    student.do_question_1122(token)
    sleep(5)
    
    # 提交模块2
    student.start_practice(student_task, 2, 2)
    sleep(5)
    print("正在提交,项目一任务一")
    # student.submit_and_confirm(student_task, (180, 80), (1200, 80), (1240, 180))
    student.confirm_commit_click(student_task, is_click_tab=True)
    print("完成 项目一任务一")
    
    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目一任务二
# ══════════════════════════════════════════
def task_1_2(student):
    print("进入 实验主页")
    print("进入项目一任务二")
    
    # 作答模块2
    student_task = student.choose_project_task(1, 2)
    token = student.get_headers_token(student_task)
    student.do_question_1222(token)
    sleep(5)
    
    # 提交模块2
    print("正在提交, 项目一任务二")
    student.start_practice(student_task, 2, 2)
    sleep(5)
    # student.submit_and_confirm(student_task, (200, 80), (350, 80), (550, 80), (1200, 80), (1220, 180))
    student.confirm_commit_click(student_task, is_click_tab=True)
    print("完成 项目一任务二")
    
    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目二任务一
# ══════════════════════════════════════════
def task_2_1(student):
    print("进入实验主页")
    print("正在进入!项目二任务一")
    
    # 作答模块2
    student_task = student.choose_project_task(2, 1)
    token = student.get_headers_token(student_task)
    student.do_question_2112(token)
    
    # 提交作答模块2
    print("正在提交!项目二任务一")
    student.start_practice(student_task, 2, 2)
    sleep(5)
    student.confirm_commit_click(student_task)
    print("完成 项目二任务一")
    
    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目二任务二
# ══════════════════════════════════════════
def task_2_2(student):
    print("正在进入实验主页")
    print("正在进入!项目二任务二")

    # 作答模块2
    student_task = student.choose_project_task(2, 2)
    sleep(5)
    student.start_practice(student_task, 2, 2)
    sleep(5)
    cookie = student.get_headers_cookie(page=student_task, url_keyword="https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes")

    if not cookie:
        student.close_current_and_return()
        return "项目二任务二可能已经作答或cookie获取失败"

    student.do_question_2222(cookie)
    student_task.reload()
    sleep(5)

    # 提交模块2
    student.start_practice(student_task, 2, 2)
    sleep(5)
    print("正在提交!项目二任务二")
    student.confirm_commit_click(student_task)
    print("提交完成!!!")
    print("完成!项目二任务二")

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目二任务三
# ══════════════════════════════════════════

def task_2_3(student):
    print("正在进入实验主页")
    print("正在进入!项目二任务三")

    # 作答模块1
    student_task = student.choose_project_task(2, 3)
    headers = student.get_headers_token(student_task)
    student.do_question_2312(headers)
    student_task.reload()
    sleep(5)
    student.start_practice(student_task, 1, 2)
    sleep(5)

    # 提交模块1
    print("正在提交!项目二任务三")
    student.confirm_commit_click(student_task)
    print("第一模块提交完成!!!")
    sleep(2)

    # 作答模块2
    student.do_question_2322(headers)

    # 提交模块2
    print("第二模块提交完成!!!")
    print("完成!项目二任务三")
    student.start_practice(student_task, 2, 2)
    sleep(5)
    student.confirm_commit_click(student_task)

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目三任务一
# ══════════════════════════════════════════
def task_3_1(student):
    print("正在进入实验主页")
    print("正在进入!项目三任务一")

    # 作答模块1 模块2
    student_task = student.choose_project_task(3, 1)
    token = student.get_headers_token(student_task)
    student.do_question_3112()
    student.do_question_3122(token)
    student_task.reload()
    sleep(5)

    # 提交模块2
    student.start_practice(student_task, 2, 2)
    sleep(5)
    print("正在提交!项目三任务一")
    student.confirm_commit_click(student_task)
    print("提交完成!!!")
    print("完成!项目三任务一")

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目三任务二
# ══════════════════════════════════════════
def task_3_2(student):
    print("正在进入实验主页")
    print("正在进入!项目三任务二")

    # 作答模块1 模块2
    student_task = student.choose_project_task(3, 2)
    token = student.get_headers_token(student_task)
    student.do_question_3212()
    student.do_question_3222(token)
    student_task.reload()
    sleep(5)

    # 提交模块2
    student.start_practice(student_task, 2, 2)
    sleep(5)
    print("正在提交!项目三任务二")
    student.confirm_commit_click(student_task)
    print("提交完成!!!")
    print("完成!项目三任务二")

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目三任务三
# ══════════════════════════════════════════
def task_3_3(student):
    print("正在进入实验主页")
    print("正在进入!项目三任务三")

    # 作答模块1 模块2
    student_task = student.choose_project_task(3, 3)
    token = student.get_headers_token(student_task)
    student.do_question_3312()
    student.do_question_3322(token)
    student_task.reload()
    sleep(5)

    # 提交模块2
    student.start_practice(student_task, 2, 2)
    sleep(5)
    print("正在提交!项目三任务三")
    student.confirm_commit_click(student_task)
    print("提交完成!!!")
    print("完成!项目三任务三")

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目四任务三
# ══════════════════════════════════════════
def task_4_3(student):
    print("正在进入实验主页")
    print("正在进入!项目四任务三")

    # 作答模块2
    student_task = student.choose_project_task(4, 3)
    token = student.get_headers_token(student_task)
    student.do_question_4323(token)
    sleep(5)

    # 提交模块2
    student.start_practice(student_task, 2, 3)
    sleep(5)
    student.confirm_commit_click(student_task)

    # 作答模块3
    student.do_question_4333(token)
    student.start_practice(student_task, 3, 3)
    sleep(5)
    student.confirm_commit_click(student_task)

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目四任务四
# ══════════════════════════════════════════
def task_4_4(student):
    print("正在进入实验主页")
    print("正在进入!项目四任务四")

    # 作答模块2
    student_task = student.choose_project_task(4, 4)
    token = student.get_headers_token(student_task)
    sleep(1)
    student.do_question_4423(token)
    sleep(5)

    # 提交模块2
    student.start_practice(student_task, 2, 3)
    sleep(5)
    student.confirm_commit_click(student_task)

    # 作答模块3
    student.do_question_4433(token)
    student.start_practice(student_task, 3, 3)
    student.confirm_commit_click(student_task)

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目五任务一
# ══════════════════════════════════════════
def task_5_1(student):
    print("正在进入实验主页")
    print("正在进入!项目五任务一")

    # 作答模块1 模块2
    student_task = student.choose_project_task(5, 1)
    token = student.get_headers_token(student_task)
    student.do_question_5112()
    student.do_question_5122(token)
    student_task.reload()
    sleep(5)

    # 提交模块2
    student.start_practice(student_task, 2, 2)
    sleep(5)
    print("正在提交!项目五任务一")
    student.confirm_commit_click(student_task)
    print("提交完成!!!")
    print("完成!项目五任务一")

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目五任务二
# ══════════════════════════════════════════
def task_5_2(student):
    print("正在进入实验主页")
    print("正在进入!项目五任务二")

    # 作答模块1
    student_task = student.choose_project_task(5, 2)
    token = student.get_headers_token(student_task)
    sleep(2)
    student.do_question_5212(token)
    sleep(5)

    # 提交模块1
    student.start_practice(student_task, 1, 2)
    sleep(5)
    print("正在提交!项目五任务三")
    student.confirm_commit_click(student_task)
    print("第一模块提交完成!!!")

    # 作答模块2
    student.do_question_5222(token)
    student.start_practice(student_task, 2, 2)
    sleep(5)
    student.save_click(student_task)
    student.confirm_commit_click(student_task)
    print("提交完成!!!")
    print("完成!项目五任务二")

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目六任务一
# ══════════════════════════════════════════
def task_6_1(student):
    print("正在进入实验主页")
    print("正在进入!项目六任务一")

    # 作答模块1
    student_task = student.choose_project_task(6, 1)
    token = student.get_headers_token(student_task)
    sleep(5)
    student.do_question_6112(token)

    # 提交模块1
    student.start_practice(student_task, 1, 2)
    sleep(5)
    print("正在提交!项目六任务一模块一")
    student.confirm_commit_click(student_task)
    print("模块一提交完成!!!")

    # 作答模块2
    student.do_question_6122(token)

    # 提交模块2
    student.start_practice(student_task, 2, 2)
    sleep(5)
    print("正在提交!项目六任务一模块二")
    student.confirm_commit_click(student_task)
    print("完成!项目六任务一")

    student.close_current_and_return()

# ══════════════════════════════════════════
#  项目六任务三
# ══════════════════════════════════════════
def task_6_3(student):
    print("正在进入实验主页")
    print("正在进入!项目六任务三")

    # 作答模块1
    student_task = student.choose_project_task(6, 3)
    token = student.get_headers_token(student_task)
    sleep(5)
    student.do_question_6312(token)

    # 提交模块1
    student.start_practice(student_task, 1, 2)
    sleep(5)
    print("正在提交!项目六任务三模块一")
    student.confirm_commit_click(student_task)
    print("模块一提交完成!!!")

    # 作答模块2
    student.do_question_6322(token)
    student_task = student.start_practice(student_task, 2, 2)
    sleep(5)

    # 提交模块2
    print("正在提交!项目六任务三模块二")
    student.confirm_commit_click(student_task)
    print("完成!项目六任务三")

    student.close_current_and_return()


# ══════════════════════════════════════════
#  项目六任务四
# ══════════════════════════════════════════
def task_6_4(student):
    print("正在进入实验主页")
    print("正在进入!项目六任务四")

    # 作答模块1
    student_task = student.choose_project_task(6, 4)
    token = student.get_headers_token(student_task)
    sleep(5)
    student.start_practice(student_task, 1, 2)
    sleep(5)
    cookie = student.get_headers_cookie(page=student_task, url_keyword="https://bi.suitanglian.com:3012/api/bitools/apiSaveProcessNodes")

    if not cookie:
        student.close_current_and_return()
        return "项目六任务四可能已经作答或cookie获取失败"

    student.do_question_6412(cookie)
    student_task.reload()
    sleep(2)
    student.do_question_6422(token)
    sleep(3)

    # 提交模块2
    student.start_practice(student_task, 2, 2)
    print("正在提交!项目六任务四")
    student.confirm_commit_click(student_task)
    sleep(3)
    print("提交完成!!!")
    print("完成!项目六任务四")

    student.close_current_and_return()
    return 0

if __name__ == "__main__":
    # student = Task(241438010104, 123456)
    # student = Task(231416100122, 123456)
    # student = Task(241537011123, 123456)

    with Task(231416100122, 123456) as student:
        # task_1_1(student)
        # task_1_2(student)
        # task_2_1(student)
        # task_2_2(student)
        # task_2_3(student)
        # task_3_1(student)
        # task_3_2(student)
        # task_3_3(student)
        # task_4_3(student)
        # task_4_4(student)
        # task_5_1(student)
        # task_5_2(student)
        # task_6_1(student)
        # task_6_3(student)
        # task_6_4(student)
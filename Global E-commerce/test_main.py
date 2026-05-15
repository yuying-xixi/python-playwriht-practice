from Task import Task
from time import sleep
# student = Task(241438010104, 123456)
# student = Task(231416100122, 123456)
# student = Task(241537011123, 123456)

with Task(231416100122, 123456) as student:
    print("进入实验主页")

    print("准备进入!项目二任务三")
    student_task = student.choose_project_task(2, 3)
    headers = student.get_headers_token(student_task)
    student.do_question_2312(headers)
    student_task.reload()
    student_task_2 = student.start_practice(student_task, 2, 2)
    print("准备提交!项目二任务三")
    student.submit_and_confirm(student_task, (1220, 80), (1220, 170))
    print("提交完成!!!")
    print("完成!项目二任务三")
    student.close_current_and_return()
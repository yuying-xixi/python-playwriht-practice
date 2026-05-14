from Task import Task

student = Task(241438010104, 123456)
# student = Task(231416100122, 123456)
# student = Task(241537011123, 123456)

print("进入实验主页")

print("进入!项目三任务一")
student1_task = student.choose_project_task(3, 1)
token = student.get_headers(student1_task)
student.do_question_3112()
student.do_question_3122(token)
student1_task.reload()
student.start_practice(student1_task, 2, 2)
print("提交!项目三任务一")
student.submit_and_confirm(student1_task)
print("提交完成!!!")
print("完成!项目三任务一")
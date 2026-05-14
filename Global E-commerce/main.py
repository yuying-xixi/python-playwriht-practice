from Task import Task
from time import sleep

# student1 = Task(241438010104, 123456)
student2 = Task(231416100122, 123456)
# student3 = Task(231416100123, 123456)

print("进入实验主页")
student1_task = student2.choose_project_task(3, 1)

print("进入项目三任务一")
token = student2.get_x_token(student1_task)
student2.do_question_3112()
student2.do_question_3122(token)
student1_task.reload()
student2.start_practice(student1_task, 2, 2)

print("进入项目三任务一完成")
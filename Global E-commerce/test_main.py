from Task import Task

# student = Task(241438010104, 123456)
student = Task(231416100122, 123456)
# student = Task(241537011123, 123456)


print("进入实验主页")

print("进入!项目二任务一")
student_task = student.choose_project_task(2, 1)
token = student.get_headers(student_task)
student.do_question_2112(token)
student_task.reload()
student_task_2 = student.start_practice(student_task, 2, 2)
print("提交!项目二任务一")
student.debug_click(student_task_2, 1220, 80)
student.debug_click(student_task_2, 1220, 170)
student.submit_and_confirm(student_task, (1220, 80), (1220, 170))
print("提交完成!!!")
print("完成!项目二任务一")
student.close_current_and_return()
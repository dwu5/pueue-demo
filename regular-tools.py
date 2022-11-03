import re
import subprocess
from itertools import groupby

"""
This is a demo of getting pueue task information by regular expression.
Strongly recommend using json based methods. 
Please check tools.py.
"""


def pueue_info():
    # 获取pueue所有输出信息
    log = subprocess.check_output('pueue').decode('utf-8')

    if 'Task list is empty' in log:
        print('Task list is empty.')
        return 'Task list is empty.'
    else:
        # 划分信息 且只保留任务信息
        log_content = log.split()

        # 获取任务间单行分隔线
        pattern = '[─|═]+'
        line = re.findall(pattern, log)

        # 根据任务间单行分隔线 划分任务元素
        # 若元素不为——或══，则key为False； key为False的元素被归为一类；
        # key为False和True的元素组交替出现，形成分组; 保留key为False的group
        log_group = [list(group) for key, group in groupby(log_content, lambda x: x in line) if not key]
        # for i in enumerate(log_group):
        #     print(i)
    return log_group


def get_id(log_group):
    if log_group:
        for task in log_group:
            if task[2] == 'BB':
                return task[0]


def get_status(log_group):
    if log_group:
        for task in log_group:
            if task[2] == 'BB':
                return task[1]


log = pueue_info()
id = get_id(pueue_info())
status = get_status(pueue_info())
print(f"log: \n{log}", end='\n\n')
print(f"id: {id}, status: {status}")

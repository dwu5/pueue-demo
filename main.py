from tools import *


def executant():
    log_json = get_pueue_log()
    print(f"log json: {log_json}", end='\n\n')

    task_id = get_pueue_id('CCC')
    print(f"id: {task_id}", end='\n\n')

    task_status = get_pueue_status('CCC')
    print(f"status: {task_status}", end='\n\n')

    task_output = get_pueue_output('CCC')
    print(f"output: \n{task_output}", end='\n\n')


if __name__ == '__main__':
    executant()

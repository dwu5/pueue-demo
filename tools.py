import json
import subprocess


def get_pueue_log() -> dict:
    pueue_log = subprocess.check_output(['pueue', 'log', '-j']).decode()
    log_json = json.loads(pueue_log)

    if len(log_json) == 0:
        raise Exception("Task list is empty.")
    return log_json


def get_pueue_id(pueue_label: str) -> int:
    log_json = get_pueue_log()

    for task in log_json.values():
        if task['task']['label'] == pueue_label:
            return task['task']['id']
    raise Exception("Couldn't find the task when trying to get pueue id by pueue label!")


def get_pueue_status(pueue_label: str) -> str:
    """
    known status includes: Running, Queued, Paused,
                           Success, Killed, Failed, Stashed
    """
    log_json = get_pueue_log()

    for task in log_json.values():
        if task['task']['label'] == pueue_label:
            # Running, Queued, Paused
            if type(task['task']['status']) == str:
                return task['task']['status']
            else:
                # Success, Killed
                if list(task['task']['status'].keys())[0] == 'Done' and type(
                        task['task']['status']['Done']) == str:
                    return task['task']['status']['Done']
                # Failed
                elif list(task['task']['status'].keys())[0] == 'Done' and type(
                        task['task']['status']['Done']) == dict:
                    return list(task['task']['status']['Done'].keys())[0]
                # Stashed
                else:
                    return list(task['task']['status'].keys())[0]
    raise Exception("Couldn't find the task when trying to get task status by pueue label!")


def get_pueue_output(pueue_label: str) -> str:
    pueue_id = get_pueue_id(pueue_label)
    task_log = subprocess.check_output(['pueue', 'log', '-f', f'{pueue_id}']).decode()
    return task_log


def check_pueue_group(group: str):
    pueue_state = subprocess.check_output(['pueue', 'status', '-j']).decode()
    state_json = json.loads(pueue_state)
    pueue_group_list = list(state_json['groups'].keys())

    if group in pueue_group_list:
        return
    else:
        if group in ['0123', '4567']:
            subprocess.run(['pueue', 'group', 'add', group])
        else:
            raise ValueError('Only gpu_index 0123 or 4567 is supported!')

import datetime

DONE = "done"
HELP = "help"
TASK = "add"
LIST = "list"
REPORT = "report"
COMPLETE = "fin"

COMMANDS = [
    (DONE, "exit"),
    (HELP, "prints this message"),
    (TASK, "adds a task"),
    (LIST, "lists the tasks"),
    (REPORT, "lists the tasks and the time to complete them"),
    (COMPLETE, "marks <task_id> task complete"),
]

todos = {}

def parse_command(rcvd):
    lowered = rcvd.lower()
    for cmd, _help in COMMANDS:
        if lowered.startswith(cmd):
            return cmd


def print_help():
    print(f"cmd\thelp")
    print(f"---\t----")
    for cmd, help in COMMANDS:
        print(f"{cmd}\t{help}")


def add_task(rcvd):
    todos[len(todos)] = {"task": rcvd, "s": datetime.datetime.now()}


def complete_task(task_id_str):
    task_id = int(task_id_str)
    todos[task_id]["c"] = datetime.datetime.now()


def remove_cmd(cmd, rcvd):
    rcvd = rcvd[len(cmd):].strip()
    return rcvd


def list_tasks():
    for i, task in todos.items():
        if "c" not in task:
            print(f"{i}\t{task['task']}")


def task_report():
    now = datetime.datetime.now()
    print(f"id\tdur\t\ttask")
    print(f"--\t---\t\t----")
    for i, task in todos.items():
        dur = now-task['s']
        if "c" in task:
            dur = task["c"] - task['s']
        else:
            dur = "pending\t"
        print(f"{i}\t{dur}\t{task['task']}")


def main_loop():
    while True:
        rcvd = input("Enter command:")
        cmd = parse_command(rcvd)

        if cmd == DONE:
            break
        if cmd is not None:
            rcvd = remove_cmd(cmd, rcvd)
        if cmd == HELP:
            print_help()
        elif cmd == TASK:
            add_task(rcvd)
        elif cmd == COMPLETE:
            complete_task(rcvd)
        elif cmd == LIST:
            list_tasks()
        elif cmd == REPORT:
            task_report()
        else:
            print_help()


if __name__ == '__main__':
    main_loop()
    list_tasks()


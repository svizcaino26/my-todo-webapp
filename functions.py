FILEPATH = "todoList.txt"

def get_tasks(filepath=FILEPATH):
    """
    Read a text file and return the list of tasks.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        tasks = file.readlines()
    return tasks


def write_tasks(tasks, filepath=FILEPATH):
    """
    Writes the tasks list in a text file.
    :param tasks:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(tasks)


if __name__ == "__main__":
    print("Hello from functions")

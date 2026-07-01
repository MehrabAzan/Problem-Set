def find_task_pair(task_times, available_time):
    seen = set()
    for time in task_times:
        needed = available_time - time
        if needed in seen:
            return True
        seen.add(time)
    return False

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))
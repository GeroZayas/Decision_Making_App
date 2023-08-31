# TODO: input the tasks
# TODO: See list of tasks
# present two at a time
# user chooses one, that one gets a point
# compare each task, select the one with more points
# if two have same amount of points, choose the one that won over those two

from collections import defaultdict
from itertools import combinations

dict_of_tasks = defaultdict(int)

on = True
while on:
    new_task = input("Insert TASK (leave blank to stop): ")
    if new_task in ['', ' ', '   ']:
        on = False
    else:
        dict_of_tasks[new_task]

task_combinations = list(combinations(dict_of_tasks.keys(), 2))
# print(f"==>> task_combinations: {task_combinations}")

for task_comb in task_combinations:
    print("1", task_comb[0], end=' or 2 ')
    print(task_comb[1])
    user_choice = input("::: ")
    if user_choice == '1':
        dict_of_tasks[task_comb[0]] += 1
    elif user_choice == '2':
        dict_of_tasks[task_comb[1]] += 1
        
# print(dict_of_tasks)

sorted_task_dict = dict(sorted(dict_of_tasks.items(), key=lambda x: x[1],reverse=True))

print("""
        -----------
        PRIORITIES:
        -----------""")
for task, ranking in sorted_task_dict.items():
    print(f"{task:35}", ranking)
    print()
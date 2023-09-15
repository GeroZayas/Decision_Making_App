# TODO -> User inserts tasks and
# ranks them in importance or urgency from 0(min) to 10(max)
# TODO -> The program compares the tasks with the same ranking
# TODO -> Insert date

from collections import defaultdict
from itertools import combinations
from datetime import date

# Get the current date
today = date.today()

dict_of_tasks = defaultdict(int)

on = True
while on:
    new_task = input("Insert TASK (leave blank to stop): ")
    if new_task in ["", " ", "   "]:
        on = False
    else:
        dict_of_tasks[new_task]

task_combinations = list(combinations(dict_of_tasks.keys(), 2))
# print(f"==>> task_combinations: {task_combinations}")

for task_comb in task_combinations:
    print("\nWhat is more important and urgent right now?\n")
    print("1 -> ", f"||{task_comb[0]}||", end=" or 2 -> ")
    print(f"||{task_comb[1]}||")
    user_choice = input("::: ")
    if user_choice == "1":
        dict_of_tasks[task_comb[0]] += 1
    elif user_choice == "2":
        dict_of_tasks[task_comb[1]] += 1

# print(dict_of_tasks)

sorted_task_dict = dict(sorted(dict_of_tasks.items(), key=lambda x: x[1], reverse=True))

print(
    f"""
        -----------
        PRIORITIES:
        -----------
        {today}
        -----------
          
        """
)


for task, ranking in sorted_task_dict.items():
    print(f"{task:35}", ranking)
    print()

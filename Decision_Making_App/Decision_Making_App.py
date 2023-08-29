import reflex as rx

from collections import defaultdict
from itertools import combinations

dict_of_tasks = defaultdict(int)

# on = True
# while on:
#     new_task = input("Insert task or leave blank to stop: ")
#     if new_task in ['', ' ', '   ']:
#         on = False
#     else:
#         dict_of_tasks[new_task]
        


task_combinations = list(combinations(dict_of_tasks.keys(), 2))

class FormState(rx.State):
    form_data= defaultdict(int)

    def handle_submit(self, form_data: dict):
        self.form_data = form_data


    
def index():
    return rx.vstack(
        rx.heading(
            "Gero's Decision Maker", color="#b93418", font_size="3.5em"
            ), 
        rx.form(
            rx.vstack(
                rx.input(placeholder="Insert task...", id="task"),
                rx.button("Add task", type_="submit"),
            ),
            on_submit=FormState.handle_submit,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )



app = rx.App()
app.add_page(index)

app.compile()
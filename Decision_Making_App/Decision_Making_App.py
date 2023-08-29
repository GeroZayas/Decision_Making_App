import reflex as rx

class State(rx.State):
    name :str = 'Gero'
    
def index():
    return rx.vstack(
        heading_top = rx.heading(
            "Gero's Decision Maker", color="#b93418", font_size="3.5em"
            )
    )
    


app = rx.App()
app.add_page(index)

app.compile()
import reflex as rx

class State(rx.State):
    name :str = 'Gero'
    
def index():
    return rx.vstack(
        rx.text("Hello World!", color="darkred", font_size="5.5em")
    )
    


app = rx.App()
app.add_page(index)

app.compile()
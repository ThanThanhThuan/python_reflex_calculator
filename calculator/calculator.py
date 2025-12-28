import reflex as rx

# --- STATE (Backend Logic) ---
class CalculatorState(rx.State):
    display: str = "0"
    
    def add_char(self, char: str):
        """Add a number or operator to the display."""
        if self.display == "0" or self.display == "Error":
            self.display = char
        else:
            self.display += char

    def clear(self):
        """Reset the display."""
        self.display = "0"

    def calculate(self):
        """Evaluate the math expression."""
        try:
            # eval() is a quick way to do math on strings in Python
            # e.g., eval("2 + 2") returns 4
            result = eval(self.display)
            self.display = str(result)
        except Exception:
            self.display = "Error"

# --- UI (Frontend) ---
def calculator_button(text: str, on_click, color="gray"):
    """A helper function to create styled buttons."""
    return rx.button(
        text,
        on_click=on_click,
        width="100%",
        height="60px",
        font_size="1.5em",
        variant="solid",
        color_scheme=color,
        border_radius="lg",
    )

def index():
    return rx.center(
        rx.vstack(
            # 1. The Display Screen
            rx.box(
                rx.text(
                    CalculatorState.display,
                    font_size="2.5em",
                    font_family="monospace",
                    text_align="right",
                    width="100%",
                    padding="10px"
                ),
                background_color="#f0f0f0",
                width="100%",
                border_radius="lg",
                margin_bottom="15px",
                border="2px solid #333"
            ),
            
            # 2. The Button Grid
            rx.grid(
                # Row 1
                calculator_button("7", lambda: CalculatorState.add_char("7")),
                calculator_button("8", lambda: CalculatorState.add_char("8")),
                calculator_button("9", lambda: CalculatorState.add_char("9")),
                calculator_button("/", lambda: CalculatorState.add_char("/"), color="orange"),

                # Row 2
                calculator_button("4", lambda: CalculatorState.add_char("4")),
                calculator_button("5", lambda: CalculatorState.add_char("5")),
                calculator_button("6", lambda: CalculatorState.add_char("6")),
                calculator_button("*", lambda: CalculatorState.add_char("*"), color="orange"),

                # Row 3
                calculator_button("1", lambda: CalculatorState.add_char("1")),
                calculator_button("2", lambda: CalculatorState.add_char("2")),
                calculator_button("3", lambda: CalculatorState.add_char("3")),
                calculator_button("-", lambda: CalculatorState.add_char("-"), color="orange"),

                # Row 4
                calculator_button("C", CalculatorState.clear, color="red"),
                calculator_button("0", lambda: CalculatorState.add_char("0")),
                calculator_button("=", CalculatorState.calculate, color="green"),
                calculator_button("+", lambda: CalculatorState.add_char("+"), color="orange"),

                columns="4", # 4 columns grid
                spacing="4", # Gap between buttons
                width="100%",
            ),
            padding="20px",
            background_color="#222",
            border_radius="20px",
            width="350px",
            box_shadow="lg",
        ),
        height="100vh", # Full screen height
        background_color="#111", # Dark background for the page
    )

# --- APP CONFIG ---
app = rx.App()
app.add_page(index)
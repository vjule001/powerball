import random
import tkinter as tk
from typing import List


def generate_power_balls() -> List:
    power_balls: set[int] = set()

    while len(power_balls) != 5:
        power_balls.add(random.randint(1, 69))

    red_ball: int = random.randint(1, 26)
    sorted_power_balls: List[int] = sorted(power_balls)
    sorted_power_balls.append(red_ball)

    return sorted_power_balls


def display_power_balls() -> object:
    def reroll():
        new_power_balls = generate_power_balls()
        for i, ball in enumerate(new_power_balls):
            if i < 5:
                ball_labels[i].config(text=str(ball), bg="white")
            else:
                ball_labels[i].config(text=str(ball), bg="red")

    power_balls = generate_power_balls()

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Power Ball Numbers")

    # Create labels for displaying the numbers
    ball_labels = []
    for i, ball in enumerate(power_balls):
        label = tk.Label(window, text=str(ball), font=("Arial", 16), width=5, height=2, borderwidth=2, relief="ridge")
        if i < 5:
            label.config(bg="white")
        else:
            label.config(bg="red")
        ball_labels.append(label)

    # Arrange labels in a grid
    for i, label in enumerate(ball_labels):
        label.grid(row=0, column=i, padx=5, pady=5)

    # Create a button to reroll the numbers
    reroll_button = tk.Button(window, text="Reroll", font=("Arial", 14), command=reroll)
    reroll_button.grid(row=1, columnspan=len(power_balls), padx=10, pady=10)

    # Run the Tkinter event loop
    window.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_power_balls()
import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Ultimate Number Guessing Game")
        self.root.geometry("450x500")
        self.root.configure(bg="#dacece")
        self.difficulty = tk.StringVar(value="medium")
        self.setup_widgets()
        self.reset_game()

    def setup_widgets(self):
        # Difficulty selection
        difficulty_frame = tk.Frame(self.root, bg="#f2f2f2")
        difficulty_frame.pack(pady=10)
        tk.Label(difficulty_frame, text="Select Difficulty:",
                 font=("Arial", 12), bg="#f2f2f2").pack()
        for level in ["easy", "medium", "hard"]:
            tk.Radiobutton(
                difficulty_frame, text=level.capitalize(), variable=self.difficulty,
                value=level, command=self.reset_game, font=("Arial", 10), bg="#f2f2f2"
            ).pack(anchor="w")

        # Feedback display
        self.feedback_label = tk.Label(
            self.root, text="", font=("Arial", 12), bg="#f2f2f2")
        self.feedback_label.pack(pady=10)

        # Guess input
        input_frame = tk.Frame(self.root, bg="#f2f2f2")
        input_frame.pack()
        self.guess_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.guess_entry.grid(row=0, column=0, padx=5)
        self.guess_entry.bind("<Return>", lambda e: self.check_guess())
        self.submit_btn = tk.Button(
            input_frame, text="🎯 Guess", command=self.check_guess, font=("Arial", 10))
        self.submit_btn.grid(row=0, column=1)

        # Status display
        self.status_label = tk.Label(
            self.root, text="", font=("Arial", 11), bg="#f2f2f2")
        self.status_label.pack(pady=10)

        # Guess history
        tk.Label(self.root, text="Your Previous Guesses:",
                 font=("Arial", 11), bg="#f2f2f2").pack()
        self.history_box = tk.Text(self.root, height=8, width=30, font=(
            "Arial", 10), state="disabled", bg="#ffffff")
        self.history_box.pack(pady=5)

        # Reset button
        self.reset_btn = tk.Button(
            self.root, text="🔄 Reset Game", command=self.reset_game, font=("Arial", 10))
        self.reset_btn.pack(pady=10)

    def reset_game(self):
        attempts_map = {"easy": 10, "medium": 7, "hard": 5}
        self.attempts_allowed = attempts_map[self.difficulty.get()]
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.score = 100
        self.guess_history = []
        self.feedback_label.config(
            text="I'm thinking of a number between 1 and 100...")
        self.status_label.config(
            text=f"Attempts Left: {self.attempts_allowed} | Score: {self.score}")
        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", tk.END)
        self.history_box.configure(state="disabled")
        self.guess_entry.delete(0, tk.END)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="⚠️ Not a number. Try again.")
            return

        self.attempts += 1
        self.guess_entry.delete(0, tk.END)
        self.guess_history.append(guess)

        # Update history display
        self.history_box.configure(state="normal")
        self.history_box.insert(tk.END, f"Attempt {self.attempts}: {guess}\n")
        self.history_box.configure(state="disabled")

        if guess < self.number_to_guess:
            self.feedback_label.config(text="📉 Too low!")
            self.score -= 10
        elif guess > self.number_to_guess:
            self.feedback_label.config(text="📈 Too high!")
            self.score -= 10
        else:
            self.feedback_label.config(
                text=f"🏆 You nailed it in {self.attempts} attempts! Final Score: {self.score}"
            )
            self.status_label.config(text="🎉 Game Over")
            return

        if self.attempts >= self.attempts_allowed:
            self.feedback_label.config(
                text=f"❌ No attempts left. Number was {self.number_to_guess}.")
            self.status_label.config(text="💀 Game Over")
        else:
            self.status_label.config(
                text=f"Attempts Left: {self.attempts_allowed - self.attempts} | Score: {self.score}"
            )


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

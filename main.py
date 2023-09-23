import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import time
from ttkbootstrap import Style
import math
# Dictionary of European countries and their capitals in English
european_countries_en = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg City",
    "Malta": "Valletta",
    "Netherlands": "Amsterdam",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "United Kingdom": "London",
    "Liechtenstein": "Vaduz",
    "Vatican City": "Vatican City",
    "Monaco": "Monaco",
    "San Marino": "San Marino",
    "Montenegro": "Podgorica",
    "North Macedonia": "Skopje",
    "Serbia": "Belgrade",
    "Bosnia and Herzegovina": "Sarajevo",
    "Kosovo": "Pristina",
    "Turkey": "Ankara",
    "Russia": "Moscow",
    "Ukraine": "Kyiv",
    "Belarus": "Minsk",
}

# Dictionary of European countries and their capitals in Polish
european_countries_pl = {
    "Albania": "Tirana",
    "Andora": "Andora la Vella",
    "Austria": "Wiedeń",
    "Belgia": "Bruksela",
    "Bułgaria": "Sofia",
    "Chorwacja": "Zagrzeb",
    "Cypr": "Nikozja",
    "Republika Czeska": "Praga",
    "Dania": "Kopenhaga",
    "Estonia": "Tallinn",
    "Finlandia": "Helsinki",
    "Francja": "Paryż",
    "Niemcy": "Berlin",
    "Grecja": "Ateny",
    "Węgry": "Budapeszt",
    "Islandia": "Reykjavik",
    "Irlandia": "Dublin",
    "Włochy": "Rzym",
    "Łotwa": "Ryga",
    "Litwa": "Wilno",
    "Luksemburg": "Luksemburg",
    "Malta": "Valletta",
    "Holandia": "Amsterdam",
    "Norwegia": "Oslo",
    "Polska": "Warszawa",
    "Portugalia": "Lizbona",
    "Rumunia": "Bukareszt",
    "Słowacja": "Bratysława",
    "Słowenia": "Lublana",
    "Hiszpania": "Madryt",
    "Szwecja": "Sztokholm",
    "Szwajcaria": "Berno",
    "Wielka Brytania": "Londyn",
    "Liechtenstein": "Vaduz",
    "Watykan": "Watykan",
    "Monako": "Monako",
    "San Marino": "San Marino",
    "Czarnogóra": "Podgorica",
    "Macedonia Północna": "Skopje",
    "Serbia": "Belgrad",
    "Bośnia i Hercegowina": "Sarajewo",
    "Kosowo": "Pristina",
    "Turcja": "Ankara",
    "Rosja": "Moskwa",
    "Ukraina": "Kijów",
    "Białoruś": "Mińsk",
}


class CapitalsQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Capitals Quiz")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)

        # Create a ttkbootstrap style
        self.style = Style(theme="darkly")  # Choose a Bootstrap theme

        title_frame = ttk.Frame(root)
        title_frame.pack(pady=10)
        self.title_label = ttk.Label(title_frame, text="European Capitals Quiz", font=("Helvetica", 18))
        self.title_label.pack()

        lang_frame = ttk.Frame(root)
        lang_frame.pack(pady=10)
        self.language_label = ttk.Label(lang_frame, text="Select language:")
        self.language_label.pack()

        self.language_var = tk.StringVar()
        self.language_var.set("english")

        self.english_radio = ttk.Radiobutton(lang_frame, text="English", variable=self.language_var, value="english")
        self.polish_radio = ttk.Radiobutton(lang_frame, text="Polish", variable=self.language_var, value="polish")

        self.english_radio.pack(side=tk.LEFT, padx=10)
        self.polish_radio.pack(side=tk.LEFT, padx=10)

        self.start_button = ttk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.quit_button = ttk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def start_quiz(self):
        selected_language = self.language_var.get()
        european_countries = european_countries_en if selected_language == "english" else european_countries_pl

        # Shuffle the order of the countries to make it more random
        countries = list(european_countries.keys())
        random.shuffle(countries)

        # Initialize variables for scoring
        correct_answers = 0
        total_points = 0

        # Disable the main window while the quiz is active
        self.root.grab_set()

        for country in countries:
            capital = european_countries[country]
            start_time = time.time()
            user_guess = simpledialog.askstring("Capital Quiz", f"What is the capital of {country}?")

            if user_guess is not None:
                end_time = time.time()
                response_time = end_time - start_time


                if response_time > 0:
                    points = int(1000 - (response_time * (100/math.pi)*math.e))
                    if points < 200:
                        points = 200
                else:
                    points = 1000

                if user_guess.lower() == capital.lower():
                    messagebox.showinfo("Correct!", f"Correct! Well done. You earned {points} points.")
                    correct_answers += 1
                    total_points += points
                else:
                    messagebox.showinfo("Incorrect",
                                        f"Sorry, the capital of {country} is {capital}. You earned 0 points.")

        # Re-enable the main window
        self.root.grab_release()

        # Print the final score
        messagebox.showinfo("Quiz Result", f"You got {correct_answers} out of {len(countries)} capitals correct."
                                           f"\nTotal Points: {total_points}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CapitalsQuizApp(root)
    root.mainloop()
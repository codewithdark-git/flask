from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.secret_key = 'codewithdark'  # Needed for session management

def initialize_game():
    session['random_number'] = random.randint(0, 9)
    session['attempts'] = 0

@app.route('/')
def home():
    if 'random_number' not in session:
        initialize_game()
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess_number():
    if 'random_number' not in session:
        initialize_game()

    session['attempts'] += 1
    name = request.form["name"]
    guess = int(request.form["guess"])
    if guess > session['random_number']:
        result_message =  f"Hi {name}, {guess} is too high, try again!"
    elif guess < session['random_number']:
        result_message =  f"Hi {name}, {guess} is too Low, try again!"
    else:
        result_message = f"Congratulations {name}, you found the number {session['random_number']} in {session['attempts']} attempts!"
        initialize_game()  # Reset the game after a correct guess
    return render_template("index.html", result_message=result_message, attempts=session['attempts'])

if __name__ == "__main__":
    app.run(debug=True)

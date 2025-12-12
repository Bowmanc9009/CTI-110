from flask import Flask, render_template, request
import random
import time

#create a flask app project
app = Flask(__name__)

# Create route for index.html
@app.route("/",methods=["GET","POST"])
def hello_friend():
    name = "Charles"
    #pull values from form
    return render_template("index.html", friendname=name)
@app.route("/submit",methods=["GET","POST"])
def results():
    if request.method == "POST":
        player_name = request.form.get('player_name')
        favorite_color = request.form.get('favorite_color')
        player_health = request.form.get('player_health')
        
    #convert health to int
        player_health = int(player_health)
        
        print(f"Player Name: {player_name}") 
        print(f"Favorite Color: {favorite_color}")
        print(f"Player Health: {player_health}")
    return render_template(
        "results.html",
        player_name=player_name,
        favorite_color=favorite_color,
        player_health=player_health
    )
@app.route("/left",methods = ["POST"])
def left_page():
    player_health = request.form.get("player_health")

    try:
        player_health = int(player_health)
    except (ValueError, TypeError):
        player_health = 0

    player_health = max(0, player_health - 3)

    return render_template("left.html", player_health=player_health)
# run app
if __name__ == "__main__":
    app.run(debug= True)
@app.route("/right", methods=["POST"])
def right_page():
    player_health = request.form.get("player_health")
    inventory = request.form.get("inventory")

    # Ensure health is integer
    try:
        player_health = int(player_health)
    except (ValueError, TypeError):
        player_health = 0

    # Make sure inventory exists
    if not inventory:
        inventory = ""

    # Add an apple to inventory
    if inventory == "":
        inventory = "apple"
    else:
        inventory += ", apple"

    return render_template("right.html",player_health=player_health,inventory=inventory)
@app.route("/sleep")
def sleep_page():
    # simulate resting delay
    time.sleep(2)

    # example sleep effect
    message = "You fall asleep... When you wake up, you feel rested."

    # maybe even restore health or do something else
    restored_amount = 5

    return render_template("sleep.html",message=message,restored_amount=restored_amount)
@app.route("/mystery_page")
def mystery_page():
    event = random.choice(["a glowing orb", "a shadowy figure", "a hidden treasure", "a strange whisper"])

    message = f"You encounter {event}."

    return render_template("mystery.html",message=message)
@app.route("/fight", methods=["POST"])
def fight():
    inventory = request.form.get("inventory", "")
    player_health = int(request.form.get("player_health", 30))
    bear_health = int(request.form.get("bear_health", 20))
    action = request.form.get("action", None)

    message = ""

    # --- ACTION LOGIC ---
    if action == "apple":
        message = "You throw an apple! The bear is stunned and cannot attack!"
        bear_health -= 5

    elif action == "gold":
        message = "You toss gold on the ground... The bear becomes distracted and wanders away!"
        bear_health = 0

    elif action == "attack":
        message = "You strike the bear!"
        bear_health -= random.randint(3, 7)

        if bear_health > 0:
            dmg = random.randint(2, 6)
            player_health -= dmg
            message += f" The bear claws you for {dmg} damage!"

    else:
        message = "A huge bear jumps out of the bushes! Prepare to fight!"

    # Prevent negative numbers
    if bear_health < 0:
        bear_health = 0
    if player_health < 0:
        player_health = 0

    # --- ENDING CONDITIONS ---
    if bear_health == 0 and player_health > 0:
        return render_template(
            "ending.html",
            ending_message="You have slain the bear and survived your journey!"
        )

    if player_health == 0:
        return render_template(
            "ending.html",
            ending_message="The bear overpowers you... and darkness consumes your vision."
        )

    # If no ending yet → continue the fight
    return render_template(
        "fight.html",
        inventory=inventory,
        player_health=player_health,
        bear_health=bear_health,
        message=message
    )


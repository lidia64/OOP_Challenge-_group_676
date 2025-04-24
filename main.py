# main.py

from pet import Pet

# Helper functions for formatting
def underline(text):
    return f"\033[4m{text}\033[0m"

def bold(text):
    return f"\033[1m{text}\033[0m"

def color(text):
    return f"\033[35m{text}\033[0m"  # Pink color (ANSI code 35)

# Create a pet named Bubbles (type: Fish 🐟)
my_pet = Pet("Bubbles", pet_type="Fish 🐟")

# Introduce the pet
print(color(bold(underline("🐾 Welcome to the Pet Simulator! 🐾"))))
print(f"{bold('Meet your pet:')} {color(my_pet.name)} the {color(my_pet.pet_type)}")

# Try different actions
print("\n" + color(underline("🎬 Actions:")))
my_pet.eat(food="fish flakes 🥣")
my_pet.play(activity="swimming through a hoop 🎯")
my_pet.sleep(duration=4)  # Sleep for 4 hours 💤
my_pet.train("blow bubbles 💨")
my_pet.train("swim in circles 🔄")

# Show status and tricks
print("\n" + color(underline("📊 Pet Status:")))
my_pet.get_status()

print("\n" + color(underline("🎓 Tricks Learned:")))
my_pet.show_tricks()

# Add a goodbye message
print("\n" + color(bold(f"{my_pet.name} the {my_pet.pet_type} swims away gracefully! 🌊")))
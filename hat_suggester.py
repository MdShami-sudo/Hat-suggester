import random

def suggest_random_hat():
    hats = [
        "Baseball Cap",
        "Cowboy Hat",
        "Fedora",
        "Beanie",
        "Top Hat",
        "Bucket Hat",
        "Sun Hat",
        "Beret",
        "Panama Hat",
        "Visor",
        "Sombrero",
        "Fez",
        "Trilby",
        "Boater Hat",
        "Newsboy Cap"
    ]
    
    return random.choice(hats)

# Suggest a random hat
print("Today's random hat suggestion is:", suggest_random_hat())

import random

# --------------------------- DATA --------------------------- #

data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 650,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 505,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 420,
        "description": "Singer and Actress",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 398,
        "description": "Businesswoman and TV Personality",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 396,
        "description": "Actor and Wrestler",
        "country": "United States"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 275,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 305,
        "description": "Singer and Songwriter",
        "country": "United States"
    },
    {
        "name": "Narendra Modi",
        "follower_count": 105,
        "description": "Prime Minister",
        "country": "India"
    },
    {
        "name": "MrBeast",
        "follower_count": 120,
        "description": "YouTuber",
        "country": "United States"
    },
    {
        "name": "Bill Gates",
        "follower_count": 38,
        "description": "Entrepreneur and Philanthropist",
        "country": "United States"
    },
    {
        "name": "Elon Musk",
        "follower_count": 240,
        "description": "Entrepreneur",
        "country": "United States"
    },
    {
        "name": "Priyanka Chopra",
        "follower_count": 92,
        "description": "Actress",
        "country": "India"
    },
    {
        "name": "Shah Rukh Khan",
        "follower_count": 48,
        "description": "Actor",
        "country": "India"
    },
    {
        "name": "Zendaya",
        "follower_count": 185,
        "description": "Actress and Singer",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 360,
        "description": "Media Personality",
        "country": "United States"
    }
]


# --------------------------- FUNCTIONS --------------------------- #

def get_random_person():
    """Return a random person."""
    return random.choice(data)


def format_data(person):
    """Return formatted details of a person."""
    return f"{person['name']}, a {person['description']}, from {person['country']}"


# --------------------------- GAME SETUP --------------------------- #

score = 0
game_over = False

personA = get_random_person()
personB = get_random_person()

# Ensure both persons are different
while personA == personB:
    personB = get_random_person()


# --------------------------- GAME LOOP --------------------------- #

while not game_over:

    print("\n----------------------------------------")
    print(f"Compare A: {format_data(personA)}")
    print("VS")
    print(f"Against B: {format_data(personB)}")

    user_choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    # Determine the winner
    if personA["follower_count"] > personB["follower_count"]:
        correct_answer = "A"
        winner = personA
    else:
        correct_answer = "B"
        winner = personB

    # Check user's answer
    if user_choice == correct_answer:

        score += 1
        print(f"\n✅ Correct! Current Score: {score}")

        # Winner stays for next round
        personA = winner

        # Generate a new opponent
        personB = get_random_person()

        while personA == personB:
            personB = get_random_person()

    else:
        print("\n❌ Wrong Guess!")
        print(f"Final Score: {score}")
        game_over = True
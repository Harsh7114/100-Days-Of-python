import random


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def cal_score(cards):
    """Calculate the score of a hand."""

    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace from 11 to 1 if score goes over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):

    if user_score == computer_score:
        return "🤝 Draw"

    elif user_score == 0:
        return "🎉 You win with a Blackjack!"

    elif computer_score == 0:
        return "💻 Computer wins with a Blackjack!"

    elif user_score > 21:
        return "💥 You went over. You lose."

    elif computer_score > 21:
        return "🎉 Computer went over. You win!"

    elif user_score > computer_score:
        return "🎉 You win!"

    else:
        return "💻 Computer wins!"


# ---------------- MAIN PROGRAM ---------------- #

user_card = []
computer_card = []

is_game_over = False

# Deal two cards each
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


# Player's turn
while not is_game_over:

    score_user = cal_score(user_card)
    score_comp = cal_score(computer_card)

    print(f"\nYour cards: {user_card}, current score: {score_user}")
    print(f"Computer's first card: {computer_card[0]}")

    if score_user == 0 or score_comp == 0 or score_user > 21:
        is_game_over = True

    else:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if choice == "y":
            user_card.append(deal_card())
        else:
            is_game_over = True


# Computer's turn
score_comp = cal_score(computer_card)

while score_comp != 0 and score_comp < 17:
    computer_card.append(deal_card())
    score_comp = cal_score(computer_card)


# Final Scores
score_user = cal_score(user_card)

print("\n========== FINAL RESULT ==========")
print(f"Your final hand: {user_card}, final score: {score_user}")
print(f"Computer's final hand: {computer_card}, final score: {score_comp}")

print(compare(score_user, score_comp))
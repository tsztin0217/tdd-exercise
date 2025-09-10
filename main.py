VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    hypothetical_score = 0
    score = 0
    for card in hand:
        if card in ['Jack', 'Queen', 'King']:
            hypothetical_score += 10
            score += 10
        elif card == 'Ace':
            hypothetical_score += 11
            if hypothetical_score <= 21:
                score += 11
            else:
                score += 1
        else:
            hypothetical_score += card
            score += card

    return score
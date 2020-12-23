from functools import reduce
from collections import defaultdict
import sys
file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(file, 'r') as f:
    decks = [ line.strip() for line in f.read().split('\n\n') ]

# convert all str numbers to ints, and reverse the list to be like an actually deck of cards (a stack)
deck1 = [int(card) for card in decks[0].split('\n')[1:][::-1]]
deck2 = [int(card) for card in decks[1].split('\n')[1:][::-1]]

def part1(player1_deck, player2_deck):
    passes = 0
    # fight!
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        card1 = player1_deck.pop()
        card2 = player2_deck.pop()

        cards = [card1, card2]
        # put cards at the bottom of the winning player's deck with the losing player's card at the bottom
        if card1 > card2:
            player1_deck = cards[::-1] + player1_deck
        else: # player1 loses
            player2_deck = cards + player2_deck
        passes += 1

    # print('Number of passes', passes)
    deck = player1_deck if len(player1_deck) > 0 else player2_deck
    return sum([(index + 1) * card for index, card in enumerate(deck)])

# def is_same_round_played(previous_cards, p1, p2):
#     if len(p1) != len(p2):
#         return False
#     if len(previous_cards) == 0:
#         return False
#
#     for index, j in enumerate(previous_cards):
#         print(j[0] == p1 and j[1] == p2)
#         if j[0] == p1 and j[1] == p2:
#             return True
#     return False


def part2(player1_deck, player2_deck):
    passes = 0
    previous_rounds = set()
    # fight!
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        passes += 1
        if (round := (tuple(player1_deck), tuple(player2_deck))) in previous_rounds:
            return { 'player': 'p1', 'deck': player1_deck }
        previous_rounds.add(round)

        card1 = player1_deck.pop()
        card2 = player2_deck.pop()
        cards = [card2, card1]
        if len(player1_deck) >= card1 and len(player2_deck) >= card2:
            winner = part2(player1_deck[len(player1_deck) - card1:], player2_deck[len(player2_deck) - card2:])
            if winner['player'] == 'p1':
                player1_deck = cards + player1_deck
            else:
                player2_deck = cards[::-1] + player2_deck
        else:
            if card1 > card2:
                player1_deck = [card2, card1] + player1_deck
            else:
                player2_deck = [card1, card2] + player2_deck
        passes += 1
    return { 'player': 'p1', 'deck': player1_deck } if len(player1_deck) > 0 \
        else { 'player': 'p2', 'deck': player2_deck }

deck1_copy = deck1.copy()
deck2_copy = deck2.copy()
print('Part 1:', part1(deck1, deck2))

part2_winner = part2(deck1_copy, deck2_copy)
print('Part 2:', sum([(index + 1) * card for index, card in enumerate(part2_winner['deck'])]))

start_deck = input().split()
shuffles = int(input())

new_deck = []

for shuffle in range(shuffles):
    left_half = start_deck[:(int(len(start_deck) / 2))]
    right_half = start_deck[(int(len(start_deck) / 2)):]
    for card in range(len(left_half)):
        new_deck.append(left_half[card])
        new_deck.append(right_half[card])
    start_deck = new_deck
    new_deck = []
new_deck = start_deck
print(new_deck)



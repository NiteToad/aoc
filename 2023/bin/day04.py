"""
[[ Day 04: Scratchcars ]]

Example Data:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

Part 1:
In the above example, card 1 has five winning numbers
(41, 48, 83, 86, and 17) and eight numbers you have
(83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have,
four of them (48, 83, 17, and 86) are winning numbers!
That means card 1 is worth 8 points (1 for the first match,
then doubled three times for each of the three matches after the first).

Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
Card 4 has one winning number (84), so it is worth 1 point.
Card 5 has no winning numbers, so it is worth no points.
Card 6 has no winning numbers, so it is worth no points.

Take a seat in the large pile of colorful cards.
How many points are they worth in total?

Answer: 13 points

Part 2:
Card 1 has four matching numbers, so you win one copy each of the next
four cards: cards 2, 3, 4, and 5.
Your original card 2 has two matching numbers, so you win one copy each
of cards 3 and 4.
Your copy of card 2 also wins one copy each of cards 3 and 4.
Your four instances of card 3 (one original and three copies) have two
matching numbers, so you win four copies each of cards 4 and 5.
Your eight instances of card 4 (one original and seven copies) have one
matching number, so you win eight copies of card 5.
Your fourteen instances of card 5 (one original and thirteen copies)
have no matching numbers and win no more cards.
Your one instance of card 6 (one original) has no matching numbers and
wins no more cards.

Once all of the originals and copies have been processed, you end up
with 1 instance of card 1, 2 instances of card 2, 4 instances of card
3, 8 instances of card 4, 14 instances of card 5, and 1 instance of
card 6. In total, this example pile of scratchcards causes you to
ultimately have 30 scratchcards!

Process all of the original and copied scratchcards until no more
scratchcards are won. Including the original set of scratchcards,
how many total scratchcards do you end up with?

Answer: 30 scratchcards

"""
from sys import argv

sample_data = [
    ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"],
    ["Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"],
    ["Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"],
    ["Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"],
    ["Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"],
    ["Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"],
]

matched_numbers = []
TOTAL = 0

with open(argv[1], encoding="utf-8") as file:
    lines = file.readlines()
    for card in lines:
        # Split card into left and right
        split_card = card.split("|")

        # Winning numbers
        left_numbers = split_card[0].split(":")[1].split()

        # Your numbers
        right_numbers = split_card[1].split()

        # Find matching numbers
        matching_numbers = len(set(left_numbers) & set(right_numbers))

        if matching_numbers > 0:
            # Calculate points
            TOTAL += 2 ** (matching_numbers - 1)


print(f"Scratchcard points: {TOTAL}")

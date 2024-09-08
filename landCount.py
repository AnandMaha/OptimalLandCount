import math

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

# Problem: What's the minimum number of lands I should put into my deck in order to have an acceptable number
#   of lands based on the average mana cost 
# Solution: By turn {mana cost}, have a {guarantee chance} to have ATLEAST {mana cost} lands.
#   Also, +2 because I would be happy with a particular range of lands not literally the 1 outcome, and I wouldn't want infinite lands either.
def land_count(m):
    lands = 0
    deck_size = 60
    init_hand_size = 7 # baseline of cards for adding cards to per turn
    min_chance = 0.9 # willingness probability to have the desired mana lands on that turn; higher chance -> more lands needed, vice versa.
    land_range = 2
    cards_seen = init_hand_size + m - 1
    prev_chance = 0

    while True: # lands will always increase as long as computation is < min_chance
        # implement the +2 range
        calc = 0
        spells = deck_size - lands
        for i in range(m, m + land_range + 1):
            calc += math.comb(lands, i) * math.comb(spells, cards_seen - i) / math.comb(deck_size, cards_seen) 

        if calc >= min_chance or prev_chance > calc:
            return lands, calc, cards_seen # the minimum lands required reached based on constraints
        else:
            lands += 1
            prev_chance = calc

average_mana = 2.0
round_mana = normal_round(average_mana)
lnd_cnt, chance, cards_seen = land_count(round_mana)
chance = round(chance * 100)
print(f"With a deck of average mana of {average_mana}, the minimum optimal amount of lands required to have a {chance}% chance of getting {round_mana}-{round_mana+2} lands by turn {round_mana} having seen {cards_seen} cards is {lnd_cnt}.")
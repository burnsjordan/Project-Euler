class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def card_value(c):
    return c.value

class Hand:
    def __init__(self, c1, c2, c3, c4, c5):
        self.cards = []
        self.cards.append(c1)
        self.cards.append(c2)
        self.cards.append(c3)
        self.cards.append(c4)
        self.cards.append(c5)
        self.cards.sort(key= card_value)

def is_combo(hand, combo):
    m = 0
    for i in range(5):
        count = 1
        for j in range(i+1, 5):
            if(hand.cards[i].value == hand.cards[j].value and i != j):
                count += 1
        if(count > m):
            m = count
    if(m == combo):
        return True
    else:
        return False

def is_straight(hand):
    if(hand.cards[1].value != hand.cards[0].value+1):
        return False
    elif(hand.cards[2].value != hand.cards[0].value+2):
        return False
    elif(hand.cards[3].value != hand.cards[0].value+3):
        return False
    elif(hand.cards[4].value != hand.cards[0].value+4):
        return False
    return True

def is_flush(hand):
    suit = hand.cards[0].suit
    for i in hand.cards:
        if(i.suit != suit):
            return False
    return True

def is_tp(hand):
    m = 0
    mm = 0
    for i in range(5):
        count = 1
        for j in range(i+1, 5):
            if(hand.cards[i].value == hand.cards[j].value and i != j):
                count += 1
        if(count > m):
            mm = m
            m = count
        elif(count > mm):
            mm = count
    if(m == 2 and mm == 2):
        return True
    else:
        return False

def is_full_house(hand):
    m = 0
    mm = 0
    used_cards = []
    for i in range(5):
        count = 1
        for j in range(i+1, 5):
            if(hand.cards[i].value == hand.cards[j].value and i != j):
                count += 1
        if(count > m and not used_cards.__contains__(hand.cards[i].value)):
            mm = m
            m = count
            used_cards.append(hand.cards[i].value)
        elif(count > mm and not used_cards.__contains__(hand.cards[i].value)):
            mm = count
            used_cards.append(hand.cards[i].value)
    if(m == 3 and mm == 2):
        return True
    else:
        return False

def is_sf(hand):
    if(is_flush(hand) and is_straight(hand)):
        return True

def is_r(hand):
    if(is_sf(hand) and hand.cards[0].value == 10):
        return True
    else:
        return False

def combo_breaker(hand):
    m = 0
    m_card = 0
    for i in range(5):
        count = 1
        for j in range(i+1, 5):
            if(hand.cards[i].value == hand.cards[j].value and i != j):
                count += 1
        if(count > m):
            m = count
            m_card = i
    if(m <= 1):
        vals = []
        for i in hand.cards:
            vals.append(i.value)
        return max(vals)
    return hand.cards[m_card].value

# TODO - this is broken in the one case it happens in 54 it returns 1 when it should return 2
# It's broken because the hands are sorted by card value only
def combo_tie_breaker(hand1, hand2, combo):
    for i in range(5-combo, -1, -1):
        if(hand1.cards[i].value > hand2.cards[i].value):
            return 1
        elif(hand2.cards[i].value > hand1.cards[i].value):
            return 2

def double_combo_breaker(hand):
    m = 0
    mm = 0
    m_card = 0
    mm_card = 0
    for i in range(5):
        count = 1
        for j in range(i+1, 5):
            if(hand.cards[i].value == hand.cards[j].value and i != j):
                count += 1
        if(count > m):
            mm_card = m_card
            mm = m
            m = count
            m_card = i
        elif(count > mm):
            mm_card = i
            mm = count
    return hand.cards[mm_card].value

def get_rank(hand):
    if(is_r(hand)):
        return 10
    elif(is_sf(hand)):
        return 9
    elif(is_combo(hand, 4)):
        return 8
    elif(is_full_house(hand)):
        return 7
    elif(is_flush(hand)):
        return 6
    elif(is_straight(hand)):
        return 5
    elif(is_combo(hand, 3)):
        return 4
    elif(is_tp(hand)):
        return 3
    elif(is_combo(hand, 2)):
        return 2
    else:
        return 1

def tiebraker(hand1, hand2, rank):
    if(rank == 1 or rank == 5 or rank == 6 or rank == 9 or rank == 10):
        if(hand1.cards[4].value > hand2.cards[4].value):
            return 1
        elif(hand2.cards[4].value > hand1.cards[4].value):
            return 2
        else:
            if(hand1.cards[3].value > hand2.cards[3].value):
                return 1
            elif(hand2.cards[3].value > hand1.cards[3].value):
                return 2 
            else:
                if(hand1.cards[2].value > hand2.cards[2].value):
                    return 1
                elif(hand2.cards[2].value > hand1.cards[2].value):
                    return 2 
                else:
                    if(hand1.cards[1].value > hand2.cards[1].value):
                        return 1
                    elif(hand2.cards[1].value > hand1.cards[1].value):
                        return 2 
                    else:
                        if(hand1.cards[0].value > hand2.cards[0].value):
                            return 1
                        elif(hand2.cards[0].value > hand1.cards[0].value):
                            return 2 
                        else:
                            return 0
    elif(rank == 2 or rank == 4 or rank == 8 or rank == 3 or rank == 7):
        if(combo_breaker(hand1) > combo_breaker(hand2)):
            return 1
        elif(combo_breaker(hand2) > combo_breaker(hand1)):
            return 2
        elif(rank == 2):
            return combo_tie_breaker(hand1, hand2, 2)
        elif(rank == 4):
            return combo_tie_breaker(hand1, hand2, 3)
        elif(rank == 8):
            return combo_tie_breaker(hand1, hand2, 4)
        else:
            if(double_combo_breaker(hand1) > double_combo_breaker(hand2)):
                return 1
            elif(double_combo_breaker(hand2) > double_combo_breaker(hand1)):
                return 2
            elif(rank == 3):
                return combo_tie_breaker(hand1, hand2, 4)
            else:
                return 0
    else:
        return 0



def winner(hand1, hand2):
    if(get_rank(hand1) > get_rank(hand2)):
        return 1
    elif(get_rank(hand2) > get_rank(hand1)):
        return 2
    else:
        return tiebraker(hand1, hand2, get_rank(hand1))

def create_card(v, s):
    if(v.isdigit()):
        return Card(int(v), s)
    else:
        if(v == 'T'):
            return Card(10, s)
        elif(v == 'J'):
            return Card(11, s)
        elif(v == 'Q'):
            return Card(12, s)
        elif(v == 'K'):
            return Card(13, s)
        else:
            return Card(14, s)

with open('51-75/54.txt') as f:
    lines = [line.rstrip() for line in f]

count = 0
for i in lines:
    temp = i.split(' ')
    h1 = []
    h2 = []
    for j in range(len(temp)):
        if(j < 5):
            h1.append(create_card(temp[j][0], temp[j][1]))
        else:
            h2.append(create_card(temp[j][0], temp[j][1]))
    hand1 = Hand(h1[0], h1[1], h1[2], h1[3], h1[4])
    hand2 = Hand(h2[0], h2[1], h2[2], h2[3], h2[4])
    if(winner(hand1, hand2) == 1):
        count += 1

print(count)

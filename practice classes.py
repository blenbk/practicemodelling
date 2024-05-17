import random


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    def __gt__(self, other):
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __eq__(self, other):
        return self.rank == other.rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self._cards)


class Hand:
    def __init__(self, deck):
        self._cards = [deck.cards[i] for i in range(5)]

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        return all(card.suit == suit for card in self._cards)

    @property
    def is_pair(self):
        ranks = [card.rank for card in self._cards]
        return any(ranks.count(rank) == 2 for rank in ranks)

    @property
    def is_3_kind(self):
        ranks = [card.rank for card in self._cards]
        return any(ranks.count(rank) == 3 for rank in ranks)

    @property
    def is_4_kind(self):
        ranks = [card.rank for card in self._cards]
        return any(ranks.count(rank) == 4 for rank in ranks)

    @property
    def is_full_house(self):
        return self.is_3_kind and self.is_pair

    @property
    def is_2_pair(self):
        ranks = [card.rank for card in self._cards]
        return len(set(rank for rank in ranks if ranks.count(rank) == 2)) == 2

    def sort_hand(self):
        self._cards.sort(key=lambda card: Card.RANKS.index(card.rank))

    @property
    def is_straight(self):
        ranks = [card.rank for card in self._cards]
        ranks.sort(key=lambda rank: Card.RANKS.index(rank))
        return ranks[-1] == Card.RANKS[Card.RANKS.index(ranks[0]) + 4]

precision = tries =  10
i = 0
while True:
    i = i+1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_straight:
        tries -= 1

    if tries==0:
        break

probability = precision/i * 100
print(f"The odds of getting a flush are {probability}%")


# Create a deck and shuffle it
d = Deck()
d.shuffle()

# Create a hand
hand = Hand(d)

# Sort the hand
hand.sort_hand()

# Print the sorted hand
print(hand)

# Print whether the hand is a straight
print(f"Is straight: {hand.is_straight}")
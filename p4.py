class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    @classmethod
    def create_shuffled_deck(cls):
        """
        Create a new shuffled deck of cards.

        This class method creates a new instance of the Deck class with cards arranged
        in a random order. It shuffles the cards and returns the shuffled deck.

        Returns:
        Deck: A shuffled deck of cards.
        """
        deck = cls()
        deck.shuffle()
        return deck

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)
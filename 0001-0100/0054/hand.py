from card import Card
from exceptions import (
    NonUniqueCardInHandError,
    InvalidTieBreakError,
)


class Hand:
    # types of hands
    ROYAL_FLUSH = 100
    STRAIGHT_FLUSH = 90
    FLUSH = 80
    STRAIGHT = 70
    FOUR_OF_A_KIND = 60
    FULL_HOUSE = 50
    THREE_OF_A_KIND = 40
    TWO_PAIR = 30
    PAIR = 20
    MEH = 10  # nothing exciting

    # results of comparing hands
    WIN = 1
    LOSS = 2
    TIE = 3

    @staticmethod
    def from_string(_string):
        return Hand(*[Card.from_string(substring) for substring in _string.split()])

    def __init__(self, card1, card2, card3, card4, card5):
        """A Hand is a collection of five cards."""
        self.cards = {card1, card2, card3, card4, card5}
        if len(self.cards) < 5:
            raise NonUniqueCardInHandError

        self._cache_expensive_helpers()

    def __iter__(self):
        return (c for c in self.cards)

    def __eq__(self, other_hand):
        self_hashes = {hash(c) for c in self}
        other_hashes = {hash(c) for c in other_hand}
        for h in self_hashes:
            if not h in other_hashes:
                return False
        return True

    def _cache_expensive_helpers(self):
        """Extracts important information based on the cards in this
        hand and caches the information for future use.

        The Information Includes:
        _sorted_rank_string:
            a string of the ranks in this hand in descending order.
        _rank_histogram:
            a frequency histogram for the ranks of the cards in
            this hand.
        _sorted_rank_count_tuple:
            a (rank, count) tuple sorted by increasing
            count of rank, then (ties in count are broken) by
            increasing weight of rank.
        """
        self._sorted_rank_string = "".join(
            sorted(
                (card.rank for card in self),
                key=(lambda r: Card.RANK_WEIGHT_MAP[r]),
                reverse=True,
            )
        )

        self._rank_histogram = {}
        for rank in self._sorted_rank_string:
            self._rank_histogram[rank] = self._rank_histogram.get(rank, 0) + 1

        self._sorted_rank_count_tuple = list(
            sorted(
                self._rank_histogram.items(),
                key=lambda t: (-t[1], -Card.RANK_WEIGHT_MAP[t[0]]),
            )
        )
        # self._sorted_rank_count_tuple = list(reversed(sorted(self._rank_histogram.items(), key=lambda t: (t[1], Card.RANK_WEIGHT_MAP[t[0]]))))

    def is_royal_flush(self):
        """Returns whether this hand of cards is a royal flush.

        A royal flush is a run of five cards of the same suite, which
        are of increasing rank starting from 10 to ACE.
        """
        return self._sorted_rank_string == "AKQJT" and self.is_flush()

    def is_straight_flush(self):
        """Returns whether this hand of cards is a straight flush.

        A straight flush is a run of five cards of the
        same suite, which are of increasing rank.
        """
        return self.is_flush() and self.is_straight()

    def is_flush(self):
        """Returns whether this hand of cards is a flush.

        A flush is a run of five cards of the same suite.
        """
        return len({card.suit for card in self}) == 1

    def is_straight(self):
        """Returns whether this hand of cards is a straight.

        A straight is a run of five cards of increasing ranks. For
        the purposes of finding a straight, an ACE may precede
        a 2 and may follow up a KING.
        """
        _string = self._sorted_rank_string
        # if there is an ACE and a 2
        # then a straight can no longer contain a KING
        # we therefore let the ACE precede the 2 in such a case
        # so we don't miss a possible straight containing a 2
        if _string[0] == "A" and _string[-1] == "2":
            _string = f"{_string[1:]}A"
            # 'A5432' becomes '5432A'

        return _string in "AKQJT98765432A"

    def is_four_of_a_kind(self):
        """Returns whether this hand of cards is a four of a kind.

        A four of a kind contains four cards of the same rank.
        """
        return 4 in self._rank_histogram.values()

    def is_full_house(self):
        """Returns whether this hand of cards is a full house.

        A full house is a hand with only two different ranks such
        that three cards have one rank, and two have the other.
        """
        return self.is_three_of_a_kind() and self.is_pair()

    def is_three_of_a_kind(self):
        """Returns whether this hand of cards is a three of
        a kind.

        A three of a kind contains three cards of the same rank.
        """
        return 3 in self._rank_histogram.values()

    def is_two_pair(self):
        """Returns whether this hand of cards is a two pair.

        A two pair contains two pairs of cards having
        the same rank.
        """
        return list(self._rank_histogram.values()).count(2) == 2

    def is_pair(self):
        """Returns whether this hand of cards is a pair.

        A pair contains two cards of the same rank.
        """
        return 2 in self._rank_histogram.values()

    def grade(self):
        """Grades this hand, returning a constant representing
        the grade of the hand.

        100 represents a royal flush,
        90  represents a straight flush,
        .
        .
        .
        10  represents an uninteresting hand.
        """
        if self.is_royal_flush():
            return self.ROYAL_FLUSH
        if self.is_straight_flush():
            return self.STRAIGHT_FLUSH
        if self.is_flush():
            return self.FLUSH
        if self.is_straight():
            return self.STRAIGHT
        if self.is_four_of_a_kind():
            return self.FOUR_OF_A_KIND
        if self.is_full_house():
            return self.FULL_HOUSE
        if self.is_three_of_a_kind():
            return self.THREE_OF_A_KIND
        if self.is_two_pair():
            return self.TWO_PAIR
        if self.is_pair():
            return self.PAIR
        return self.MEH

    def compare_with(self, other_hand):
        """Returns a constant indicating whether comparing this
        hand against some other hand results in a WIN or a
        LOSS for this hand, or a TIE.

        1 represents a WIN for this hand,
        2 represents a LOSS for this hand,
        3 represents a TIE.
        """
        if self.grade() > other_hand.grade():
            return self.WIN
        if self.grade() < other_hand.grade():
            return self.LOSS
        return self.break_tie_with(other_hand)

    def break_tie_with(self, other_hand):
        """Returns a constant indicating whether breaking a
        tie for this hand against some other hand results in a
        WIN or a LOSS for this hand, or a TIE.

        1 represents a WIN for this hand,
        2 represents a LOSS for this hand,
        3 represents a TIE.
        """
        # assert that both hands are actually tied by grade
        if not self.grade() == other_hand.grade():
            raise InvalidTieBreakError

        for (self_rank, self_freq), (other_rank, other_freq) in zip(
            self._sorted_rank_count_tuple, other_hand._sorted_rank_count_tuple
        ):
            self_weight = Card.RANK_WEIGHT_MAP[self_rank]
            other_weight = Card.RANK_WEIGHT_MAP[other_rank]

            if self_weight > other_weight:
                return self.WIN
            if self_weight < other_weight:
                return self.LOSS
            continue

        return self.TIE

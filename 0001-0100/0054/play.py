from hand import Hand


def compare_hand_strings(string1, string2):
    """Compares a host hand string against an other hand string.

    A hand string is a string containing the
    string representation of five cards.
    * only five cards can be specified in the string.
    * <del>a space is</del><ins>spaces are</del> used as
      card separators.
    * each card in the string consists of two
      case insensitive characters.
        + first character is the rank of the card
            - valid ranks are: 2, 3, 4, 5, 6, 7, 8, 9,
                              T (for 10), J (for Jack),
                              Q (for Queen), K(for King),
                              A (for Ace)
        + second character is the suite
            - valid suites are: S (for Spades), H (for Hearts),
                              D (for Diamonds), C (for Clubs)

    Example: "KD 5S 2H AH 7H"

    Args:
        string1: the host hand.
        string2: the other hand.

    Returns:
        a constant indicating whether it's a WIN (1) for the
        host, or a LOSS (2) for the host, or a TIE (3).
    """
    return Hand.from_string(string1).compare_with(Hand.from_string(string2))

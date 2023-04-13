class InvalidRankError(AssertionError):
    """Exception to be raised when one tries
    instantiating a card with an invalid rank."""

    pass


class InvalidSuitError(AssertionError):
    """Exception to be raised when one tries
    instantiating a card with an invalid suit."""

    pass


class NonUniqueCardInHandError(AssertionError):
    """Exception to be raised when one tries
    instantiating a hand containing an invalid card."""

    pass


class InvalidCardStringError(AssertionError):
    """Exception to be raised when one tries instantiating
    a card from a string that could never be resolved
    to a valid card."""

    pass


class InvalidTieBreakError(AssertionError):
    """Exception to be raised when one tries
    a tie for unequally graded hands of cards."""

    pass

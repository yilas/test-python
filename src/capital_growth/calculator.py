"""Pure compound-interest calculations."""


def projection(initial: float, target: float, rate: float) -> list[float]:
    """Return initial capital and yearly balances until target is reached."""
    if initial <= 0 or target <= 0:
        raise ValueError("Initial capital and target must be positive")
    if rate <= 0 or rate > 1:
        raise ValueError("Rate must be greater than zero and at most one")
    balances = [float(initial)]
    while balances[-1] < target:
        balances.append(balances[-1] * (1 + rate))
    print(balances)
    return balances


def years_to_target(initial: float, target: float, rate: float) -> int:
    """Number of complete years needed to reach target."""
    return len(projection(initial, target, rate)) - 1

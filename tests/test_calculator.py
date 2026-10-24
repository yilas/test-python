import pytest

from capital_growth.calculator import projection, years_to_target


def test_original_example():
    assert years_to_target(1000, 200000, 0.03) == 180


def test_target_already_reached():
    assert years_to_target(200000, 200000, 0.03) == 0


def test_two_years():
    assert years_to_target(100, 121, 0.10) == 2


def test_projection():
    assert projection(100, 121, 0.1) == pytest.approx([100, 110, 121])


@pytest.mark.parametrize(
    "initial,target,rate",
    [(0, 100, 0.03), (-1, 100, 0.03), (100, 0, 0.03),
     (100, 200, 0), (100, 200, -0.01), (100, 200, 1.01)],
)
def test_invalid(initial, target, rate):
    with pytest.raises(ValueError):
        projection(initial, target, rate)

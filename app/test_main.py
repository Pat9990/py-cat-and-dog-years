from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_dog, dog_age, exp_cat, exp_dog",
                         [(0, 0, 0, 0),
                          (14, 14, 0, 0),
                          (15, 15, 1, 1),
                          (23, 23, 1, 1),
                          (24, 24, 2, 2),
                          (27, 27, 2, 2),
                          (28, 28, 3, 2),
                          (100, 100, 21, 17)])
def test_verify_cat_dog_age(
        cat_dog: int,
        dog_age: int,
        exp_cat: int,
        exp_dog: int
) -> None:
    assert get_human_age(cat_dog, dog_age) == [exp_cat, exp_dog]

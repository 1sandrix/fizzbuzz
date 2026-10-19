from fizzbuzz import fizzbuzz

def test_1_to_10_with_fizz_and_buzz():
    assert fizzbuzz(10) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

def test_prints_1_to_100():
    assert len(fizzbuzz()) == 100
    assert fizzbuzz()[0] == 1
    assert fizzbuzz()[99] == "Buzz"
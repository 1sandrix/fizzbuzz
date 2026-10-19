from fizzbuzz import fizzbuzz

def test_prints_numbers_1_to_10_with_fizz():
    assert fizzbuzz(10) == [1, 2, "Fizz", 4, 5, "Fizz", 7, 8, "Fizz", 10]

def test_prints_1_to_100():
    assert len(fizzbuzz()) == 100
    assert fizzbuzz()[0] == 1
    assert fizzbuzz()[99] == 100
from fizzbuzz import fizzbuzz

def test_1_to_15_with_fizzbuzz():
    assert fizzbuzz(15) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

def test_prints_1_to_100():
    assert len(fizzbuzz()) == 100
    assert fizzbuzz()[0] == 1
    assert fizzbuzz()[99] == "Buzz"
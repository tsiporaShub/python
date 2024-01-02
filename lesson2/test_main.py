import main
import pytest


def test_find_primes():
    assert main.find_primes(15) == [2, 3, 5, 7, 11, 13]
    assert main.find_primes(5) == [2, 3]


@pytest.mark.skip(reason="dont computed")
def test_find_primes2():
    assert main.find_primes(100) == [2, 3, 5, 7, 11, 13]


@pytest.mark.parametrize("mylist,result", [([3, 5, 8, 1], [1, 3, 5, 8]), ([1, 6, 5, 8, 8, 1], [1, 1, 5, 6, 8, 8])])
def test_sort_list(mylist, result):
    assert main.sort_list(mylist) == result


@pytest.mark.sort
def test_sort_list2():
    assert main.sort_list([3, 9, 8, 2, 5, 5]) == [2, 3, 5, 5, 8, 9]


@pytest.mark.sort
def test_sort_list2():
    assert main.sort_list([3, 9, 2, 5, 5]) == [2, 3, 5, 5, 9]

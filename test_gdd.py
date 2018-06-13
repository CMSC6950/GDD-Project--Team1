import pytest
import gdd

def test_gddCal():
	observed = gdd.gddCal(25,15,10,30)
	expected = 10
	assert observed == expected
	
def test_gddCal2():
	observed = gdd.gddCal(35,20,10,30)
	expected = 15
	assert observed == expected
	
def test_gddCal3():
	observed = gdd.gddCal(10,8,10,30)
	expected = 0
	assert observed == expected
from CIE2 import temperature
def test_tempartureneagative():
    assert temperature(-25)==-13
def test_temperaturepositive():
    assert temperature(25)==77
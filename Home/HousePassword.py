def checkio(data):
    if (len(data) < 10):
        return False
    import re
    cond = re.match("^(?=.*?[0-9])(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z0-9]{10,}$", data)
    return cond is not None


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
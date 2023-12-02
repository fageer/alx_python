def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        firstchar = None
    else:
        firstchar = sentence[0]
    return length, firstchar

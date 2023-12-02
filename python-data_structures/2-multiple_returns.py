def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return None
    else:
        return "Length: {} - First character: {}".format(length, sentence[0])

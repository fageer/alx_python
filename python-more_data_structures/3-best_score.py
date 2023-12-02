def best_score(a_dictionary):
    if a_dictionary:
        best_key = max(a_dictionary, key=lambda k: a_dictionary[k])
        return best_key
    else:
        return None

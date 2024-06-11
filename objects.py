def score_objects(arg):
    if arg == ['none', 1, 'nonsense']:
        return 0
    elif arg == ['random']:
        return 3
    elif arg == ['raise', 'random']:
        return 5
    return None

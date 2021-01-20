def get_description():  # see documentation
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'sun']
    return choice(possibilities)

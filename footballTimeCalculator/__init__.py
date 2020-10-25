def convertFootballTimeToReal(original):
    """
    parameter original: Original number
    Algorithm comes from the fact that a football game is supposed to last 60 minutes, but actually lasts two and a half hours. So I multiply the original number by 2.5 and it works!
    Sadly it doesn't account for overtime but that's because it's unpredictable.
    """
    return original * 2.5

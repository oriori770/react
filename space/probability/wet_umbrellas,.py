def probability_to_wet(umbrellas, p):
    q = 1 - p
    chance = q * p / (q + umbrellas)
    return chance

    return


def stay_dry(percent, p):
    q = 1 - p
    if 0 < percent <= 100:
        n = 100 * p * q - q
        return n / percent


print(stay_dry(5, 0.6))
print(probability_to_wet(4, 0.6))

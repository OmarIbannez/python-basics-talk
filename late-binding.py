
def late_create_multipliers():
    return [lambda x : i * x for i in range(5)]

def late_binding():
    for multiplier in late_create_multipliers():
        print multiplier(2)

late_binding()

def immediately_create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]


def immediately_binding():
    for multiplier in immediately_create_multipliers():
        print multiplier(2)

immediately_binding()

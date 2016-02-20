# possible subscription models
subs = ("minute", "hour", "day", "week", "month", "year")

def calculate_payment(sub, sub_units, default_sub, default_units, default_price):
    '''
    Converts a subscription price of default_price per default_units per
    default_sub to a price per sub_units per sub, adjusted so we can make money.

    For example, calling calculate_payment("day", 2, "month", 1, 15.00) will
    convert the $15 per month cost to the price per two days.

    This function is assuming that sub is a smaller unit of time than
    default_sub because that's our business model.

    Returns -1 on an error, or the converted price if successful.
    '''

    sub_index = subs.index(sub)
    def_index = subs.index(default_sub)

    # errors
    if sub_index == -1 or def_index == -1:
        # subscription models not found
        return -1
    elif sub_index >= def_index:
        # no point converting a smaller subscription length into a larger one
        return -1
    elif default_price <= 0:
        # negative price
        return -1
    elif sub_units <= 0 or default_units <= 0:
        # can't have a non-positive number of hours/days etc.
        return -1

    # our price will be this many times the actual price
    inflate = 1 + abs(def_index - sub_index) / 5
    # convert prices to $/min
    if default_sub == "year":
        per_min = default_price / default_units / 365 / 24 / 60
    elif default_sub == "month":
        per_min = default_price / default_units / 365 * 12 / 24 / 60
    elif default_sub == "week":
        per_min = default_price / default_units / 7 / 24 / 60
    elif default_sub == "day":
        per_min = default_price / default_units / 24 / 60
    elif default_sub == "hour":
        per_min = default_price / default_units / 60

    # convert from $/min to the desired format
    if sub == "hour":
        return per_min * inflate * sub_units * 60
    elif sub == "day":
        return per_min * inflate * sub_units * 60 * 24
    elif sub == "week":
        return per_min * inflate * sub_units * 60 * 24 * 7
    elif sub == "month":
        return per_min * inflate * sub_units * 60 * 24 * 365 / 12

    # sub is a per minute subscription, so return the per_min price
    return per_min * inflate * sub_units

# test calculate_payment
# valid
print(calculate_payment("hour", 1, "month", 1, 15.00))
print(calculate_payment("minute", 1, "month", 6, 100.00))
print(calculate_payment("hour", 6, "year", 3, 300.00))
# invalid
print(calculate_payment("hour", 7, "minute", 4, 500.00))
print(calculate_payment("year", 5, "year", 4, 40.0))
print(calculate_payment("month", 5, "year", -6, 5))

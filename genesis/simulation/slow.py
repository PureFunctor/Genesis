import random


def simulation(cc, tc):
    """Takes the total count of cards in a card pack and the count
    of specific cards to be obtained and returns the count of rolls
    and duplicates aggregated in obtained the target cards."""

    tc = tc if cc >= tc else cc

    missing = set(range(1, cc + 1))
    targets = set(range(1, tc + 1))

    roll_count = 0
    dupe_count = 0

    generation_power = 0

    while missing.intersection(targets):
        roll_count += 1

        rolls = 5 if generation_power < 100 else 4

        if rolls == 4:
            card = random.choice(list(missing))
            missing.remove(card)
            generation_power = 0
        
        for _ in range(rolls):
            card = random.randint(1, cc)

            if card in missing:
                missing.remove(card)
            
            else:
                generation_power += 10
                dupe_count += 1
    
    return roll_count, dupe_count


def frequency(data):
    """Returns the frequency of items in a data tuple."""
    items = sorted(set(data))
    count = (data.count(i) for i in items)
    return dict(zip(items, count))


def aggregate(cc, tc, ss):
    """Given a sample size, call simulate on a given card count and target
    count, aggregate and split the data for the roll counts and the duplicate
    counts, compute the mean and the frequency of items."""

    aggregate = (simulation(cc, tc) for _ in range(ss))
    rc, dc = zip(*aggregate)
    return {
        "rc_mean": sum(rc) / len(rc),
        "dc_mean": sum(dc) / len(dc),
        "rc_frequency": frequency(rc),
        "dc_frequency": frequency(dc),
    }

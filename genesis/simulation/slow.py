import random


def simulate(cc, tc):
    tc = tc if cc >= tc else cc

    trg_set = set(range(1, tc + 1))
    unowned = set(range(1, cc + 1))

    roll_count = 0
    dupe_count = 0

    generation_power = 0

    while unowned.intersection(trg_set):
        roll_count += 1

        rolls = 5 if generation_power < 100 else 4
        cards = (random.randint(1, cc) for _ in range(rolls))

        if rolls == 4:
            unique = random.choice(list(unowned))
            unowned.remove(unique)
            generation_power = 0

        for card in cards:
            if card in unowned:
                unowned.remove(card)
            elif card not in unowned:
                generation_power += 10
                dupe_count += 1

    return roll_count, dupe_count


def frequency(data):
    items = sorted(set(data))
    count = (data.count(i) for i in items)
    return dict(zip(items, count))


def aggregate(cc, tc, ss):
    aggregate = (simulate(cc, tc) for _ in range(ss))
    rc, dc = zip(*aggregate)
    return {
        "rc_mean": sum(rc) / len(rc),
        "dc_mean": sum(dc) / len(dc),
        "rc_frequency": frequency(rc),
        "dc_frequency": frequency(dc),
    }

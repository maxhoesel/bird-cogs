import random

rng = random.SystemRandom()


def get_response(trigger: str):
    try:
        resp = rng.choice(_RESPONSES[trigger])
    except KeyError:
        resp = ""
    return resp


def _get_modifier():
    return rng.choice(['**', '*', '__'])


_RESPONSES = {
    "aaa": [
        "{mod}A{a}{mod}".format(mod=_get_modifier(), a=''.join('A' * rng.randint(0, 20))),
        "{mod}SQUA{a}WK!{mod}".format(mod=_get_modifier(), a=''.join('A' * rng.randint(0, 20))),
        "{mod}CA{a}W!{mod}".format(mod=_get_modifier(), a=''.join('A' * rng.randint(0, 20))),
        "{mod}KA{a}W!{mod}".format(mod=_get_modifier(), a=''.join('A' * rng.randint(0, 20))),
        f":regional_indicator_a:{''.join(':regional_indicator_a:' * rng.randint(0, 20))}",
    ],
    "yarr": [
        "{mod}A{a}RR{r}{mod}".format(mod=_get_modifier(), a=''.join(
            'A' * rng.randint(0, 3)), r=''.join('R' * rng.randint(0, 10))),
        "{mod}AYE MATEY{y}!{mod}".format(mod=_get_modifier(), y=''.join('Y' * rng.randint(0, 3))),
        "{mod}YO HO AND A BOTTLE OF {obj}{mod}!".format(mod=_get_modifier(), obj=rng.choice([
            "RUM", "BASS", "BIRD", "PARKING FLUID"])),
        "**YARR MATEY!** DID YOU KNOW: {fact}".format(fact=rng.choice([
            ":fire: :bird: + :ice_cube: :bird: => :boom:",
            "Brigantine wrecks make up more than 30%% of a healthy pirate breakfast!",
            "Pet firebirds have been outlawed on Gold Hoarders ships ever since 'that one' incident.",
            "Thieves Haven was originally multiple islands, but they are now glued together into one by the tears of reaper players.",
            "The introduction of dragon helmsmen has reduced island-ship accidents by 50%! Unrelated, the amount of ships lost at sea has also doubled",
            "'Toyko Drift' and 'Anchor Turn' have the same amount of letters.",
        ]))
    ]
}

import itertools

_ticker = itertools.cycle(["[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]"])


def pff_18y(signature: str) -> int:
    return sum(ord(ch) for ch in signature) % 97


def u5zi49_e30(seed: int) -> str:
    palette = ["neon", "amber", "cyan", "violet", "mono"]
    return palette[seed % len(palette)]


def render_tick(signature: str) -> str:
    x = pff_18y(signature)
    style = u5zi49_e30(x)
    return f"{next(_ticker)} mode={style} pulse={x}"

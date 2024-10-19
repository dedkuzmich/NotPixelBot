def rgb_to_hex(rgb: tuple) -> str:
    hex = "#{:02x}{:02x}{:02x}".format(*rgb)
    return hex


def hex_to_rgb(hex: str) -> tuple:
    hex = hex.lstrip("#")
    rgb = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    return rgb


class Rect():
    def __init__(self, tl: list, br: list):
        self.tl = tl
        self.br = br


class Color():
    def __init__(self, hex: str, rects: list[Rect] = None):
        self.hex = hex
        self.rgb = hex_to_rgb(hex)
        if not rects:
            rects = []
        self.rects: list[Rect] = rects


# Colors are located in the order like in GUI grid (3 rows x 10 rows = 30 in total)
colors = [
    # idx 0-9, num 1-10
    Color("#e46e6e"),
    Color("#ffd635"),
    Color("#7eed56"),
    Color("#00ccc0"),
    Color("#51e9f4"),
    Color("#94b3ff"),
    Color("#e4abff"),
    Color("#ff99aa"),
    Color("#ffb470"),
    Color("#ffffff"),

    # idx 10-19, num 11-20
    Color("#be0039"),
    Color("#ff9600"),
    Color("#00cc78"),
    Color("#009eaa"),
    Color("#3690ea"),
    Color("#6a5cff"),
    Color("#b44ac0"),
    Color("#ff3881"),
    Color("#9c6926"),
    Color("#898d90"),

    # idx 20-29, num 21-30
    Color("#6d001a"),
    Color("#bf4300"),
    Color("#00a368"),
    Color("#00756f"),
    Color("#2450a4"),
    Color("#493ac1"),
    Color("#811e9f"),
    Color("#a00357"),
    Color("#6d482f"),
    Color("#000000"),
]

# Use indexes to set rects. Index = Number -1
# Rect([x1, y1], [x2, y2])
# [x1, y2] is top-left pixel, [x2, y2] is bottom-right px
# !!! 3x PX bonus doesn't work with colorful pixels, use only black (idx = 29)

# colors[11].rects = [
#     Rect([499, 920], [503, 927]),
#     Rect([510, 920], [513, 926]),
# ]
#
# colors[14].rects = [
#     Rect([517, 916], [527, 917]),
# ]
#
# colors[25].rects = [
#     Rect([545, 941], [547, 949]),
#     Rect([538, 939], [541, 940]),
# ]
#
# colors[9].rects = [
#     Rect([541, 922], [543, 924]),
#     Rect([537, 922], [539, 924]),
# ]

colors[29].rects = [
    Rect([49, 876], [77, 896]),
    Rect([74, 900], [88, 918]),
    Rect([138, 878], [162, 919]),
    Rect([142, 828], [161, 852]),
    Rect([143, 795], [156, 816]),
    Rect([54, 826], [72, 848]),
]

COLORS = colors

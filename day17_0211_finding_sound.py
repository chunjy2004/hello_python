import winsound

oct = {
    'C':261,'D':293,'E':329,'F':349,'G':391,'A':440,'B':493,
    'C2': 523, 'D2': 587, 'E2': 659, 'F2': 698, 'G2': 783, 'A2': 880,
    'B2': 987, 'blk': 37
    }

plane = [
    'E', 'D', 'C', 'D',
    'E', 'E', 'E',
    'blk',
    'D', 'D', 'D',
    'blk',
    'E', 'E', 'E',
    'blk',
    'E', 'D', 'C', 'D',
    'E', 'E', 'E',
    'blk',
    'D', 'D', 'E', 'D', 'C'
    ]

CDEsong = [
    'C', 'blk', 'blk', 'D', 'E', 'blk', 'blk', 'C', 'E', 'blk', 'C', 'blk', 'E', 'blk', 'blk', 'blk',
    'D', 'blk', 'blk', 'E', 'F', 'F', 'E', 'D', 'F', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk',
    'E', 'blk', 'blk', 'F', 'G', 'blk', 'blk', 'E', 'G', 'blk', 'E', 'blk', 'G', 'blk', 'blk', 'blk',
    'F', 'blk', 'blk', 'G', 'A', 'A', 'G', 'F', 'A', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk',
    'G', 'blk', 'blk', 'C', 'D', 'E', 'F', 'G', 'A', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk',
    'A', 'blk', 'blk', 'D', 'E', 'F', 'G', 'A', 'B', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk', 'blk',
    'B', 'blk', 'blk', ''
]
def play_song(lists, delay):

    for list in lists:
        winsound.Beep(oct[list], delay)
play_song(CDEsong, 300)

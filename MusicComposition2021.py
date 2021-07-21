# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools

# Step 1 - Generate libraries

# 12 possible keys
# 0: C
# 1: C# / Db
# 2: D
# 3: D# / Eb
# 4: E
# 5: F
# 6: F# / Gb
# 7: G
# 8: G# / Ab
# 9: A
# 10: A# / Bb
# 11: B

# the more key changes, the more complex the song
# the larger jumps between key changes, the more complex the song
# separate button to adjust this?
keyLibrary = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# rhythm without duration, for 8, 16, and 32 beats
percussiveRhythmLibrary_8 = list(itertools.product([0, 1], repeat=8))
percussiveRhythmLibrary_16 = list(itertools.product([0, 1], repeat=16))
percussiveRhythmLibrary_32 = list(itertools.product([0, 1], repeat=32))

# rhythm with duration, for 8, 16, and 32 beats
# note starts on 2, continues with 1, and ends / doesn't play on 0
durationRhythmLibrary_8 = list(itertools.product([0, 1, 2], repeat=8))
durationRhythmLibrary_16 = list(itertools.product([0, 1, 2], repeat=16))
durationRhythmLibrary_32 = list(itertools.product([0, 1, 2], repeat=32))

# Selects notes from a chord with 3 intervals
melodyLibrary_3_8 = list(itertools.product([0, 1, 2], repeat=8))
melodyLibrary_3_16 = list(itertools.product([0, 1, 2], repeat=16))
melodyLibrary_3_32 = list(itertools.product([0, 1, 2], repeat=32))

# Selects notes from a chord with 4 intervals
melodyLibrary_4_8 = list(itertools.product([0, 1, 2, 3], repeat=8))
melodyLibrary_4_16 = list(itertools.product([0, 1, 2, 3], repeat=16))
melodyLibrary_4_32 = list(itertools.product([0, 1, 2, 3], repeat=32))

# Selects notes from a chord with 5 intervals
melodyLibrary_5_8 = list(itertools.product([0, 1, 2, 3, 4], repeat=8))
melodyLibrary_5_16 = list(itertools.product([0, 1, 2, 3, 4], repeat=16))
melodyLibrary_5_32 = list(itertools.product([0, 1, 2, 3, 4], repeat=32))

# Selects notes from a chord with 6 intervals
# the more interval jumps, the higher the complexity
melodyLibrary_6_8 = list(itertools.product([0, 1, 2, 3, 4. 5], repeat=8))
melodyLibrary_6_16 = list(itertools.product([0, 1, 2, 3, 4, 5], repeat=16))
melodyLibrary_6_32 = list(itertools.product([0, 1, 2, 3, 4, 5], repeat=32))

# Chord progressions 
# 0: I
# 1: ii
# 2: iii
# 3: IV
# 4: V
# 5: vi
# 6: bVII
# 7: bVI
# 8: bIII
# 9: II
# 10: III
# 11: iv
# 12: bV
# 13: v
# the higher the numbers, the more the complexity rating
# the more chord changes, the higher the complexity
chordProgressionLibrary_4 = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], repeat=4))
chordProgressionLibrary_8 = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], repeat=8))
chordProgressionLibrary_16 = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], repeat=16))

# Chord extensions
# 0: Major
# 1: Minor
# 2: 5
# 3: 6
# 4: 6/9
# 5: 7
# 6: add9
# 7: maj7
# 8: maj9
# 9: maj11
# 10: maj13
# 11: sus2
# 12: sus4
# 13: augmented
# 14: diminished
# 15: m6
# 16: m6/9
# 17: m7
# 18: m9
# 19: madd9
# 20: m11
# 21: m13
# 22: mmaj7
# 23: mmaj9
chordExtensionLibrary_4 = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], repeat=4))
chordExtensionLibrary_8 = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], repeat=8))
chordExtensionLibrary_16 = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], repeat=16))

# From 0 (softest) to 9 (loudest)
# the more dynamics changes the more complex
dynamicsLibrary_8 = list(itertools.product([0, 1, 2, 3, 4. 5, 6, 7, 8, 9], repeat=8))
dynamicsLibrary_16 = list(itertools.product([0, 1, 2, 3, 4. 5, 6, 7, 8, 9], repeat=16))
dynamicsLibrary_32 = list(itertools.product([0, 1, 2, 3, 4. 5, 6, 7, 8, 9], repeat=32))



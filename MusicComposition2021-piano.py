# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
import pianoPart
import midiFunctions
import mido
import sys
from datetime import datetime
import shutil
from globals import TIME_SIG

now = datetime.now()

timestamp = "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)

piano_notes = np.zeros((8,0), dtype=np.int64)
piano_velocity = np.zeros((8,0), dtype=np.int64)
piano_onoff = np.ones((8,0), dtype=np.int64) # all 1's for percussive parts (?)

np.set_printoptions(linewidth=150)
np.set_printoptions(threshold=sys.maxsize)

KEYS = ["C", "G"]

repititions = 1

i = 0 
while i < repititions: 

	bass_part, treble_part = pianoPart.get(scaleDegrees=[1,5,8,12])

	piano_notes, piano_velocity, piano_onoff = pianoPart.compilePianoPart(bass_part, treble_part, key="C")

	filename = "pianoPart" + timestamp +  "_" + str(i)

	midiFunctions.createMidiFile(piano_notes, piano_velocity, piano_onoff, 80, filename, "Piano")

	i+= 1
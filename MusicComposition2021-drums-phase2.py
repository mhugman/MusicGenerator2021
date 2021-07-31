# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
import drumPart
import midiFunctions
import mido
import os
import sys
from datetime import datetime
import shutil
from globals import TIME_SIG
from globals import SONG_LENGTH
from globals import NUM_BARS_IN_PART

NUM_16th_PER_BAR = TIME_SIG * 4

hihat_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
ride_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64)
kick_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
snare_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
tom_h_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
tom_m_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
tom_l_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64)
crash_part = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64)

print("Contents of midi/saved: ")
print(os.listdir("midi/saved"))

filename = input("Enter saved midi filename (midi/saved): ")

noteArray, velocityArray, onOffArray = midiFunctions.parseMidi(mido.MidiFile('midi/saved/' + filename + '.mid'))

print("Reconverted array: ")
print(noteArray[0])
print("----")
print(noteArray[1])
print("----")
print(noteArray[2])
print("----")
print(noteArray[3])
print("----")
print(noteArray[4])
print("----")
print(noteArray[5])
print("----")
print(noteArray[6])
print("----")
print(noteArray[7])
print("----")

kick_part[0] = noteArray[0][:NUM_BARS_IN_PART*NUM_16th_PER_BAR]
snare_part[0] = noteArray[1][:NUM_BARS_IN_PART*NUM_16th_PER_BAR]
hihat_part[0] = noteArray[2][:NUM_BARS_IN_PART*NUM_16th_PER_BAR]
ride_part[0] = noteArray[3][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_h_part[0] = noteArray[4][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_m_part[0] = noteArray[5][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_l_part[0] = noteArray[6][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
crash_part[0] = noteArray[7][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 

kick_part[1] = velocityArray[0][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
snare_part[1] = velocityArray[1][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
hihat_part[1] = velocityArray[2][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
ride_part[1] = velocityArray[3][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_h_part[1] = velocityArray[4][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_m_part[1] = velocityArray[5][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_l_part[1] = velocityArray[6][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
crash_part[1] = velocityArray[7][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 

'''
kick_part[2] = onOffArray[0] 
snare_part[2] = onOffArray[1] 
hihat_part[2] = onOffArray[2] 
ride_part[2] = onOffArray[3] 
tom_h_part[2] = onOffArray[4] 
tom_m_part[2] = onOffArray[5] 
tom_l_part[2] = onOffArray[6] 
crash_part[2] = onOffArray[7] 
'''
print(kick_part[0])
print(snare_part[0])
print(hihat_part[0])
print(ride_part[0])
print(tom_h_part[0])
print(tom_m_part[0])
print(tom_l_part[0])
print(crash_part[0])

running = True

while running and selection != 'q': 

	print("--- mutating drum part ---")
	print("Options: ")
	print("a: mutate parts")
	print("h: mutate hi hat part")
	print("r: mutate ride part")
	print("k: mutate kick part")
	print("s: mutate snare part")
	print("1: mutate high tom part")
	print("2: mutate mid tom part")
	print("3: mutate low tom part")
	print("t: mutate all tom parts")
	print("c: mutate crash part")
	print("q: quit")

	selection = input("Selection: ")

	whichPartsToMutate = []

	if selection == "a": 
		whichPartsToMutate = ["hihat", "ride", "kick", "snare", "tom_h", "tom_m", "tom_l", "crash"]
	elif selection == "h": 
		whichPartsToMutate.append("hihat")
	elif selection == "r": 
		whichPartsToMutate.append("ride")
	elif selection == "k": 
		whichPartsToMutate.append("kick")
	elif selection == "s": 
		whichPartsToMutate.append("snare")
	elif selection == "1": 
		whichPartsToMutate.append("tom_h")
	elif selection == "2": 
		whichPartsToMutate.append("tom_m")
	elif selection == "3": 
		whichPartsToMutate.append("tom_l")
	elif selection == "t": 
		whichPartsToMutate.append("tom_l")
		whichPartsToMutate.append("tom_m")
		whichPartsToMutate.append("tom_h")
	elif selection == "c": 
		whichPartsToMutate.append("crash")
	elif selection == "q": 
		running = False
		break
	else: 
		print("Selection not recognized")

	new_kick_part, new_snare_part, new_hihat_part, new_ride_part, new_tom_h_part, new_tom_m_part, new_tom_l_part, new_crash_part \
	= drumMutate.get(kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part \
		, whichPartsToMutate=whichPartsToMutate)

	

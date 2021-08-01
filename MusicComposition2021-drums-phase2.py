# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
import drumPart
import drumMutate
import midiFunctions
import mido
import os
import sys
from datetime import datetime
import shutil
from globals import TIME_SIG
from globals import SONG_LENGTH
from globals import NUM_BARS_IN_PART
from copy import deepcopy

now = datetime.now()

timestamp = "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)

NUM_16th_PER_BAR = TIME_SIG * 4

hihat_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
ride_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64)
kick_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
snare_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
tom_h_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
tom_m_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64) 
tom_l_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64)
crash_part_original = np.zeros((3,NUM_BARS_IN_PART*NUM_16th_PER_BAR), dtype=np.int64)

print("Contents of midi/saved: ")
print(os.listdir("midi/saved"))

filename = input("Enter saved midi filename (midi/saved): ")

noteArray, velocityArray, onOffArray = midiFunctions.parseMidi(mido.MidiFile('midi/saved/' + filename + '.mid'))

'''
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
'''

kick_part_original[0] = noteArray[0][:NUM_BARS_IN_PART*NUM_16th_PER_BAR]
snare_part_original[0] = noteArray[1][:NUM_BARS_IN_PART*NUM_16th_PER_BAR]
hihat_part_original[0] = noteArray[2][:NUM_BARS_IN_PART*NUM_16th_PER_BAR]
ride_part_original[0] = noteArray[3][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_h_part_original[0] = noteArray[4][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_m_part_original[0] = noteArray[5][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_l_part_original[0] = noteArray[6][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
crash_part_original[0] = noteArray[7][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 

kick_part_original[1] = velocityArray[0][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
snare_part_original[1] = velocityArray[1][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
hihat_part_original[1] = velocityArray[2][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
ride_part_original[1] = velocityArray[3][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_h_part_original[1] = velocityArray[4][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_m_part_original[1] = velocityArray[5][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
tom_l_part_original[1] = velocityArray[6][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 
crash_part_original[1] = velocityArray[7][:NUM_BARS_IN_PART*NUM_16th_PER_BAR] 

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
print(kick_part_original[0])
print(snare_part_original[0])
print(hihat_part_original[0])
print(ride_part_original[0])
print(tom_h_part_original[0])
print(tom_m_part_original[0])
print(tom_l_part_original[0])
print(crash_part_original[0])

print("--------------------------------")

kick_parts = [kick_part_original]
snare_parts = [snare_part_original]
hihat_parts = [hihat_part_original]
ride_parts = [ride_part_original]
tom_h_parts = [tom_h_part_original]
tom_m_parts = [tom_m_part_original]
tom_l_parts = [tom_l_part_original]
crash_parts = [crash_part_original]

kick_part = deepcopy(kick_part_original)
snare_part = deepcopy(snare_part_original)
hihat_part = deepcopy(hihat_part_original)
ride_part = deepcopy(ride_part_original)
tom_h_part = deepcopy(tom_h_part_original)
tom_m_part = deepcopy(tom_m_part_original)
tom_l_part = deepcopy(tom_l_part_original)
crash_part = deepcopy(crash_part_original)

# create 3 modifications
for i in range(3): 
	selection = "x"
	while selection != 'q': 

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
			break
		else: 
			print("Selection not recognized")

		complexity_selection = input("Enter 'x' to complexify, 's' to simplify, or 'b' for both: ")

		if complexity_selection == 'x': 
			kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part \
			= drumMutate.get(kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part \
				, whichPartsToMutate=whichPartsToMutate, sample_size = 8, complexify = True, simplify = False)
		elif complexity_selection == 's': 
			kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part \
			= drumMutate.get(kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part \
				, whichPartsToMutate=whichPartsToMutate, sample_size = 8, complexify = False, simplify = True)
		elif complexity_selection == 'b': 
			kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part \
			= drumMutate.get(kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part \
				, whichPartsToMutate=whichPartsToMutate, sample_size = 8, complexify = True, simplify = True)

		print("Mutated drum part: ")
		
		print(kick_part[0])
		print(snare_part[0])
		print(hihat_part[0])
		print(ride_part[0])
		print(tom_h_part[0])
		print(tom_m_part[0])
		print(tom_l_part[0])
		print(crash_part[0])

		print("--------------------------------")

	print("Saving mutated drum part...")
	kick_parts.append(kick_part)
	snare_parts.append(snare_part)
	hihat_parts.append(hihat_part)
	ride_parts.append(ride_part)
	tom_h_parts.append(tom_h_part)
	tom_m_parts.append(tom_m_part)
	tom_l_parts.append(tom_l_part)
	crash_parts.append(crash_part)

notes = []
velocities = []
onoffs = []

for i in range(4): 

	kick_part_ = kick_parts[i]
	snare_part_ = snare_parts[i]
	hihat_part_ = hihat_parts[i]
	ride_part_ = ride_parts[i]
	tom_h_part_ = tom_h_parts[i]
	tom_m_part_ = tom_m_parts[i]
	tom_l_part_ = tom_l_parts[i]
	crash_part_ = crash_parts[i]

	drum_part_notes, drum_part_velocity, drum_part_onoff = \
		drumMutate.compileDrumPart(hihat_part_, ride_part_, kick_part_, snare_part_, tom_h_part_, tom_m_part_, tom_l_part_, crash_part_)

	print(drum_part_notes[0])
	print(drum_part_notes[1])
	print(drum_part_notes[2])
	print(drum_part_notes[3])
	print(drum_part_notes[4])
	print(drum_part_notes[5])
	print(drum_part_notes[6])
	print(drum_part_notes[7])
	print("--------------------------------")

	notes.append(drum_part_notes)
	velocities.append(drum_part_velocity)
	onoffs.append(drum_part_onoff)

print("Select structure of drum complete part: ")
print("Options: ")
print("1: [AABB] [CCDD] [AABB]")
print("2: [AAB] [AAB] [CCD]")
print("3: [AABA] [AABA] [CCDC] [AABA]")
print("4: [ABAB] [CDCD] [ABAB] [CDCD]")
print("5: [ABA] [CDC] [ABA] [CDC]")
structure_selection = input("Selection: ")

if structure_selection == "1": 
	structure = "AABBCCDDAABB"
elif structure_selection == "2": 
	structure = "AABAABCCD"
elif structure_selection == "3": 
	structure = "AABAAABACCDCAABA"
elif structure_selection == "4": 
	structure = "ABABCDCDABABCDCD"
elif structure_selection == "5": 
	structure = "ABACDCABACDC"
else:
	print("Selection not recognized")

drum_complete_notes, drum_complete_velocity, drum_complete_onoff = \
		drumMutate.createDrumComplete(notes, velocities, onoffs, structure)

completefilename = "drumComplete_" + filename + timestamp 

midiFunctions.createMidiFile(drum_complete_notes, drum_complete_velocity, drum_complete_onoff, 80, completefilename)

	

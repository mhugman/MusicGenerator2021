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

NUM_16th_PER_BAR = TIME_SIG * 4

now = datetime.now()

timestamp = "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)

piano_notes = np.zeros((4,0), dtype=np.int64)
piano_velocity = np.zeros((4,0), dtype=np.int64)
piano_onoff = np.ones((4,0), dtype=np.int64) 

piano_part_notes = np.zeros((4,NUM_16th_PER_BAR), dtype=np.int64)
piano_part_velocity = np.zeros((4,NUM_16th_PER_BAR), dtype=np.int64)
piano_part_onoff = np.zeros((4,NUM_16th_PER_BAR), dtype=np.int64) 

piano_segment_notes = np.zeros((4,0), dtype=np.int64)
piano_segment_velocity = np.zeros((4,0), dtype=np.int64)
piano_segment_onoff = np.ones((4,0), dtype=np.int64)

np.set_printoptions(linewidth=150)
np.set_printoptions(threshold=sys.maxsize)

# I ii III IV V VI VII bVII bVI bIII 
KEY_C = ["C", "D", "E", "F", "G", "A", "B", "Bb", "G#", "Eb"]
KEY_C_sharp = ["C#", "Eb", "F", "F#", "G#", "Bb", "C", "B", "A", "E"]
KEY_D = ["D", "E", "F#", "G", "A", "B", "C#", "C", "A#", "F"]
KEY_E_flat = ["Eb", "F", "G", "G#", "Bb", "C", "D", "C#", "B", "F#"]
KEY_E = ["E", "F#", "G#", "A", "B", "C#", "Eb", "D", "C", "G"]
KEY_F = ["F", "G", "A", "Bb", "C", "D", "E", "D#", "C#", "G#"]
KEY_F_sharp = ["F#", "G#", "Bb", "B", "C#", "Eb", "F", "E", "D", "A"]
KEY_G = ["G", "A", "B", "C", "D", "E", "F#", "F", "D#", "A#"]
KEY_G_sharp = ["G#", "Bb", "C", "C#", "D#", "F", "G", "F#", "E", "B"]
KEY_A = ["A", "B", "C#", "D", "E", "F#", "G#", "G", "F", "C"]
KEY_B_flat = ["Bb", "C", "D", "D#", "F", "G", "A", "G#", "F#", "C#"]
KEY_B = ["B", "C#", "D#", "E", "F#", "G#", "Bb", "A", "G", "D"]

print("Select key: ")
print("Options: ")
print("1: C")
print("2: C#")
print("3: D")
print("4: Eb")
print("5: E")
print("6: F")
print("7: F#")
print("8: G")
print("9: G#")
print("10: A")
print("11: Bb")
print("12: B")

key_selection = input("Selection: ")

if key_selection == "1": 
	key = KEY_C
elif key_selection == "2": 
	key = KEY_C_sharp
elif key_selection == "3": 
	key = KEY_D
elif key_selection == "4": 
	key = KEY_E_flat
elif key_selection == "5": 
	key = KEY_E
elif key_selection == "6": 
	key = KEY_F
elif key_selection == "7": 
	key = KEY_F_sharp
elif key_selection == "8": 
	key = KEY_G
elif key_selection == "9": 
	key = KEY_G_sharp
elif key_selection == "10": 
	key = KEY_A
elif key_selection == "11": 
	key = KEY_B_flat
elif key_selection == "12": 
	key = KEY_B
else:
	print("Selection not recognized")

print("Enter chord progression (sequence of 1-10, separated by commas) ")
print("Options: ")
print("1: I")
print("2: II")
print("3: III")
print("4: IV")
print("5: V")
print("6: VI")
print("7: VII")
print("8: bVII")
print("9: bVI")
print("10: bIII")

chord_progression = input("Type: ")

print("Enter major/minor sequence for key: ")
print("Options: ")
print("1: I-ii-iii-IV-V-vi-viidim-bVII-bVI-bIII (default)")
print("2: I-II-iii-IV-V-vi-viidim-bVII-bVI-bIII (2-maj)")
print("3: I-ii-III-IV-V-vi-viidim-bVII-bVI-bIII (3-maj)")
print("4: I-II-III-IV-V-vi-viidim-bVII-bVI-bIII (2-3-maj)")
print("5: I-ii-iii-iv-V-vi-viidim-bVII-bVI-bIII (4-min)")
print("6: I-ii-iii-IV-v-vi-viidim-bVII-bVI-bIII (5-min)")

maj_min_sequence = input("Selection: ")

if maj_min_sequence == "1": 
	keyDegrees = [[1,5,8], [1,4,8], [1,4,8], [1,5,8], [1,5,8], [1,4,8], [1,4,7], [1,5,8], [1,5,8], [1,5,8]]
elif maj_min_sequence == "2": 
	keyDegrees = [[1,5,8], [1,5,8], [1,4,8], [1,5,8], [1,5,8], [1,4,8], [1,4,7], [1,5,8], [1,5,8], [1,5,8]]
elif maj_min_sequence == "3": 
	keyDegrees = [[1,5,8], [1,4,8], [1,5,8], [1,5,8], [1,5,8], [1,4,8], [1,4,7], [1,5,8], [1,5,8], [1,5,8]]
elif maj_min_sequence == "4": 
	keyDegrees = [[1,5,8], [1,5,8], [1,5,8], [1,5,8], [1,5,8], [1,4,8], [1,4,7], [1,5,8], [1,5,8], [1,5,8]]
elif maj_min_sequence == "5": 
	keyDegrees = [[1,5,8], [1,4,8], [1,4,8], [1,4,8], [1,5,8], [1,4,8], [1,4,7], [1,5,8], [1,5,8], [1,5,8]]
elif maj_min_sequence == "6": 
	keyDegrees = [[1,5,8], [1,4,8], [1,4,8], [1,5,8], [1,4,8], [1,4,8], [1,4,7], [1,5,8], [1,5,8], [1,5,8]]
else:
	print("Selection not recognized")


print("Chord modifications (y/n): ")
aug_5  = input("#5? ")

if aug_5 == "y": 
	for k in keyDegrees: 
		for i in range(len(k)): 
			if k[i] == 8: 
				k[i] = 9

dim_5  = input("b5? ")

if dim_5 == "y": 
	for k in keyDegrees: 
		for i in range(len(k)): 
			if k[i] == 8: 
				k[i] = 7

sus2  = input("sus2? ")

if sus2 == "y": 
	for k in keyDegrees: 
		for i in range(len(k)): 
			if k[i] == 4 or k[i] == 5: 
				k[i] = 3

sus4  = input("sus4? ")

if sus4 == "y": 
	for k in keyDegrees: 
		for i in range(len(k)): 
			if k[i] == 4 or k[i] == 5: 
				k[i] = 6

print("Extensions (y/n): ")
ext_6 = input("6? ")

if ext_6 == "y": 
	for k in keyDegrees: 
		k.append(10)

ext_9 = input("9? ")

if ext_9 == "y": 
	for k in keyDegrees: 
		k.append(15)

ext_9_sharp = input("#9? ")

if ext_9_sharp == "y": 
	for k in keyDegrees: 
		k.append(16)

ext_9_flat = input("b9? ")

if ext_9_flat == "y": 
	for k in keyDegrees: 
		k.append(14)

ext_7 = input("7? ")

if ext_7 == "y": 
	for k in keyDegrees: 
		k.append(11)

ext_maj7 = input("maj7? ")

if ext_maj7 == "y": 
	for k in keyDegrees: 
		k.append(12)

ext_11 = input("11? ")

if ext_11 == "y": 
	for k in keyDegrees: 
		k.append(18)

ext_11_sharp = input("#11? ")

if ext_11_sharp == "y": 
	for k in keyDegrees: 
		k.append(19)

ext_13 = input("13? ")

if ext_13 == "y": 
	for k in keyDegrees: 
		k.append(22)


repititions = 4

i = 0 
while i < repititions: 

	chordProgression = chord_progression.split(",")

	for c in chordProgression: 

		idx = int(c) - 1

		bass_part, treble_part = pianoPart.get(scaleDegrees=keyDegrees[idx])

		piano_part_notes, piano_part_velocity, piano_part_onoff = pianoPart.compilePianoPart(bass_part, treble_part, key=key[idx])

		piano_segment_notes = np.concatenate((piano_segment_notes, piano_part_notes), axis = 1)
		piano_segment_velocity = np.concatenate((piano_segment_velocity, piano_part_velocity), axis = 1)
		piano_segment_onoff = np.concatenate((piano_segment_onoff, piano_part_onoff), axis = 1)

	piano_notes = np.concatenate((piano_notes, piano_segment_notes), axis = 1)
	piano_velocity = np.concatenate((piano_velocity, piano_segment_velocity), axis = 1)
	piano_onoff = np.concatenate((piano_onoff, piano_segment_onoff), axis = 1)

	i+= 1

filename = "pianoPart" + timestamp +  "_" + str(i)

midiFunctions.createMidiFile(piano_notes, piano_velocity, piano_onoff, 80, filename, "Piano")


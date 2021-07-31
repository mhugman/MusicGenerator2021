# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
import drumPart
import midiFunctions
import mido
import sys
from datetime import datetime
import shutil

TIME_SIG = 4

now = datetime.now()

timestamp = "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)

np.set_printoptions(linewidth=150)
np.set_printoptions(threshold=sys.maxsize)

drum_notes = np.zeros((8,0), dtype=np.int64)
drum_velocity = np.zeros((8,0), dtype=np.int64)
drum_onoff = np.ones((8,0), dtype=np.int64) # all 1's for percussive parts (?)

print("--- Initialize beat ---")
print("Options: ")
print("a: automatically create all new parts")
print("h: input hihat part")
print("r: input ride part")
print("k: input kick part")
print("s: input snare part")

initial_selection = input("Selection: ")

if initial_selection == 'a': 
	user_input = [[], []]
elif initial_selection == 'h': 
	user_input_str = input("Input hihat groove (consisting of " + str(TIME_SIG * 4) + " 0's, 1's and 2's): ")
	user_input = [['h'], [user_input_str]]
elif initial_selection == 'r': 
	user_input_str = input("Input ride groove (consisting of " + str(TIME_SIG * 4) + " 0's, 1's): ")
	user_input = [['r'], [user_input_str]]
elif initial_selection == 'k': 
	user_input_str = input("Input kick groove (consisting of " + str(TIME_SIG * 4) + " 0's, 1's): ")
	user_input = [['k'], [user_input_str]]
elif initial_selection == 's': 
	user_input_str = input("Input snare groove (consisting of " + str(TIME_SIG * 4) + " 0's, 1's): ")
	user_input = [['s'], [user_input_str]]
else:
	print("Selection not recognized")

repititions = 5

i = 0 
while i < repititions: 

	if initial_selection == 'a': 
		whichPartsToCreate = ["hihat", "ride", "kick", "snare", "tom_h", "tom_m", "tom_l", "crash"]
	elif initial_selection == 'h': 
		whichPartsToCreate = ["ride", "kick", "snare", "tom_h", "tom_m", "tom_l", "crash"]
	elif initial_selection == 'r': 
		whichPartsToCreate = ["hihat", "kick", "snare", "tom_h", "tom_m", "tom_l", "crash"]
	elif initial_selection == 'k': 
		whichPartsToCreate = ["hihat", "ride", "snare", "tom_h", "tom_m", "tom_l", "crash"]
	elif initial_selection == 's': 
		whichPartsToCreate = ["hihat", "ride", "kick", "tom_h", "tom_m", "tom_l", "crash"]
	else:
		print("Selection not recognized")

	hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part, \
	hihat_part_fill, ride_part_fill, kick_part_fill, snare_part_fill, tom_h_part_fill, tom_m_part_fill, \
	tom_l_part_fill, crash_part_fill = \
		drumPart.get(whichPartsToCreate=whichPartsToCreate, user_input=user_input)

	print("Without fill: ")
	print(crash_part[0])
	print(ride_part[0])
	print(hihat_part[0])
	print(tom_h_part[0])
	print(tom_m_part[0])
	print(tom_l_part[0])
	print(snare_part[0])
	print(kick_part[0])
	print("--------------------------------")

	print("With fill: ")
	print(crash_part_fill[0])
	print(ride_part_fill[0])
	print(hihat_part_fill[0])
	print(tom_h_part_fill[0])
	print(tom_m_part_fill[0])
	print(tom_l_part_fill[0])
	print(snare_part_fill[0])
	print(kick_part_fill[0])
	print("--------------------------------")

	#print(crash_part[1])
	#print(ride_part[1])
	#print(hihat_part[1])
	#print(tom_h_part[1])
	#print(tom_m_part[1])
	#print(tom_l_part[1])
	#print(snare_part[1])
	#print(kick_part[1])
	#print("----")

	#print(crash_part[2])
	#print(ride_part[2])
	#print(hihat_part[2])
	#print(tom_h_part[2])
	#print(tom_m_part[2])
	#print(tom_l_part[2])
	#print(snare_part[2])
	#print(kick_part[2])
	#print("----")

	selection = input("Modify drum part? y/n: ")

	while selection != 'q' and selection != 'n': 

		print("--- making drum part ---")
		print("Options: ")
		print("a: create all new parts")
		print("h: create new hi hat part")
		print("r: create new ride part")
		print("k: create new kick part")
		print("s: create new snare part")
		print("1: create new high tom part")
		print("2: create new mid tom part")
		print("3: create new low tom part")
		print("t: create all new tom parts")
		print("c: create new crash part")
		print("f: create new fills")
		print("q: quit")

		selection = input("Selection: ")

		whichPartsToCreate = []

		for char in list(selection): 

			if selection == "a": 
				whichPartsToCreate = ["hihat", "ride", "kick", "snare", "tom_h", "tom_m", "tom_l", "crash"]
			elif selection == "f": 
				whichPartsToCreate.append("fills")
			elif selection == "h": 
				whichPartsToCreate.append("hihat")
			elif selection == "r": 
				whichPartsToCreate.append("ride")
			elif selection == "k": 
				whichPartsToCreate.append("kick")
			elif selection == "s": 
				whichPartsToCreate.append("snare")
			elif selection == "1": 
				whichPartsToCreate.append("tom_h")
			elif selection == "2": 
				whichPartsToCreate.append("tom_m")
			elif selection == "3": 
				whichPartsToCreate.append("tom_l")
			elif selection == "t": 
				whichPartsToCreate.append("tom_l")
				whichPartsToCreate.append("tom_m")
				whichPartsToCreate.append("tom_h")
			elif selection == "c": 
				whichPartsToCreate.append("crash")
			else: 
				print("Selection not recognized")

		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part, \
			hihat_part_fill, ride_part_fill, kick_part_fill, snare_part_fill, tom_h_part_fill, tom_m_part_fill, \
			tom_l_part_fill, crash_part_fill = \
			drumPart.get(hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part, \
			hihat_part_fill, ride_part_fill, kick_part_fill, snare_part_fill, tom_h_part_fill, tom_m_part_fill, \
			tom_l_part_fill, crash_part_fill, whichPartsToCreate=whichPartsToCreate)
		
		print("Without fill: ")
		print(crash_part[0])
		print(ride_part[0])
		print(hihat_part[0])
		print(tom_h_part[0])
		print(tom_m_part[0])
		print(tom_l_part[0])
		print(snare_part[0])
		print(kick_part[0])
		print("--------------------------------")

		print("With fill: ")
		print(crash_part_fill[0])
		print(ride_part_fill[0])
		print(hihat_part_fill[0])
		print(tom_h_part_fill[0])
		print(tom_m_part_fill[0])
		print(tom_l_part_fill[0])
		print(snare_part_fill[0])
		print(kick_part_fill[0])
		print("--------------------------------")

		#print(crash_part[1])
		#print(ride_part[1])
		#print(hihat_part[1])
		#print(tom_h_part[1])
		#print(tom_m_part[1])
		#print(tom_l_part[1])
		#print(snare_part[1])
		#print(kick_part[1])
		#print("----")

		#print(crash_part[2])
		#print(ride_part[2])
		#print(hihat_part[2])
		#print(tom_h_part[2])
		#print(tom_m_part[2])
		#print(tom_l_part[2])
		#print(snare_part[2])
		#print(kick_part[2])
		print("----------------------")

	drum_part_notes, drum_part_velocity, drum_part_onoff = \
	drumPart.compileDrumPart(hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part)

	drum_part_notes_fill, drum_part_velocity_fill, drum_part_onoff_fill = \
	drumPart.compileDrumPart(hihat_part_fill, ride_part_fill, kick_part_fill, snare_part_fill, tom_h_part_fill, tom_m_part_fill, tom_l_part_fill, crash_part_fill)

	print("Select structure of drum segment: ")
	print("Options: ")
	print("1: AAAB")
	print("2: ABAB")
	print("3: AABA")
	print("4: ABAA")
	print("5: ABBA")
	print("6: AAB")
	print("7: ABA")
	print("8: ABB")
	print("9: AAAAB")
	print("10: AAABB")
	print("11: AABBA")
	print("12: ABBAA")
	print("13: ABABA")
	structure_selection = input("Selection: ")

	if structure_selection == "1": 
		structure = "AAAB"
	elif structure_selection == "2": 
		structure = "ABAB"
	elif structure_selection == "3": 
		structure = "AABA"
	elif structure_selection == "4": 
		structure = "ABAA"
	elif structure_selection == "5": 
		structure = "ABBA"
	elif structure_selection == "6": 
		structure = "AAB"
	elif structure_selection == "7": 
		structure = "ABA"
	elif structure_selection == "8": 
		structure = "ABB"
	elif structure_selection == "9": 
		structure = "AAAAB"
	elif structure_selection == "10": 
		structure = "AAABB"
	elif structure_selection == "11": 
		structure = "AABBA"
	elif structure_selection == "12": 
		structure = "ABBAA"
	elif structure_selection == "13": 
		structure = "ABABA"
	else:
		print("Selection not recognized")

	drum_segment_notes, drum_segment_velocity, drum_segment_onoff = \
		drumPart.createDrumSegmentFromTwoParts(drum_part_notes, drum_part_velocity, drum_part_onoff, \
		drum_part_notes_fill, drum_part_velocity_fill, drum_part_onoff_fill, 
		structure)

	print(drum_segment_notes[0])
	print(drum_segment_notes[1])
	print(drum_segment_notes[2])
	print(drum_segment_notes[3])
	print(drum_segment_notes[4])
	print(drum_segment_notes[5])
	print(drum_segment_notes[6])
	print(drum_segment_notes[7])
	print("--------------------------------")

	filename = "drumPart" + timestamp +  "_" + str(i)

	midiFunctions.createMidiFile(drum_segment_notes, drum_segment_velocity, drum_segment_onoff, 80, filename)

	noteArray, velocityArray, onOffArray = midiFunctions.parseMidi(mido.MidiFile('midi/' + filename + '.mid'))

	"""
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
	"""

	drum_notes = np.concatenate((drum_notes, drum_segment_notes, np.zeros((8,TIME_SIG * 4), dtype=np.int64)), axis = 1)
	drum_velocity = np.concatenate((drum_velocity, drum_segment_velocity, np.zeros((8, TIME_SIG * 4), dtype=np.int64)), axis = 1)
	drum_onoff = np.concatenate((drum_onoff, drum_segment_onoff, np.zeros((8,TIME_SIG * 4), dtype=np.int64)), axis = 1)

	i+= 1

midiFunctions.createMidiFile(drum_notes, drum_velocity, drum_onoff, 80, "drumPart_final" + timestamp)

shutil.copyfile("drumPart.py", "midi/drumPart_saved" + timestamp + ".py")

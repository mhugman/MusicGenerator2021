# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
import drumPart
import midiFunctions
import mido
import sys

np.set_printoptions(linewidth=150)
np.set_printoptions(threshold=sys.maxsize)

whichPartsToCreate = ["hihat", "ride", "kick", "snare", "tom_h", "tom_m", "tom_l", "crash"]

hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
	drumPart.get(whichPartsToCreate=whichPartsToCreate)

print(crash_part[0])
print(ride_part[0])
print(hihat_part[0])
print(tom_h_part[0])
print(tom_m_part[0])
print(tom_l_part[0])
print(snare_part[0])
print(kick_part[0])
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
		elif selection == "t1": 
			whichPartsToCreate.append("tom_h")
		elif selection == "t2": 
			whichPartsToCreate.append("tom_m")
		elif selection == "t3": 
			hwhichPartsToCreate.append("tom_l")
		elif selection == "c": 
			whichPartsToCreate.append("crash")

	hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = drumPart.get( \
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part, whichPartsToCreate=whichPartsToCreate)

	print(crash_part[0])
	print(ride_part[0])
	print(hihat_part[0])
	print(tom_h_part[0])
	print(tom_m_part[0])
	print(tom_l_part[0])
	print(snare_part[0])
	print(kick_part[0])
	print("----")

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
drumPart.createCompleteDrumPart(hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part)

midiFunctions.createMidiFile(drum_part_notes, drum_part_velocity, drum_part_onoff, 80, "drumPart1")

noteArray, velocityArray, onOffArray = midiFunctions.parseMidi(mido.MidiFile('midi/drumPart1.mid'))

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




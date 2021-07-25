# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
import drumPart

whichPartsToCreate = ["hihat", "ride", "kick", "snare", "tom_h", "tom_m", "tom_l", "crash"]

hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
	drumPart.get(whichPartsToCreate=whichPartsToCreate)

print(crash_part)
print(ride_part)
print(hihat_part)
print(tom_h_part)
print(tom_m_part)
print(tom_l_part)
print(snare_part)
print(kick_part)
print("----")

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

	print(crash_part)
	print(ride_part)
	print(hihat_part)
	print(tom_h_part)
	print(tom_m_part)
	print(tom_l_part)
	print(snare_part)
	print(kick_part)
	print("----")


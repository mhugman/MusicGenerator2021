# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
import drumPart

hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = drumPart.get()

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

while selection != 'n': 

	print("--- making drum part ---")
	print("Options: ")
	print("a: create all new parts")
	print("h: create new hi hat part")
	print("r: create new ride part")
	print("k: create new kick part")
	print("s: create new snare part")
	print("t1: create new high tom part")
	print("t2: create new mid tom part")
	print("t3: create new low tom part")
	print("c: create new crash part")
	print("n: quit")

	selection = input("Selection: ")

	if selection == "a": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = drumPart.get()
	elif selection == "h": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(             ride_part = ride_part, kick_part = kick_part, snare_part = snare_part, \
		 tom_h_part = tom_h_part, tom_m_part = tom_m_part, tom_l_part = tom_l_part, crash_part = crash_part)
	elif selection == "r": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(hihat_part = hihat_part,              kick_part = kick_part, snare_part = snare_part, \
		 tom_h_part = tom_h_part, tom_m_part = tom_m_part, tom_l_part = tom_l_part, crash_part = crash_part)
	elif selection == "k": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(hihat_part = hihat_part, ride_part = ride_part,               snare_part = snare_part, \
		 tom_h_part = tom_h_part, tom_m_part = tom_m_part, tom_l_part = tom_l_part, crash_part = crash_part)
	elif selection == "s": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(hihat_part = hihat_part, ride_part = ride_part, kick_part = kick_part,            \
		 tom_h_part = tom_h_part, tom_m_part = tom_m_part, tom_l_part = tom_l_part, crash_part = crash_part)
	elif selection == "t1": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(hihat_part = hihat_part, ride_part = ride_part, kick_part = kick_part, snare_part = snare_part, \
		                          tom_m_part = tom_m_part, tom_l_part = tom_l_part, crash_part = crash_part)
	elif selection == "t2": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(hihat_part = hihat_part, ride_part = ride_part, kick_part = kick_part, snare_part = snare_part, \
		 tom_h_part = tom_h_part,                          tom_l_part = tom_l_part, crash_part = crash_part)
	elif selection == "t3": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(hihat_part = hihat_part, ride_part = ride_part, kick_part = kick_part, snare_part = snare_part, \
		 tom_h_part = tom_h_part, tom_m_part = tom_m_part,                           crash_part = crash_part)
	elif selection == "c": 
		hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part = \
		drumPart.get(hihat_part = hihat_part, ride_part = ride_part, kick_part = kick_part, snare_part = snare_part, \
		 tom_h_part = tom_h_part, tom_m_part = tom_m_part, tom_l_part = tom_l_part,                         )

	print(crash_part)
	print(ride_part)
	print(hihat_part)
	print(tom_h_part)
	print(tom_m_part)
	print(tom_l_part)
	print(snare_part)
	print(kick_part)
	print("----")


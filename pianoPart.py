# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools
from globals import TIME_SIG

np.set_printoptions(linewidth=150)

'''

Scale key: 

1: 1 (root)
2: b2
3: 2
4: b3
5: 3
6: 4
7: b5
8: 5
9: #5
10: 6
11: b7
12: 7
13: 8 (root up one octave)
14: b9 (b2 up one octave)
15: 9 (2 up one octave)
16: #9 (b3 up one octave)
17: b11 (3 up on octave)
18: 11 (4 up one octave)
19: #11 (b5 up one octave)
20: ? (5 up one octave)
21: b13 (#5 up one octave)
22: 13 (6 up one octave)
23: #13 (b7 up one octave)


'''

NUM_16th_PER_BAR = TIME_SIG * 4

BASS_ON = True
TREBLE_ON = True

BASS_VOL = 90
TREBLE_VOL = 90

BASS_OCT = 3
TREBLE_OCT = 6

BASS_RHYTHM_PROB = 0.4
TREBLE_RHYTHM_PROB = 0.5

BASS_REPEATED = True
TREBLE_REPEATED = True

BASS_REPEAT_UNIT = 4
TREBLE_REPEAT_UNIT = 8

BASS_RANDOM= True
TREBLE_RANDOM = True

TREBLE_WHOLE_NOTES = False
TREBLE_HALF_NOTES = False
TREBLE_QUARTER_NOTES = False
TREBLE_EIGHTH_NOTES = False
TREBLE_SIXTEENTH_NOTES = False

BASS_WHOLE_NOTES = False
BASS_HALF_NOTES = False
BASS_QUARTER_NOTES = False
BASS_EIGHTH_NOTES = False
BASS_SIXTEENTH_NOTES = False


def get(scaleDegrees = [1,5,8,12]) : 

	bass_part = np.zeros((4,NUM_16th_PER_BAR), dtype=np.int64)
	treble_part = np.zeros((6,NUM_16th_PER_BAR), dtype=np.int64)

	base_rhythm_bass = np.zeros((1,NUM_16th_PER_BAR), dtype=np.int64)
	base_rhythm_treble = np.zeros((1,NUM_16th_PER_BAR), dtype=np.int64)

	base_notes_bass = np.zeros((1,NUM_16th_PER_BAR), dtype=np.int64)
	base_notes_treble = np.zeros((3,NUM_16th_PER_BAR), dtype=np.int64)

	base_octave_bass = np.zeros((1,NUM_16th_PER_BAR), dtype=np.int64)
	base_octave_treble = np.zeros((1,NUM_16th_PER_BAR), dtype=np.int64)

	if BASS_ON: 
		if BASS_RANDOM and BASS_REPEATED: 

			if NUM_16th_PER_BAR >= 4 and BASS_REPEAT_UNIT == 4: 
				micro_rhythm_bass = np.random.binomial(2, BASS_RHYTHM_PROB, size=(1,4))
				micro_notes_bass = np.random.choice(scaleDegrees, size=(1,4))

				if TIME_SIG == 4: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_rnotes_bass, micro_notes_bass), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass), axis=1)
			elif NUM_16th_PER_BAR >= 8 and BASS_REPEAT_UNIT == 8: 
				micro_rhythm_bass = np.random.binomial(2, BASS_RHYTHM_PROB, size=(1,8))
				micro_notes_bass = np.random.choice(scaleDegrees, size=(1,8))
				if TIME_SIG == 4: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, np.zeros((3,4), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, np.zeros((3,4), dtype=np.int64)), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,4), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, np.zeros((1,4), dtype=np.int64)), axis=1)

			elif NUM_16th_PER_BAR >= 3 and BASS_REPEAT_UNIT == 3: 
				micro_rhythm_bass = np.random.binomial(2, BASS_RHYTHM_PROB, size=(1,3))
				micro_notes_bass = np.random.choice(scaleDegrees, size=(1,3))
				if TIME_SIG == 4: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,1), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass, np.zeros((1,1), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
			elif NUM_16th_PER_BAR >= 5 and BASS_REPEAT_UNIT == 5: 
				micro_rhythm_bass = np.random.binomial(2, BASS_RHYTHM_PROB, size=(1,5))
				micro_notes_bass = np.random.choice(scaleDegrees, size=(1,5))
				if TIME_SIG == 4: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,1), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, np.zeros((1,1), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, micro_notes_bass), axis=1)
			elif NUM_16th_PER_BAR >= 7 and BASS_REPEAT_UNIT == 7: 
				micro_rhythm_bass = np.random.binomial(2, BASS_RHYTHM_PROB, size=(1,7))
				micro_notes_bass = np.random.choice(scaleDegrees, size=(1,7))
				
				if TIME_SIG == 4: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, np.zeros((1,5), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, np.zeros((1,5), dtype=np.int64)), axis=1)
				elif TIME_SIG == 5 : 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,6), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, np.zeros((1,6), dtype=np.int64)), axis=1)

			elif NUM_16th_PER_BAR >= 6 and BASS_REPEAT_UNIT == 6: 
				micro_rhythm_bass = np.random.binomial(2, BASS_RHYTHM_PROB, size=(1,7))
				micro_notes_bass = np.random.choice(scaleDegrees, size=(1,7))
				if TIME_SIG == 4: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,4), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, np.zeros((1,4), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_bass = np.concatenate((micro_rhythm_bass, micro_rhythm_bass, micro_rhythm_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_bass = np.concatenate((micro_notes_bass, micro_notes_bass, micro_notes_bass, np.zeros((1,2), dtype=np.int64)), axis=1)
			else: 
				print("repeat unit not accounted for")

		elif BASS_RANDOM: 
			base_rhythm_bass = np.random.binomial(2, BASS_RHYTHM_PROB, size=(1,NUM_16th_PER_BAR))
			base_rhythm_bass = np.random.choice(scaleDegrees, size=(1,NUM_16th_PER_BAR))
		else: 
			print("Case not accounted for")

	if TREBLE_ON: 
		if TREBLE_RANDOM and TREBLE_REPEATED: 

			if NUM_16th_PER_BAR >= 4 and TREBLE_REPEAT_UNIT == 4: 
				micro_rhythm_treble = np.random.binomial(2, TREBLE_RHYTHM_PROB, size=(1,4))
				micro_notes_treble = np.random.choice(scaleDegrees, size=(3,4))

				if TIME_SIG == 4: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_rnotes_treble, micro_notes_treble), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble), axis=1)
			elif NUM_16th_PER_BAR >= 8 and TREBLE_REPEAT_UNIT == 8: 
				micro_rhythm_treble = np.random.binomial(2, TREBLE_RHYTHM_PROB, size=(1,8))
				micro_notes_treble = np.random.choice(scaleDegrees, size=(3,8))
				if TIME_SIG == 4: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, np.zeros((3,4), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, np.zeros((3,4), dtype=np.int64)), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,4), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, np.zeros((1,4), dtype=np.int64)), axis=1)

			elif NUM_16th_PER_BAR >= 3 and TREBLE_REPEAT_UNIT == 3: 
				micro_rhythm_treble = np.random.binomial(2, TREBLE_RHYTHM_PROB, size=(1,3))
				micro_notes_treble = np.random.choice(scaleDegrees, size=(3,3))
				if TIME_SIG == 4: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,1), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble, np.zeros((1,1), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
			elif NUM_16th_PER_BAR >= 5 and TREBLE_REPEAT_UNIT == 5: 
				micro_rhythm_treble = np.random.binomial(2, TREBLE_RHYTHM_PROB, size=(1,5))
				micro_notes_treble = np.random.choice(scaleDegrees, size=(3,5))
				if TIME_SIG == 4: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,1), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, np.zeros((1,1), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, micro_notes_treble), axis=1)
			elif NUM_16th_PER_BAR >= 7 and TREBLE_REPEAT_UNIT == 7: 
				micro_rhythm_treble = np.random.binomial(2, TREBLE_RHYTHM_PROB, size=(1,7))
				micro_notes_treble = np.random.choice(scaleDegrees, size=(3,7))
				
				if TIME_SIG == 4: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, np.zeros((1,5), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, np.zeros((1,5), dtype=np.int64)), axis=1)
				elif TIME_SIG == 5 : 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,6), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, np.zeros((1,6), dtype=np.int64)), axis=1)

			elif NUM_16th_PER_BAR >= 6 and TREBLE_REPEAT_UNIT == 6: 
				micro_rhythm_treble = np.random.binomial(2, TREBLE_RHYTHM_PROB, size=(1,7))
				micro_notes_treble = np.random.choice(scaleDegrees, size=(3,7))
				if TIME_SIG == 4: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,4), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, np.zeros((1,4), dtype=np.int64)), axis=1)
				elif TIME_SIG == 3: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble), axis=1)
				elif TIME_SIG == 5: 
					base_rhythm_treble = np.concatenate((micro_rhythm_treble, micro_rhythm_treble, micro_rhythm_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
					base_notes_treble = np.concatenate((micro_notes_treble, micro_notes_treble, micro_notes_treble, np.zeros((1,2), dtype=np.int64)), axis=1)
			else: 
				print("repeat unit not accounted for")

		elif TREBLE_RANDOM: 
			base_rhythm_treble = np.random.binomial(2, TREBLE_RHYTHM_PROB, size=(1,NUM_16th_PER_BAR))
			base_notes_treble = np.random.choice(scaleDegrees, size=(3,NUM_16th_PER_BAR))
		else: 
			print("Case not accounted for")

	bass_part[0].fill(BASS_VOL)
	treble_part[0].fill(TREBLE_VOL)

	bass_part[1] = base_rhythm_bass[0]
	treble_part[1] = base_rhythm_treble[0]

	bass_part[2].fill(BASS_OCT)
	treble_part[2].fill(TREBLE_OCT)

	bass_part[3] = base_notes_bass[0]
	treble_part[3] = base_notes_treble[0]

	treble_part[4] = base_notes_treble[1]

	treble_part[5] = base_notes_treble[2]

	return bass_part, treble_part


def compilePianoPart(bass_part, treble_part, key = "C"): 

	if key == "C": 

		noteDict_0 = {}
		noteDict_1 = {}
		noteDict_2 = {}
		noteDict_3 = {}
		noteDict_4 = {}
		noteDict_5 = {}
		noteDict_6 = {}
		noteDict_7 = {}
		noteDict_8 = {}

		startingNote_0 = 0
		startingNote_1 = 12
		startingNote_2 = 24
		startingNote_3 = 36
		startingNote_4 = 48
		startingNote_5 = 60
		startingNote_6 = 72
		startingNote_7 = 84
		startingNote_8 = 96

		for i in range(23): 
			noteDict_0[i + 1] = startingNote_0 + i
			noteDict_1[i + 1] = startingNote_1 + i
			noteDict_2[i + 1] = startingNote_2 + i
			noteDict_3[i + 1] = startingNote_3 + i
			noteDict_4[i + 1] = startingNote_4 + i
			noteDict_5[i + 1] = startingNote_5 + i
			noteDict_6[i + 1] = startingNote_6 + i
			noteDict_7[i + 1] = startingNote_7 + i
			noteDict_8[i + 1] = startingNote_8 + i

	else: 
		print("Key not accounted for")

	piano_part_notes = np.zeros((4,NUM_16th_PER_BAR), dtype=np.int64)
	piano_part_velocity = np.zeros((4,NUM_16th_PER_BAR), dtype=np.int64)
	piano_part_onoff = np.zeros((4,NUM_16th_PER_BAR), dtype=np.int64) 

	# https://stackoverflow.com/questions/3403973/fast-replacement-of-values-in-a-numpy-array
	bass_notes = np.copy(bass_part[3])
	for k, v in noteDict_3.items(): bass_notes[bass_part[3]==k] = v

	treble_notes_1 = np.copy(treble_part[3])
	for k, v in noteDict_6.items(): treble_notes_1[treble_part[3]==k] = v

	treble_notes_2 = np.copy(treble_part[4])
	for k, v in noteDict_6.items(): treble_notes_2[treble_part[4]==k] = v

	treble_notes_3 = np.copy(treble_part[5])
	for k, v in noteDict_6.items(): treble_notes_3[treble_part[5]==k] = v

	piano_part_notes[0] = bass_notes
	piano_part_notes[1] = treble_notes_1
	piano_part_notes[2] = treble_notes_2
	piano_part_notes[3] = treble_notes_3

	piano_part_velocity[0] = bass_part[0]
	piano_part_velocity[1] = treble_part[0]
	piano_part_velocity[2] = treble_part[0]
	piano_part_velocity[3] = treble_part[0]

	piano_part_onoff[0] = bass_part[1]
	piano_part_onoff[1] = treble_part[1]
	piano_part_onoff[2] = treble_part[1]
	piano_part_onoff[3] = treble_part[1]

	return piano_part_notes, piano_part_velocity, piano_part_onoff

	
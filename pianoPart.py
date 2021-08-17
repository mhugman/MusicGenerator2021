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

	

	noteDict_0 = {}
	noteDict_1 = {}
	noteDict_2 = {}
	noteDict_3 = {}
	noteDict_4 = {}
	noteDict_5 = {}
	noteDict_6 = {}
	noteDict_7 = {}
	noteDict_8 = {}

	if key == "C": 

		startingNote_0 = 0
		startingNote_1 = 12
		startingNote_2 = 24
		startingNote_3 = 36
		startingNote_4 = 48
		startingNote_5 = 60
		startingNote_6 = 72
		startingNote_7 = 84
		startingNote_8 = 96
	elif key == "C#": 

		startingNote_0 = 1
		startingNote_1 = 13
		startingNote_2 = 25
		startingNote_3 = 37
		startingNote_4 = 49
		startingNote_5 = 61
		startingNote_6 = 73
		startingNote_7 = 85
		startingNote_8 = 97
	elif key == "D": 
		startingNote_0 = 2
		startingNote_1 = 14
		startingNote_2 = 26
		startingNote_3 = 38
		startingNote_4 = 50
		startingNote_5 = 62
		startingNote_6 = 74
		startingNote_7 = 86
		startingNote_8 = 98
	elif key == "Eb": 
		startingNote_0 = 3
		startingNote_1 = 15
		startingNote_2 = 27
		startingNote_3 = 39
		startingNote_4 = 51
		startingNote_5 = 63
		startingNote_6 = 75
		startingNote_7 = 87
		startingNote_8 = 99
	elif key == "E": 
		startingNote_0 = 4
		startingNote_1 = 16
		startingNote_2 = 28
		startingNote_3 = 40
		startingNote_4 = 52
		startingNote_5 = 64
		startingNote_6 = 76
		startingNote_7 = 88
		startingNote_8 = 100
	elif key == "F": 
		startingNote_0 = 5
		startingNote_1 = 17
		startingNote_2 = 29
		startingNote_3 = 41
		startingNote_4 = 53
		startingNote_5 = 65
		startingNote_6 = 77
		startingNote_7 = 89
		startingNote_8 = 101
	elif key == "F#": 
		startingNote_0 = 6
		startingNote_1 = 18
		startingNote_2 = 30
		startingNote_3 = 42
		startingNote_4 = 54
		startingNote_5 = 66
		startingNote_6 = 78
		startingNote_7 = 90
		startingNote_8 = 102
	elif key == "G": 
		startingNote_0 = 7
		startingNote_1 = 19
		startingNote_2 = 31
		startingNote_3 = 43
		startingNote_4 = 55
		startingNote_5 = 67
		startingNote_6 = 79
		startingNote_7 = 91
		startingNote_8 = 103
	elif key == "G#": 
		startingNote_0 = 8
		startingNote_1 = 20
		startingNote_2 = 32
		startingNote_3 = 44
		startingNote_4 = 56
		startingNote_5 = 68
		startingNote_6 = 80
		startingNote_7 = 92
		startingNote_8 = 104
	elif key == "A": 
		startingNote_0 = 9
		startingNote_1 = 21
		startingNote_2 = 33
		startingNote_3 = 45
		startingNote_4 = 57
		startingNote_5 = 69
		startingNote_6 = 81
		startingNote_7 = 93
		startingNote_8 = 105
	elif key == "Bb": 
		startingNote_0 = 10
		startingNote_1 = 22
		startingNote_2 = 34
		startingNote_3 = 46
		startingNote_4 = 58
		startingNote_5 = 70
		startingNote_6 = 82
		startingNote_7 = 94
		startingNote_8 = 106
	elif key == "B": 
		startingNote_0 = 11
		startingNote_1 = 23
		startingNote_2 = 35
		startingNote_3 = 47
		startingNote_4 = 59
		startingNote_5 = 71
		startingNote_6 = 83
		startingNote_7 = 95
		startingNote_8 = 107

	else: 
		print("Key not accounted for")

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

	
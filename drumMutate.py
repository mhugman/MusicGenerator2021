import numpy as np
from globals import NUM_BARS_IN_PART
from globals import TIME_SIG
import random

NUM_16th_PER_BAR = TIME_SIG * 4

def get(
	kick_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64),
	snare_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64),
	hihat_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64), 
	ride_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64), 
	tom_h_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64), 
	tom_m_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64), 
	tom_l_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64), 
	crash_part = np.zeros((3,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64), 

	whichPartsToMutate = [], 

	sample_size = 1, 
	complexify = True, 
	simplify = True

	): 


	random_val_1 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_2 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_3 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_4 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_5 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_6 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_7 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_8 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)

	random_val_9 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_10 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_11 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_12 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_13 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_14 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_15 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)
	random_val_16 = random.sample(list(range(NUM_BARS_IN_PART * NUM_16th_PER_BAR)), sample_size)

	random_indices_1 = []
	random_indices_2 = []
	random_indices_3 = []
	random_indices_4 = []
	random_indices_5 = []
	random_indices_6 = []
	random_indices_7 = []
	random_indices_8 = []

	random_indices_9 = []
	random_indices_10 = []
	random_indices_11 = []
	random_indices_12 = []
	random_indices_13 = []
	random_indices_14 = []
	random_indices_15 = []
	random_indices_16 = []

	for v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16 in \
		zip(random_val_1, random_val_2, random_val_3, random_val_4, random_val_5, random_val_6, random_val_7, random_val_8, \
			random_val_9, random_val_10, random_val_11, random_val_12, random_val_13, random_val_14, random_val_15, random_val_16): 
		random_indices_1.append([0,v1])
		random_indices_2.append([0,v2])
		random_indices_3.append([0,v3])
		random_indices_4.append([0,v4])
		random_indices_5.append([0,v5])
		random_indices_6.append([0,v6])
		random_indices_7.append([0,v7])
		random_indices_8.append([0,v8])

		random_indices_9.append([0,v9])
		random_indices_10.append([0,v10])
		random_indices_11.append([0,v11])
		random_indices_12.append([0,v12])
		random_indices_13.append([0,v13])
		random_indices_14.append([0,v14])
		random_indices_15.append([0,v15])
		random_indices_16.append([0,v16])

		print("----- RANDOM INDICES 1 -----")
		print(random_indices_1)

	if complexify: 
		if "ride" in whichPartsToMutate:
			ride_part[0][np.asarray(random_indices_1)] = 1
		if "crash" in whichPartsToMutate:
			crash_part[0][np.asarray(random_indices_2)] = 1
		if "hihat" in whichPartsToMutate:
			hihat_part[0][np.asarray(random_indices_3)] = 1
		if "tom_h" in whichPartsToMutate:
			tom_h_part[0][np.asarray(random_indices_4)] = 1
		if "tom_m" in whichPartsToMutate:
			tom_m_part[0][np.asarray(random_indices_5)] = 1
		if "tom_l" in whichPartsToMutate:
			tom_l_part[0][np.asarray(random_indices_6)] = 1
		if "snare" in whichPartsToMutate: 
			snare_part[0][np.asarray(random_indices_7)] = 1
		if "kick" in whichPartsToMutate:
			print(np.asarray(random_indices_8))
			kick_part[0][np.asarray(random_indices_8)] = 1

	if simplify: 
		if "ride" in whichPartsToMutate:
			ride_part[0][np.asarray(random_indices_9)] = 0
		if "crash" in whichPartsToMutate:
			crash_part[0][np.asarray(random_indices_10)] = 0
		if "hihat" in whichPartsToMutate:
			hihat_part[0][np.asarray(random_indices_11)] = 0
		if "tom_h" in whichPartsToMutate:
			tom_h_part[0][np.asarray(random_indices_12)] = 0
		if "tom_m" in whichPartsToMutate:
			tom_m_part[0][np.asarray(random_indices_13)] = 0
		if "tom_l" in whichPartsToMutate:
			tom_l_part[0][np.asarray(random_indices_14)] = 0
		if "snare" in whichPartsToMutate: 
			snare_part[0][np.asarray(random_indices_15)] = 0
		if "kick" in whichPartsToMutate:
			kick_part[0][np.asarray(random_indices_16)] = 0

	return kick_part, snare_part, hihat_part, ride_part, tom_h_part, tom_m_part, tom_l_part, crash_part

def compileDrumPart(hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part):

	indices_1 = np.where(np.logical_and(np.greater_equal(hihat_part[0],0.9),np.less_equal(hihat_part[0],1.1)))
	indices_2 = np.where(np.logical_and(np.greater_equal(hihat_part[0],1.9),np.less_equal(hihat_part[0],2.1)))
	hihat_part[0][indices_1] = 42
	hihat_part[0][indices_2] = 46

	indices = np.where(np.greater_equal(snare_part[0],0.9))
	snare_part[0][indices] = 38

	indices = np.where(np.greater_equal(ride_part[0],0.9))
	ride_part[0][indices] = 51

	indices = np.where(np.greater_equal(kick_part[0],0.9))
	kick_part[0][indices] = 36

	indices = np.where(np.greater_equal(tom_h_part[0],0.9))
	tom_h_part[0][indices] = 48

	indices = np.where(np.greater_equal(tom_m_part[0],0.9))
	tom_m_part[0][indices] = 47

	indices = np.where(np.greater_equal(tom_l_part[0],0.9))
	tom_l_part[0][indices] = 41

	indices = np.where(np.greater_equal(crash_part[0],0.9))
	crash_part[0][indices] = 49

	# 0: kick
	# 1: snare
	# 2: hihat
	# 3: ride
	# 4: tom_h
	# 5: tom_m
	# 6: tom_l
	# 7: crash

	drum_part_notes = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64)
	drum_part_velocity = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64)
	drum_part_onoff = np.ones((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR), dtype=np.int64) # all 1's for percussive parts (?)

	print("---------------------")
	print(drum_part_notes.shape)
	print(kick_part.shape)

	drum_part_notes[0] = kick_part[0]
	drum_part_notes[1] = snare_part[0]
	drum_part_notes[2] = hihat_part[0]
	drum_part_notes[3] = ride_part[0]
	drum_part_notes[4] = tom_h_part[0]
	drum_part_notes[5] = tom_m_part[0]
	drum_part_notes[6] = tom_l_part[0]
	drum_part_notes[7] = crash_part[0]

	drum_part_velocity[0] = kick_part[1]
	drum_part_velocity[1] = snare_part[1]
	drum_part_velocity[2] = hihat_part[1]
	drum_part_velocity[3] = ride_part[1]
	drum_part_velocity[4] = tom_h_part[1]
	drum_part_velocity[5] = tom_m_part[1]
	drum_part_velocity[6] = tom_l_part[1]
	drum_part_velocity[7] = crash_part[1]

	return drum_part_notes, drum_part_velocity, drum_part_onoff

def createDrumComplete(notes, velocities, onoffs, structure = "AABBCCDDAABB"): 

	part_A_notes = notes[0]
	part_A_velocity = velocities[0]
	part_A_onoff = onoffs[0]

	part_B_notes = notes[1]
	part_B_velocity = velocities[1]
	part_B_onoff = onoffs[1]

	part_C_notes = notes[2]
	part_C_velocity = velocities[2]
	part_C_onoff = onoffs[2]

	part_D_notes = notes[3]
	part_D_velocity = velocities[3]
	part_D_onoff = onoffs[3]

	if structure == "AABBCCDDAABB": 
		segment_length = 4
		num_segments = 3
	elif structure == "AABAABCCD":
		segment_length = 3
		num_segments = 3
	elif structure == "AABAAABACCDCAABA": 
		segment_length = 4
		num_segments = 4
	elif structure == "ABABCDCDABABCDCD": 
		segment_length = 4
		num_segments = 4
	elif structure == "ABACDCABACDC": 
		segment_length = 3
		num_segments = 4


	drum_segment_notes_1 = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length), dtype=np.int64)
	drum_segment_velocity_1 = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length), dtype=np.int64)
	drum_segment_onoff_1 = np.ones((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length), dtype=np.int64) # all 1's for percussive parts (?)

	drum_segment_notes_2 = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length), dtype=np.int64)
	drum_segment_velocity_2 = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length), dtype=np.int64)
	drum_segment_onoff_2 = np.ones((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length), dtype=np.int64) # all 1's for percussive parts (?)

	drum_complete_notes = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length * num_segments), dtype=np.int64)
	drum_complete_velocity = np.zeros((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length * num_segments), dtype=np.int64)
	drum_complete_onoff = np.ones((8,NUM_BARS_IN_PART * NUM_16th_PER_BAR * segment_length * num_segments), dtype=np.int64) # all 1's for percussive parts (?)

	if structure == "AABBCCDDAABB": 

		drum_segment_notes_1 = np.concatenate((part_A_notes, part_A_notes, part_B_notes, part_B_notes), axis = 1)
		drum_segment_velocity_1 = np.concatenate((part_A_velocity, part_A_velocity, part_B_velocity, part_B_velocity), axis = 1)
		drum_segment_onoff_1 = np.concatenate((part_A_onoff, part_A_onoff, part_B_onoff, part_B_onoff), axis = 1)

		drum_segment_notes_2 = np.concatenate((part_C_notes, part_C_notes, part_D_notes, part_D_notes), axis = 1)
		drum_segment_velocity_2 = np.concatenate((part_C_velocity, part_C_velocity, part_D_velocity, part_D_velocity), axis = 1)
		drum_segment_onoff_2 = np.concatenate((part_C_onoff, part_C_onoff, part_D_onoff, part_D_onoff), axis = 1)

		drum_complete_notes = np.concatenate((drum_segment_notes_1, drum_segment_notes_2, drum_segment_notes_1), axis = 1)
		drum_complete_velocity = np.concatenate((drum_segment_velocity_1, drum_segment_velocity_2, drum_segment_velocity_1), axis = 1)
		drum_complete_onoff = np.concatenate((drum_segment_onoff_1, drum_segment_onoff_2, drum_segment_onoff_1), axis = 1)

	elif structure == "AABAABCCD": 

		drum_segment_notes_1 = np.concatenate((part_A_notes, part_A_notes, part_B_notes), axis = 1)
		drum_segment_velocity_1 = np.concatenate((part_A_velocity, part_A_velocity, part_B_velocity), axis = 1)
		drum_segment_onoff_1 = np.concatenate((part_A_onoff, part_A_onoff, part_B_onoff), axis = 1)

		drum_segment_notes_2 = np.concatenate((part_C_notes, part_C_notes, part_D_notes), axis = 1)
		drum_segment_velocity_2 = np.concatenate((part_C_velocity, part_C_velocity, part_D_velocity), axis = 1)
		drum_segment_onoff_2 = np.concatenate((part_C_onoff, part_C_onoff, part_D_onoff), axis = 1)

		drum_complete_notes = np.concatenate((drum_segment_notes_1, drum_segment_notes_1, drum_segment_notes_2), axis = 1)
		drum_complete_velocity = np.concatenate((drum_segment_velocity_1, drum_segment_velocity_1, drum_segment_velocity_2), axis = 1)
		drum_complete_onoff = np.concatenate((drum_segment_onoff_1, drum_segment_onoff_1, drum_segment_onoff_2), axis = 1)

	elif structure == "AABAAABACCDCAABA": 

		drum_segment_notes_1 = np.concatenate((part_A_notes, part_A_notes, part_B_notes, part_A_notes), axis = 1)
		drum_segment_velocity_1 = np.concatenate((part_A_velocity, part_A_velocity, part_B_velocity, part_A_velocity), axis = 1)
		drum_segment_onoff_1 = np.concatenate((part_A_onoff, part_A_onoff, part_B_onoff, part_A_onoff), axis = 1)

		drum_segment_notes_2 = np.concatenate((part_C_notes, part_C_notes, part_D_notes, part_C_notes), axis = 1)
		drum_segment_velocity_2 = np.concatenate((part_C_velocity, part_C_velocity, part_D_velocity, part_C_velocity), axis = 1)
		drum_segment_onoff_2 = np.concatenate((part_C_onoff, part_C_onoff, part_D_onoff, part_C_onoff), axis = 1)

		drum_complete_notes = np.concatenate((drum_segment_notes_1, drum_segment_notes_1, drum_segment_notes_2, drum_segment_notes_1), axis = 1)
		drum_complete_velocity = np.concatenate((drum_segment_velocity_1, drum_segment_velocity_1, drum_segment_velocity_2, drum_segment_velocity_1), axis = 1)
		drum_complete_onoff = np.concatenate((drum_segment_onoff_1, drum_segment_onoff_1, drum_segment_onoff_2, drum_segment_onoff_1), axis = 1)

	elif structure == "ABABCDCDABABCDCD": 

		drum_segment_notes_1 = np.concatenate((part_A_notes, part_B_notes, part_A_notes, part_B_notes), axis = 1)
		drum_segment_velocity_1 = np.concatenate((part_A_velocity, part_B_velocity, part_A_velocity, part_B_velocity), axis = 1)
		drum_segment_onoff_1 = np.concatenate((part_A_onoff, part_B_onoff, part_A_onoff, part_B_onoff), axis = 1)

		drum_segment_notes_2 = np.concatenate((part_C_notes, part_D_notes, part_C_notes, part_D_notes), axis = 1)
		drum_segment_velocity_2 = np.concatenate((part_C_velocity, part_D_velocity, part_C_velocity, part_D_velocity), axis = 1)
		drum_segment_onoff_2 = np.concatenate((part_C_onoff, part_D_onoff, part_C_onoff, part_D_onoff), axis = 1)

		drum_complete_notes = np.concatenate((drum_segment_notes_1, drum_segment_notes_2, drum_segment_notes_1, drum_segment_notes_2), axis = 1)
		drum_complete_velocity = np.concatenate((drum_segment_velocity_1, drum_segment_velocity_2, drum_segment_velocity_1, drum_segment_velocity_2), axis = 1)
		drum_complete_onoff = np.concatenate((drum_segment_onoff_1, drum_segment_onoff_2, drum_segment_onoff_1, drum_segment_onoff_2), axis = 1)

	elif structure == "ABACDCABACDC": 

		drum_segment_notes_1 = np.concatenate((part_A_notes, part_B_notes, part_A_notes), axis = 1)
		drum_segment_velocity_1 = np.concatenate((part_A_velocity, part_B_velocity, part_A_velocity), axis = 1)
		drum_segment_onoff_1 = np.concatenate((part_A_onoff, part_B_onoff, part_A_onoff), axis = 1)

		drum_segment_notes_2 = np.concatenate((part_C_notes, part_D_notes, part_D_notes), axis = 1)
		drum_segment_velocity_2 = np.concatenate((part_C_velocity, part_D_velocity, part_C_velocity), axis = 1)
		drum_segment_onoff_2 = np.concatenate((part_C_onoff, part_D_onoff, part_C_onoff), axis = 1)

		drum_complete_notes = np.concatenate((drum_segment_notes_1, drum_segment_notes_2, drum_segment_notes_1, drum_segment_notes_2), axis = 1)
		drum_complete_velocity = np.concatenate((drum_segment_velocity_1, drum_segment_velocity_2, drum_segment_velocity_1, drum_segment_velocity_2), axis = 1)
		drum_complete_onoff = np.concatenate((drum_segment_onoff_1, drum_segment_onoff_2, drum_segment_onoff_1, drum_segment_onoff_2), axis = 1)

	return drum_complete_notes, drum_complete_velocity, drum_complete_onoff
# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools

np.set_printoptions(linewidth=150)

# Probabilities

HI_HAT_PROB = 0.5
RIDE_PROB = 0.5
KICK_PROB = 0.5
SNARE_PROB = 0.25
TOM_H_PROB = 0.5
TOM_M_PROB = 0.5
TOM_L_PROB = 0.5
CRASH_PROB = 0.1

FILL_HIHAT_PROB = 0.1
FILL_RIDE_PROB = 0
FILL_SNARE_PROB = 0.25
FILL_TOM_H_PROB = 0.50
FILL_TOM_M_PROB = 0.50
FILL_TOM_L_PROB = 0.50
FILL_KICK_PROB = 0.1
FILL_CRASH_PROB = 0.1

FILL_LENGTH = 8 # MAX 16

# Switches

HI_HAT_ON = True
RIDE_ON = False
KICK_ON = True
TOM_ON = True
SNARE_ON = True
CRASH_ON = False

HI_HAT_REPEATED = True
RIDE_REPEATED = False
KICK_REPEATED = False
TOM_REPEATED = True
SNARE_REPEATED = True

# Number of 16th notes to form one chunk to be repeated
HI_HAT_REPEAT_UNIT = 3
RIDE_REPEAT_UNIT = 4
KICK_REPEAT_UNIT = 8
TOM_REPEAT_UNIT = 3
SNARE_REPEAT_UNIT = 5

HI_HAT_RANDOM = True
RIDE_RANDOM = False
KICK_RANDOM = True
SNARE_RANDOM = False
TOM_RANDOM = True
CRASH_RANDOM = False

HI_HAT_CLOSED = False
HI_HAT_OPEN = False
HI_HAT_OPEN_SYNC = False
HI_HAT_OPEN_BACKBEAT = False
HI_HAT_CLOSED_SYNC = False
HI_HAT_OPEN_QUARTERS = False
HI_HAT_CLOSED_QUARTERS = False
HI_HAT_CLOSED_EIGHTS = False
HI_HAT_CLOSED_SIXTEENS = False

RIDE_QUARTERS = False
RIDE_EIGHTS = False
RIDE_SIXTEENS = False
RIDE_SYNC = False

KICK_ONE_THREE = True
KICK_LEAD_FOUR = False
KICK_LEAD_DOUBLE_FOUR = True
KICK_END = False
KICK_DOUBLE_END = True

SNARE_BACKBEAT = True
SNARE_AMEN_1 = True
SNARE_AMEN_2 = False
SNARE_END = False
SNARE_DOUBLE_END = False

NO_SNARE_WHEN_OPEN_HIHAT = False
NO_KICK_WHEN_SNARE = True
KICK_WHEN_CRASH = False
KICK_WHEN_OPEN_HIHAT = False
CRASH_ON_ONE = True  
TOM_MONOPHONIC = True

RIDE_VOL = 75
HIHAT_VOL = 75
KICK_VOL = 100
SNARE_VOL = 100
CRASH_VOL = 50
TOM_VOL = 75

def get(hihat_part = np.zeros((3,16), dtype=np.int64), 
	ride_part = np.zeros((3,16), dtype=np.int64), 
	kick_part = np.zeros((3,16), dtype=np.int64), 
	snare_part = np.zeros((3,16), dtype=np.int64), 
	tom_h_part = np.zeros((3,16), dtype=np.int64), 
	tom_m_part = np.zeros((3,16), dtype=np.int64), 
	tom_l_part = np.zeros((3,16), dtype=np.int64), 
	crash_part = np.zeros((3,16), dtype=np.int64),
	hihat_part_fill = np.zeros((3,16), dtype=np.int64), 
	ride_part_fill = np.zeros((3,16), dtype=np.int64), 
	kick_part_fill = np.zeros((3,16), dtype=np.int64), 
	snare_part_fill = np.zeros((3,16), dtype=np.int64), 
	tom_h_part_fill = np.zeros((3,16), dtype=np.int64), 
	tom_m_part_fill = np.zeros((3,16), dtype=np.int64), 
	tom_l_part_fill = np.zeros((3,16), dtype=np.int64), 
	crash_part_fill = np.zeros((3,16), dtype=np.int64),  

	whichPartsToCreate = []
	): 
	 
	base_rhythm_hihat = np.zeros((3,16), dtype=np.int64)
	base_rhythm_ride = np.zeros((3,16), dtype=np.int64)
	base_rhythm_kick= np.zeros((3,16), dtype=np.int64)
	base_rhythm_snare = np.zeros((3,16), dtype=np.int64)
	base_rhythm_tom_h = np.zeros((3,16), dtype=np.int64)
	base_rhythm_tom_m = np.zeros((3,16), dtype=np.int64)
	base_rhythm_tom_l = np.zeros((3,16), dtype=np.int64)
	base_rhythm_crash = np.zeros((3,16), dtype=np.int64)

	# 0 = rest
	# 1 = closed
	# 2 = open

	if HI_HAT_ON: 

		if HI_HAT_RANDOM and HI_HAT_REPEATED: 

			if HI_HAT_REPEAT_UNIT == 4: 
				micro_rhythm_hihat = np.random.binomial(2, HI_HAT_PROB, size=(3,4))
				base_rhythm_hihat = np.concatenate((micro_rhythm_hihat, micro_rhythm_hihat, micro_rhythm_hihat, micro_rhythm_hihat), axis=1)
			elif HI_HAT_REPEAT_UNIT == 8: 
				micro_rhythm_hihat = np.random.binomial(2, HI_HAT_PROB, size=(3,8))
				base_rhythm_hihat = np.concatenate((micro_rhythm_hihat, micro_rhythm_hihat), axis=1)
			elif HI_HAT_REPEAT_UNIT == 3: 
				micro_rhythm_hihat = np.random.binomial(2, HI_HAT_PROB, size=(3,3))
				base_rhythm_hihat = np.concatenate((micro_rhythm_hihat, micro_rhythm_hihat, micro_rhythm_hihat, micro_rhythm_hihat, micro_rhythm_hihat, np.zeros((3,1), dtype=np.int64)), axis=1)
			elif HI_HAT_REPEAT_UNIT == 5: 
				micro_rhythm_hihat = np.random.binomial(2, HI_HAT_PROB, size=(3,5))
				base_rhythm_hihat = np.concatenate((micro_rhythm_hihat, micro_rhythm_hihat, micro_rhythm_hihat, np.zeros((3,1), dtype=np.int64)), axis=1)
			elif HI_HAT_REPEAT_UNIT == 7: 
				micro_rhythm_hihat = np.random.binomial(2, HI_HAT_PROB, size=(3,7))
				base_rhythm_hihat = np.concatenate((micro_rhythm_hihat, micro_rhythm_hihat, np.zeros((3,2), dtype=np.int64)), axis=1)
			elif HI_HAT_REPEAT_UNIT == 6: 
				micro_rhythm_hihat = np.random.binomial(2, HI_HAT_PROB, size=(3,7))
				base_rhythm_hihat = np.concatenate((micro_rhythm_hihat, micro_rhythm_hihat, np.zeros((3,4), dtype=np.int64)), axis=1)
			else: 
				print("repeat unit not accounted for")

		elif HI_HAT_RANDOM: 
			base_rhythm_hihat = np.random.binomial(2, HI_HAT_PROB, size=(3,16))	

		if HI_HAT_OPEN_BACKBEAT: 
			np.put(base_rhythm_hihat[0], 4, 2)
			np.put(base_rhythm_hihat[0], 12, 2)

		if HI_HAT_CLOSED: 
			indices = np.where(base_rhythm_hihat[0]>1.9)
			base_rhythm_hihat[0][indices] = 1

		if HI_HAT_OPEN: 
			indices = np.where(base_rhythm_hihat[0]==1)
			base_rhythm_hihat[0][indices] = 2

		if HI_HAT_CLOSED_SIXTEENS: 
			base_rhythm_hihat = np.ones((3,16), dtype=np.int64)

		if HI_HAT_CLOSED_EIGHTS: 
			np.put(base_rhythm_hihat[0], 0, 1)
			np.put(base_rhythm_hihat[0], 2, 1)
			np.put(base_rhythm_hihat[0], 4, 1)
			np.put(base_rhythm_hihat[0], 6, 1)
			np.put(base_rhythm_hihat[0], 8, 1)
			np.put(base_rhythm_hihat[0], 10, 1)
			np.put(base_rhythm_hihat[0], 12, 1)
			np.put(base_rhythm_hihat[0], 14, 1)

		if HI_HAT_OPEN_SYNC: 
			np.put(base_rhythm_hihat[0], 2, 2)
			np.put(base_rhythm_hihat[0], 6, 2)
			np.put(base_rhythm_hihat[0], 10, 2)
			np.put(base_rhythm_hihat[0], 14, 2)

		if HI_HAT_CLOSED_SYNC: 
			np.put(base_rhythm_hihat[0], 2, 1)
			np.put(base_rhythm_hihat[0], 6, 1)
			np.put(base_rhythm_hihat[0], 10, 1)
			np.put(base_rhythm_hihat[0], 14, 1)

		if HI_HAT_OPEN_QUARTERS: 
			np.put(base_rhythm_hihat[0], 0, 2)
			np.put(base_rhythm_hihat[0], 4, 2)
			np.put(base_rhythm_hihat[0], 8, 2)
			np.put(base_rhythm_hihat[0], 12, 2)

		if HI_HAT_CLOSED_QUARTERS: 
			np.put(base_rhythm_hihat[0], 0, 1)
			np.put(base_rhythm_hihat[0], 4, 1)
			np.put(base_rhythm_hihat[0], 8, 1)
			np.put(base_rhythm_hihat[0], 12, 1)

	if RIDE_ON: 

		if RIDE_RANDOM and RIDE_REPEATED: 
			micro_rhythm_ride = np.random.binomial(1, RIDE_PROB, size=(3,4))
			base_rhythm_ride = np.concatenate((micro_rhythm_ride, micro_rhythm_ride, micro_rhythm_ride, micro_rhythm_ride), axis=1)

		elif RIDE_RANDOM: 
			base_rhythm_ride = np.random.binomial(1, RIDE_PROB, size=(3,16))

		if RIDE_SIXTEENS: 
			base_rhythm_ride = np.ones((3,16), dtype=np.int64)

		if RIDE_SYNC: 
			np.put(base_rhythm_ride[0], 2, 1)
			np.put(base_rhythm_ride[0], 6, 1)
			np.put(base_rhythm_ride[0], 10, 1)
			np.put(base_rhythm_ride[0], 14, 1)

		if RIDE_QUARTERS: 
			np.put(base_rhythm_ride[0], 0, 1)
			np.put(base_rhythm_ride[0], 4, 1)
			np.put(base_rhythm_ride[0], 8, 1)
			np.put(base_rhythm_ride[0], 12, 1)

		if RIDE_EIGHTS: 
			np.put(base_rhythm_ride[0], 0, 1)
			np.put(base_rhythm_ride[0], 2, 1)
			np.put(base_rhythm_ride[0], 4, 1)
			np.put(base_rhythm_ride[0], 6, 1)
			np.put(base_rhythm_ride[0], 8, 1)
			np.put(base_rhythm_ride[0], 10, 1)
			np.put(base_rhythm_ride[0], 12, 1)
			np.put(base_rhythm_ride[0], 14, 1)

	if KICK_ON: 

		if KICK_RANDOM and KICK_REPEATED: 

			micro_rhythm_kick = np.random.binomial(1, KICK_PROB, size=(3,8))
			base_rhythm_kick = np.concatenate((micro_rhythm_kick, micro_rhythm_kick), axis=1)

		elif KICK_RANDOM: 
			base_rhythm_kick = np.random.binomial(1, KICK_PROB, size=(3,16))

		if KICK_ONE_THREE: 
			np.put(base_rhythm_kick[0], 0, 1)
			np.put(base_rhythm_kick[0], 8, 1)

		if KICK_LEAD_FOUR: 
			np.put(base_rhythm_kick[0], 10, 1)

		if KICK_LEAD_DOUBLE_FOUR: 
			np.put(base_rhythm_kick[0], 10, 1)
			np.put(base_rhythm_kick[0], 11, 1)

		if KICK_END: 
			np.put(base_rhythm_kick[0], 14, 1)

		if KICK_DOUBLE_END: 
			np.put(base_rhythm_kick[0], 14, 1)
			np.put(base_rhythm_kick[0], 15, 1)

		if KICK_WHEN_OPEN_HIHAT: 
			indices = np.where(base_rhythm_hihat[0]>1.9)
			base_rhythm_kick[0][indices] = 1

	if SNARE_ON: 
		if SNARE_RANDOM and SNARE_REPEATED: 

			micro_rhythm_snare = np.random.binomial(1, SNARE_PROB, size=(3,8))
			base_rhythm_snare = np.concatenate((micro_rhythm_snare, micro_rhythm_snare), axis=1)

		elif SNARE_RANDOM: 

			base_rhythm_snare = np.random.binomial(1, SNARE_PROB, size=(3,16))		

		if SNARE_BACKBEAT: 
			np.put(base_rhythm_snare[0], 4, 1)
			np.put(base_rhythm_snare[0], 12, 1)

		if SNARE_AMEN_1: 
			np.put(base_rhythm_snare[0], 7, 1)

		if SNARE_AMEN_2: 
			np.put(base_rhythm_snare[0], 9, 1)

		if SNARE_END: 
			np.put(base_rhythm_snare[0], 14, 1)

		if SNARE_DOUBLE_END: 
			np.put(base_rhythm_snare[0], 14, 1)
			np.put(base_rhythm_snare[0], 15, 1)

		if NO_KICK_WHEN_SNARE:
			indices = np.where(base_rhythm_snare[0]>0.9)
			base_rhythm_kick[0][indices] = 0

		if NO_SNARE_WHEN_OPEN_HIHAT:
			indices = np.where(base_rhythm_hihat[0]>1.9)
			base_rhythm_snare[0][indices] = 0

	if TOM_ON: 
		if TOM_RANDOM and TOM_REPEATED: 

			if TOM_REPEAT_UNIT == 4:
				print("----- HERE ----- ")
				micro_rhythm_tom_h = np.random.binomial(1, TOM_H_PROB, size=(3,4))
				base_rhythm_tom_h = np.concatenate((micro_rhythm_tom_h, micro_rhythm_tom_h, micro_rhythm_tom_h, micro_rhythm_tom_h), axis=1)
				micro_rhythm_tom_m = np.random.binomial(1, TOM_M_PROB, size=(3,4))
				base_rhythm_tom_m = np.concatenate((micro_rhythm_tom_m, micro_rhythm_tom_m, micro_rhythm_tom_m, micro_rhythm_tom_m), axis=1)
				micro_rhythm_tom_l = np.random.binomial(1, TOM_L_PROB, size=(3,4))
				base_rhythm_tom_l = np.concatenate((micro_rhythm_tom_l, micro_rhythm_tom_l, micro_rhythm_tom_l, micro_rhythm_tom_l), axis=1) 
			
			elif TOM_REPEAT_UNIT == 8: 
				micro_rhythm_tom_h = np.random.binomial(1, TOM_H_PROB, size=(3,8))
				base_rhythm_tom_h = np.concatenate((micro_rhythm_tom_h, micro_rhythm_tom_h), axis=1)
				micro_rhythm_tom_m = np.random.binomial(1, TOM_M_PROB, size=(3,8))
				base_rhythm_tom_m = np.concatenate((micro_rhythm_tom_m, micro_rhythm_tom_m), axis=1)
				micro_rhythm_tom_l = np.random.binomial(1, TOM_L_PROB, size=(3,8))
				base_rhythm_tom_l = np.concatenate((micro_rhythm_tom_l, micro_rhythm_tom_l), axis=1)
			elif TOM_REPEAT_UNIT == 3:
				micro_rhythm_tom_h = np.random.binomial(1, TOM_H_PROB, size=(3,3))
				base_rhythm_tom_h = np.concatenate((micro_rhythm_tom_h, micro_rhythm_tom_h, micro_rhythm_tom_h, micro_rhythm_tom_h, micro_rhythm_tom_h, np.zeros((3,1), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_m = np.random.binomial(1, TOM_M_PROB, size=(3,3))
				base_rhythm_tom_m = np.concatenate((micro_rhythm_tom_m, micro_rhythm_tom_m, micro_rhythm_tom_m, micro_rhythm_tom_m, micro_rhythm_tom_m, np.zeros((3,1), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_l = np.random.binomial(1, TOM_L_PROB, size=(3,3))
				base_rhythm_tom_l = np.concatenate((micro_rhythm_tom_l, micro_rhythm_tom_l, micro_rhythm_tom_l, micro_rhythm_tom_l, micro_rhythm_tom_l, np.zeros((3,1), dtype=np.int64) ), axis=1) 
			
			elif TOM_REPEAT_UNIT == 5: 
				micro_rhythm_tom_h = np.random.binomial(1, TOM_H_PROB, size=(3,5))
				base_rhythm_tom_h = np.concatenate((micro_rhythm_tom_h, micro_rhythm_tom_h, micro_rhythm_tom_h, np.zeros((3,1), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_m = np.random.binomial(1, TOM_M_PROB, size=(3,5))
				base_rhythm_tom_m = np.concatenate((micro_rhythm_tom_m, micro_rhythm_tom_m, micro_rhythm_tom_m, np.zeros((3,1), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_l = np.random.binomial(1, TOM_L_PROB, size=(3,5))
				base_rhythm_tom_l = np.concatenate((micro_rhythm_tom_l, micro_rhythm_tom_l, micro_rhythm_tom_l, np.zeros((3,1), dtype=np.int64) ), axis=1) 
			elif TOM_REPEAT_UNIT == 7: 
				micro_rhythm_tom_h = np.random.binomial(1, TOM_H_PROB, size=(3,7))
				base_rhythm_tom_h = np.concatenate((micro_rhythm_tom_h, micro_rhythm_tom_h, np.zeros((3,2), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_m = np.random.binomial(1, TOM_M_PROB, size=(3,7))
				base_rhythm_tom_m = np.concatenate((micro_rhythm_tom_m, micro_rhythm_tom_m, np.zeros((3,2), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_l = np.random.binomial(1, TOM_L_PROB, size=(3,7))
				base_rhythm_tom_l = np.concatenate((micro_rhythm_tom_l, micro_rhythm_tom_l, np.zeros((3,2), dtype=np.int64) ), axis=1) 	
			elif TOM_REPEAT_UNIT == 6: 
				micro_rhythm_tom_h = np.random.binomial(1, TOM_H_PROB, size=(3,6))
				base_rhythm_tom_h = np.concatenate((micro_rhythm_tom_h, micro_rhythm_tom_h, np.zeros((3,4), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_m = np.random.binomial(1, TOM_M_PROB, size=(3,6))
				base_rhythm_tom_m = np.concatenate((micro_rhythm_tom_m, micro_rhythm_tom_m, np.zeros((3,4), dtype=np.int64) ), axis=1)
				micro_rhythm_tom_l = np.random.binomial(1, TOM_L_PROB, size=(3,6))
				base_rhythm_tom_l = np.concatenate((micro_rhythm_tom_l, micro_rhythm_tom_l, np.zeros((3,4), dtype=np.int64) ), axis=1) 
			else: 
				print("repeat unit not accounted for")

		elif TOM_RANDOM: 

			base_rhythm_tom_h = np.random.binomial(1, TOM_H_PROB, size=(3,16))
			base_rhythm_tom_m = np.random.binomial(1, TOM_M_PROB, size=(3,16))
			base_rhythm_tom_l = np.random.binomial(1, TOM_L_PROB, size=(3,16))

		if TOM_MONOPHONIC: 
			indices = np.where(base_rhythm_tom_m[0]>0.9)
			base_rhythm_tom_h[0][indices] = 0
			base_rhythm_tom_l[0][indices] = 0


	if CRASH_ON:
		if CRASH_RANDOM:  
			base_rhythm_crash = np.random.binomial(1, CRASH_PROB, size=(3,16))
		else: 
			base_rhythm_crash = np.zeros((3,16), dtype=np.int64)

		if CRASH_ON_ONE: 
			np.put(base_rhythm_crash[0], 0, 1)
		if KICK_WHEN_CRASH: 
			indices = np.where(base_rhythm_crash[0]>0.9)
			base_rhythm_kick[0][indices] = 1

	base_fill_ride = np.random.binomial(2, FILL_RIDE_PROB, size=(3,FILL_LENGTH))
	base_fill_hihat = np.random.binomial(2, FILL_HIHAT_PROB, size=(3,FILL_LENGTH))
	base_fill_snare = np.random.binomial(1, FILL_SNARE_PROB, size=(3,FILL_LENGTH))
	base_fill_tom_H = np.random.binomial(1, FILL_TOM_H_PROB, size=(3,FILL_LENGTH))
	base_fill_tom_M = np.random.binomial(1, FILL_TOM_M_PROB, size=(3,FILL_LENGTH))
	base_fill_tom_L = np.random.binomial(1, FILL_TOM_L_PROB, size=(3,FILL_LENGTH))
	base_fill_kick = np.random.binomial(1, FILL_KICK_PROB, size=(3,FILL_LENGTH))
	base_fill_crash = np.random.binomial(1, FILL_CRASH_PROB, size=(3,FILL_LENGTH))

	if "ride" in whichPartsToCreate:
		ride_part = base_rhythm_ride
	if "crash" in whichPartsToCreate:
		crash_part = base_rhythm_crash
	if "hihat" in whichPartsToCreate:
		hihat_part = base_rhythm_hihat
	if "tom_h" in whichPartsToCreate:
		tom_h_part = base_rhythm_tom_h
	if "tom_m" in whichPartsToCreate:
		tom_m_part = base_rhythm_tom_m
	if "tom_l" in whichPartsToCreate:
		tom_l_part = base_rhythm_tom_l
	if "snare" in whichPartsToCreate: 
		snare_part = base_rhythm_snare
	if "kick" in whichPartsToCreate:
		kick_part = base_rhythm_kick

	# add new base rythms to existing fills, or create brand new fill parts if they don't exist

	if "ride" in whichPartsToCreate:
		if not np.any(ride_part_fill): 
			ride_part_fill = np.concatenate((base_rhythm_ride[:, 0:16-FILL_LENGTH], base_fill_ride), axis=1)	
		else: 
			ride_part_fill = np.concatenate((base_rhythm_ride[:, 0:16-FILL_LENGTH], ride_part_fill[:, 16-FILL_LENGTH:]), axis=1)
	if "crash" in whichPartsToCreate: 
		if not np.any(crash_part_fill):
			crash_part_fill = np.concatenate((base_rhythm_crash[:, 0:16-FILL_LENGTH], base_fill_crash), axis=1)
		else: 
			crash_part_fill = np.concatenate((base_rhythm_crash[:, 0:16-FILL_LENGTH], crash_part_fill[:, 16-FILL_LENGTH:]), axis=1)
	if "hihat" in whichPartsToCreate:
		if not np.any(hihat_part_fill):
			hihat_part_fill = np.concatenate((base_rhythm_hihat[:, 0:16-FILL_LENGTH], base_fill_hihat), axis=1)
		else:
			hihat_part_fill = np.concatenate((base_rhythm_hihat[:, 0:16-FILL_LENGTH], hihat_part_fill[:, 16-FILL_LENGTH:]), axis=1)
	if "tom_h" in whichPartsToCreate:
		if not np.any(tom_h_part_fill):
			tom_h_part_fill = np.concatenate((base_rhythm_tom_h[:, 0:16-FILL_LENGTH], base_fill_tom_H), axis=1)
		else:
			tom_h_part_fill = np.concatenate((base_rhythm_tom_h[:, 0:16-FILL_LENGTH], tom_h_part_fill[:, 16-FILL_LENGTH:]), axis=1)
	if "tom_m" in whichPartsToCreate:
		if not np.any(tom_m_part_fill):
			tom_m_part_fill =np.concatenate((base_rhythm_tom_m[:, 0:16-FILL_LENGTH], base_fill_tom_M), axis=1)
		else:
			tom_m_part_fill = np.concatenate((base_rhythm_tom_m[:, 0:16-FILL_LENGTH], tom_m_part_fill[:, 16-FILL_LENGTH:]), axis=1)
	if "tom_l" in whichPartsToCreate: 
		if not np.any(tom_l_part_fill):
			tom_l_part_fill = np.concatenate((base_rhythm_tom_l[:, 0:16-FILL_LENGTH], base_fill_tom_L), axis=1)
		else: 
			tom_l_part_fill = np.concatenate((base_rhythm_tom_l[:, 0:16-FILL_LENGTH], tom_l_part_fill[:, 16-FILL_LENGTH:]), axis=1)
	if "snare" in whichPartsToCreate: 
		if not np.any(snare_part_fill):
			snare_part_fill = np.concatenate((base_rhythm_snare[:, 0:16-FILL_LENGTH], base_fill_snare), axis=1)
		else: 
			snare_part_fill = np.concatenate((base_rhythm_snare[:, 0:16-FILL_LENGTH], snare_part_fill[:, 16-FILL_LENGTH:]), axis=1)
	if "kick" in whichPartsToCreate: 
		if not np.any(kick_part_fill):
			kick_part_fill = np.concatenate((base_rhythm_kick[:, 0:16-FILL_LENGTH], base_fill_kick), axis=1)
		else: 
			kick_part_fill = np.concatenate((base_rhythm_kick[:, 0:16-FILL_LENGTH], kick_part_fill[:,16-FILL_LENGTH:]), axis=1)
	
	if "fills"  in whichPartsToCreate: 
		ride_part_fill = np.concatenate((ride_part_fill[:, 0:16-FILL_LENGTH], base_fill_ride), axis=1)
		crash_part_fill = np.concatenate((crash_part_fill[:, 0:16-FILL_LENGTH], base_fill_crash), axis=1)
		hihat_part_fill = np.concatenate((hihat_part_fill[:, 0:16-FILL_LENGTH], base_fill_hihat), axis=1)
		tom_h_part_fill = np.concatenate((tom_h_part_fill[:, 0:16-FILL_LENGTH], base_fill_tom_H), axis=1)
		tom_m_part_fill = np.concatenate((tom_m_part_fill[:, 0:16-FILL_LENGTH], base_fill_tom_M), axis=1)
		tom_l_part_fill = np.concatenate((tom_l_part_fill[:, 0:16-FILL_LENGTH], base_fill_tom_L), axis=1)
		snare_part_fill = np.concatenate((snare_part_fill[:, 0:16-FILL_LENGTH], base_fill_snare), axis=1)
		kick_part_fill = np.concatenate((kick_part_fill[:, 0:16-FILL_LENGTH], base_fill_kick), axis=1)

	# velocity
	ride_part[1].fill(100)
	crash_part[1].fill(100)
	hihat_part[1].fill(100)
	tom_h_part[1].fill(100)
	tom_m_part[1].fill(100)
	tom_l_part[1].fill(100)
	snare_part[1].fill(100)
	kick_part[1].fill(100)

	ride_part_fill[1].fill(100)
	crash_part_fill[1].fill(100)
	hihat_part_fill[1].fill(100)
	tom_h_part_fill[1].fill(100)
	tom_m_part_fill[1].fill(100)
	tom_l_part_fill[1].fill(100)
	snare_part_fill[1].fill(100)
	kick_part_fill[1].fill(100)

	# on-off
	ride_part[2].fill(1)
	crash_part[2].fill(1)
	hihat_part[2].fill(1)
	tom_h_part[2].fill(1)
	tom_m_part[2].fill(1)
	tom_l_part[2].fill(1)
	snare_part[2].fill(1)
	kick_part[2].fill(1)

	ride_part_fill[2].fill(1)
	crash_part_fill[2].fill(1)
	hihat_part_fill[2].fill(1)
	tom_h_part_fill[2].fill(1)
	tom_m_part_fill[2].fill(1)
	tom_l_part_fill[2].fill(1)
	snare_part_fill[2].fill(1)
	kick_part_fill[2].fill(1)

	return hihat_part, ride_part, kick_part, snare_part, tom_h_part, tom_m_part, tom_l_part, crash_part, \
		hihat_part_fill, ride_part_fill, kick_part_fill, snare_part_fill, tom_h_part_fill, tom_m_part_fill, tom_l_part_fill, crash_part_fill 

def createDrumSegmentFromTwoParts(part_A_notes, part_A_velocity, part_A_onoff, 
	part_B_notes, part_B_velocity, part_B_onoff, structure = "AAAB"): 

	length = len(structure) * 16

	drum_segment_notes = np.zeros((8,length), dtype=np.int64)
	drum_segment_velocity = np.zeros((8,length), dtype=np.int64)
	drum_segment_onoff = np.ones((8,length), dtype=np.int64) # all 1's for percussive parts (?)

	if structure == "AAAB": 

		drum_segment_notes = np.concatenate((part_A_notes, part_A_notes, part_A_notes, part_B_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_A_velocity, part_A_velocity, part_B_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_A_onoff, part_A_onoff, part_B_onoff), axis = 1)

	elif structure == "ABAB": 

		drum_segment_notes = np.concatenate((part_A_notes, part_B_notes, part_A_notes, part_B_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_B_velocity, part_A_velocity, part_B_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_B_onoff, part_A_onoff, part_B_onoff), axis = 1)

	elif structure == "AABA": 

		drum_segment_notes = np.concatenate((part_A_notes, part_A_notes, part_B_notes, part_A_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_A_velocity, part_B_velocity, part_A_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_A_onoff, part_B_onoff, part_A_onoff), axis = 1)

	elif structure == "ABAA": 

		drum_segment_notes = np.concatenate((part_A_notes, part_B_notes, part_A_notes, part_A_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_B_velocity, part_A_velocity, part_A_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_B_onoff, part_A_onoff, part_A_onoff), axis = 1)

	elif structure == "ABBA": 

		drum_segment_notes = np.concatenate((part_A_notes, part_B_notes, part_B_notes, part_A_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_B_velocity, part_B_velocity, part_A_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_B_onoff, part_B_onoff, part_A_onoff), axis = 1)

	elif structure == "AAB": 

		drum_segment_notes = np.concatenate((part_A_notes, part_A_notes, part_B_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_A_velocity, part_B_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_A_onoff, part_B_onoff), axis = 1)

	elif structure == "ABA": 

		drum_segment_notes = np.concatenate((part_A_notes, part_B_notes, part_A_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_B_velocity, part_A_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_B_onoff, part_A_onoff), axis = 1)

	elif structure == "ABB": 

		drum_segment_notes = np.concatenate((part_A_notes, part_B_notes, part_B_notes), axis = 1)
		drum_segment_velocity = np.concatenate((part_A_velocity, part_B_velocity, part_B_velocity), axis = 1)
		drum_segment_onoff = np.concatenate((part_A_onoff, part_B_onoff, part_B_onoff), axis = 1)

	return drum_segment_notes, drum_segment_velocity, drum_segment_onoff


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

	#hihat_part[0][hihat_part[0] > 0.9] = 42 # closed hi hat
	#hihat_part[0][hihat_part[0] > 1.9] = 46 # open hi hat
	#ride_part[0][ride_part[0] > 0.9] = 51 # ride cymbal 1
	#kick_part[0][kick_part[0] > 0.9] = 36 # bass drum 1
	#snare_part[0][snare_part[0] > 0.9] = 38 # snare
	#tom_h_part[0][tom_h_part[0] > 0.9] = 48 # mid hi tom
	#tom_m_part[0][tom_m_part[0] > 0.9] = 47 # mid lo tom
	#tom_l_part[0][tom_l_part[0] > 0.9] = 41 # low floor tom
	#crash_part[0][crash_part[0] > 0.9] = 49 # crash cymbal 1

	# 0: kick
	# 1: snare
	# 2: hihat
	# 3: ride
	# 4: tom_h
	# 5: tom_m
	# 6: tom_l
	# 7: crash

	drum_part_notes = np.zeros((8,16), dtype=np.int64)
	drum_part_velocity = np.zeros((8,16), dtype=np.int64)
	drum_part_onoff = np.ones((8,16), dtype=np.int64) # all 1's for percussive parts (?)

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


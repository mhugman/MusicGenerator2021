# Music Composition 2021
# Author: Michael Hugman

import numpy as np
import itertools

np.set_printoptions(linewidth=150)

HI_HAT_PROB = 0.5
KICK_PROB = 0.5
SNARE_PROB = 0.1
TOM_H_PROB = 0.1
TOM_M_PROB = 0.1
TOM_L_PROB = 0.1

FILL_HIHAT_PROB = 0.25
FILL_SNARE_PROB = 0.25
FILL_TOM_H_PROB = 0.25
FILL_TOM_M_PROB = 0.25
FILL_TOM_L_PROB = 0.25
FILL_KICK_PROB = 0.25
FILL_CRASH_PROB = 0.25

FILL_LENGTH = 4

HI_HAT_REPEATED = True
KICK_REPEATED = True
KICK_ONE_THREE = True
TOM_REPEATED = True
SNARE_BACKBEAT = True
SNARE_REPEATED = True
NO_KICK_WHEN_SNARE = True

# 0 = rest
# 1 = closed
# 2 = open

if HI_HAT_REPEATED: 
	micro_rhythm_hihat_A = np.random.binomial(2, HI_HAT_PROB, size=(1,4))
	micro_rhythm_hihat_B = np.random.binomial(2, HI_HAT_PROB, size=(1,4))
	micro_rhythm_hihat_C = np.random.binomial(2, HI_HAT_PROB, size=(1,4))
	micro_rhythm_hihat_D = np.random.binomial(2, HI_HAT_PROB, size=(1,4))

	base_rhythm_hihat_A = np.concatenate((micro_rhythm_hihat_A, micro_rhythm_hihat_A, micro_rhythm_hihat_A, micro_rhythm_hihat_A), axis=1)
	base_rhythm_hihat_B = np.concatenate((micro_rhythm_hihat_B, micro_rhythm_hihat_B, micro_rhythm_hihat_B, micro_rhythm_hihat_B), axis=1)
	base_rhythm_hihat_C = np.concatenate((micro_rhythm_hihat_C, micro_rhythm_hihat_C, micro_rhythm_hihat_C, micro_rhythm_hihat_C), axis=1)
	base_rhythm_hihat_D = np.concatenate((micro_rhythm_hihat_D, micro_rhythm_hihat_D, micro_rhythm_hihat_D, micro_rhythm_hihat_D), axis=1)

else: 
	base_rhythm_hihat_A = np.random.binomial(2, HI_HAT_PROB, size=(1,16))
	base_rhythm_hihat_B = np.random.binomial(2, HI_HAT_PROB, size=(1,16))
	base_rhythm_hihat_C = np.random.binomial(2, HI_HAT_PROB, size=(1,16))
	base_rhythm_hihat_D = np.random.binomial(2, HI_HAT_PROB, size=(1,16))

if KICK_REPEATED: 

	micro_rhythm_kick_A = np.random.binomial(1, KICK_PROB, size=(1,8))
	micro_rhythm_kick_B = np.random.binomial(1, KICK_PROB, size=(1,8))
	micro_rhythm_kick_C = np.random.binomial(1, KICK_PROB, size=(1,8))
	micro_rhythm_kick_D = np.random.binomial(1, KICK_PROB, size=(1,8))

	base_rhythm_kick_A = np.concatenate((micro_rhythm_kick_A, micro_rhythm_kick_A), axis=1)
	base_rhythm_kick_B = np.concatenate((micro_rhythm_kick_B, micro_rhythm_kick_B), axis=1)
	base_rhythm_kick_C = np.concatenate((micro_rhythm_kick_C, micro_rhythm_kick_C), axis=1)
	base_rhythm_kick_D = np.concatenate((micro_rhythm_kick_D, micro_rhythm_kick_D), axis=1)

else: 
	base_rhythm_kick_A = np.random.binomial(1, KICK_PROB, size=(1,16))
	base_rhythm_kick_B = np.random.binomial(1, KICK_PROB, size=(1,16))
	base_rhythm_kick_C = np.random.binomial(1, KICK_PROB, size=(1,16))
	base_rhythm_kick_D = np.random.binomial(1, KICK_PROB, size=(1,16))

if KICK_ONE_THREE: 
	np.put(base_rhythm_kick_A[0], 0, 1)
	np.put(base_rhythm_kick_A[0], 8, 1)
	np.put(base_rhythm_kick_B[0], 0, 1)
	np.put(base_rhythm_kick_B[0], 8, 1)
	np.put(base_rhythm_kick_C[0], 0, 1)
	np.put(base_rhythm_kick_C[0], 8, 1)
	np.put(base_rhythm_kick_D[0], 0, 1)
	np.put(base_rhythm_kick_D[0], 8, 1)

if SNARE_REPEATED: 

	micro_rhythm_snare_A = np.random.binomial(1, SNARE_PROB, size=(1,8))
	micro_rhythm_snare_B = np.random.binomial(1, SNARE_PROB, size=(1,8))
	micro_rhythm_snare_C = np.random.binomial(1, SNARE_PROB, size=(1,8))
	micro_rhythm_snare_D = np.random.binomial(1, SNARE_PROB, size=(1,8))

	base_rhythm_snare_A = np.concatenate((micro_rhythm_snare_A, micro_rhythm_snare_A), axis=1)
	base_rhythm_snare_B = np.concatenate((micro_rhythm_snare_B, micro_rhythm_snare_B), axis=1)
	base_rhythm_snare_C = np.concatenate((micro_rhythm_snare_C, micro_rhythm_snare_C), axis=1)
	base_rhythm_snare_D = np.concatenate((micro_rhythm_snare_D, micro_rhythm_snare_D), axis=1)

else: 

	base_rhythm_snare_A = np.random.binomial(1, SNARE_PROB, size=(1,16))
	base_rhythm_snare_B = np.random.binomial(1, SNARE_PROB, size=(1,16))
	base_rhythm_snare_C = np.random.binomial(1, SNARE_PROB, size=(1,16))
	base_rhythm_snare_D = np.random.binomial(1, SNARE_PROB, size=(1,16))

if SNARE_BACKBEAT: 
	np.put(base_rhythm_snare_A[0], 4, 1)
	np.put(base_rhythm_snare_A[0], 12, 1)
	np.put(base_rhythm_snare_B[0], 4, 1)
	np.put(base_rhythm_snare_B[0], 12, 1)
	np.put(base_rhythm_snare_C[0], 4, 1)
	np.put(base_rhythm_snare_C[0], 12, 1)
	np.put(base_rhythm_snare_D[0], 4, 1)
	np.put(base_rhythm_snare_D[0], 12, 1)

if NO_KICK_WHEN_SNARE:
	indices = np.where(base_rhythm_snare_A[0]>0.9)
	base_rhythm_kick_A[0][indices] = 0

	indices = np.where(base_rhythm_snare_B[0]>0.9)
	base_rhythm_kick_B[0][indices] = 0

	indices = np.where(base_rhythm_snare_C[0]>0.9)
	base_rhythm_kick_C[0][indices] = 0

	indices = np.where(base_rhythm_snare_D[0]>0.9)
	base_rhythm_kick_D[0][indices] = 0

if TOM_REPEATED: 

	micro_rhythm_tom_h_A = np.random.binomial(1, TOM_H_PROB, size=(1,8))
	micro_rhythm_tom_h_B = np.random.binomial(1, TOM_H_PROB, size=(1,8))
	micro_rhythm_tom_h_C = np.random.binomial(1, TOM_H_PROB, size=(1,8))
	micro_rhythm_tom_h_D = np.random.binomial(1, TOM_H_PROB, size=(1,8))

	base_rhythm_tom_h_A = np.concatenate((micro_rhythm_tom_h_A, micro_rhythm_tom_h_A), axis=1)
	base_rhythm_tom_h_B = np.concatenate((micro_rhythm_tom_h_B, micro_rhythm_tom_h_B), axis=1)
	base_rhythm_tom_h_C = np.concatenate((micro_rhythm_tom_h_C, micro_rhythm_tom_h_C), axis=1)
	base_rhythm_tom_h_D = np.concatenate((micro_rhythm_tom_h_D, micro_rhythm_tom_h_D), axis=1)

	micro_rhythm_tom_m_A = np.random.binomial(1, TOM_M_PROB, size=(1,8))
	micro_rhythm_tom_m_B = np.random.binomial(1, TOM_M_PROB, size=(1,8))
	micro_rhythm_tom_m_C = np.random.binomial(1, TOM_M_PROB, size=(1,8))
	micro_rhythm_tom_m_D = np.random.binomial(1, TOM_M_PROB, size=(1,8))

	base_rhythm_tom_m_A = np.concatenate((micro_rhythm_tom_m_A, micro_rhythm_tom_m_A), axis=1)
	base_rhythm_tom_m_B = np.concatenate((micro_rhythm_tom_m_B, micro_rhythm_tom_m_B), axis=1)
	base_rhythm_tom_m_C = np.concatenate((micro_rhythm_tom_m_C, micro_rhythm_tom_m_C), axis=1)
	base_rhythm_tom_m_D = np.concatenate((micro_rhythm_tom_m_D, micro_rhythm_tom_m_D), axis=1)

	micro_rhythm_tom_l_A = np.random.binomial(1, TOM_L_PROB, size=(1,8))
	micro_rhythm_tom_l_B = np.random.binomial(1, TOM_L_PROB, size=(1,8))
	micro_rhythm_tom_l_C = np.random.binomial(1, TOM_L_PROB, size=(1,8))
	micro_rhythm_tom_l_D = np.random.binomial(1, TOM_L_PROB, size=(1,8))

	base_rhythm_tom_l_A = np.concatenate((micro_rhythm_tom_l_A, micro_rhythm_tom_l_A), axis=1)
	base_rhythm_tom_l_B = np.concatenate((micro_rhythm_tom_l_B, micro_rhythm_tom_l_B), axis=1)
	base_rhythm_tom_l_C = np.concatenate((micro_rhythm_tom_l_C, micro_rhythm_tom_l_C), axis=1)
	base_rhythm_tom_l_D = np.concatenate((micro_rhythm_tom_l_D, micro_rhythm_tom_l_D), axis=1)

else: 

	base_rhythm_tom_h_A = np.random.binomial(1, TOM_H_PROB, size=(1,16))
	base_rhythm_tom_h_B = np.random.binomial(1, TOM_H_PROB, size=(1,16))
	base_rhythm_tom_h_C = np.random.binomial(1, TOM_H_PROB, size=(1,16))
	base_rhythm_tom_h_D = np.random.binomial(1, TOM_H_PROB, size=(1,16))

	base_rhythm_tom_m_A = np.random.binomial(1, TOM_M_PROB, size=(1,16))
	base_rhythm_tom_m_B = np.random.binomial(1, TOM_M_PROB, size=(1,16))
	base_rhythm_tom_m_C = np.random.binomial(1, TOM_M_PROB, size=(1,16))
	base_rhythm_tom_m_D = np.random.binomial(1, TOM_M_PROB, size=(1,16))

	base_rhythm_tom_l_A = np.random.binomial(1, TOM_L_PROB, size=(1,16))
	base_rhythm_tom_l_B = np.random.binomial(1, TOM_L_PROB, size=(1,16))
	base_rhythm_tom_l_C = np.random.binomial(1, TOM_L_PROB, size=(1,16))
	base_rhythm_tom_l_D = np.random.binomial(1, TOM_L_PROB, size=(1,16))

base_fill_hihat_A = np.random.binomial(2, FILL_HIHAT_PROB, size=(1,FILL_LENGTH))
base_fill_hihat_B = np.random.binomial(2, FILL_HIHAT_PROB, size=(1,FILL_LENGTH))
base_fill_hihat_C = np.random.binomial(2, FILL_HIHAT_PROB, size=(1,FILL_LENGTH))
base_fill_hihat_D = np.random.binomial(2, FILL_HIHAT_PROB, size=(1,FILL_LENGTH))

base_fill_snare_A = np.random.binomial(1, FILL_SNARE_PROB, size=(1,FILL_LENGTH))
base_fill_snare_B = np.random.binomial(1, FILL_SNARE_PROB, size=(1,FILL_LENGTH))
base_fill_snare_C = np.random.binomial(1, FILL_SNARE_PROB, size=(1,FILL_LENGTH))
base_fill_snare_D = np.random.binomial(1, FILL_SNARE_PROB, size=(1,FILL_LENGTH))

base_fill_tom_H_A = np.random.binomial(1, FILL_TOM_H_PROB, size=(1,FILL_LENGTH))
base_fill_tom_H_B = np.random.binomial(1, FILL_TOM_H_PROB, size=(1,FILL_LENGTH))
base_fill_tom_H_C = np.random.binomial(1, FILL_TOM_H_PROB, size=(1,FILL_LENGTH))
base_fill_tom_H_D = np.random.binomial(1, FILL_TOM_H_PROB, size=(1,FILL_LENGTH))

base_fill_tom_M_A = np.random.binomial(1, FILL_TOM_M_PROB, size=(1,FILL_LENGTH))
base_fill_tom_M_B = np.random.binomial(1, FILL_TOM_M_PROB, size=(1,FILL_LENGTH))
base_fill_tom_M_C = np.random.binomial(1, FILL_TOM_M_PROB, size=(1,FILL_LENGTH))
base_fill_tom_M_D = np.random.binomial(1, FILL_TOM_M_PROB, size=(1,FILL_LENGTH))

base_fill_tom_L_A = np.random.binomial(1, FILL_TOM_L_PROB, size=(1,FILL_LENGTH))
base_fill_tom_L_B = np.random.binomial(1, FILL_TOM_L_PROB, size=(1,FILL_LENGTH))
base_fill_tom_L_C = np.random.binomial(1, FILL_TOM_L_PROB, size=(1,FILL_LENGTH))
base_fill_tom_L_D = np.random.binomial(1, FILL_TOM_L_PROB, size=(1,FILL_LENGTH))

base_fill_kick_A = np.random.binomial(1, FILL_KICK_PROB, size=(1,FILL_LENGTH))
base_fill_kick_B = np.random.binomial(1, FILL_KICK_PROB, size=(1,FILL_LENGTH))
base_fill_kick_C = np.random.binomial(1, FILL_KICK_PROB, size=(1,FILL_LENGTH))
base_fill_kick_D = np.random.binomial(1, FILL_KICK_PROB, size=(1,FILL_LENGTH))

base_fill_crash_A = np.random.binomial(1, FILL_CRASH_PROB, size=(1,FILL_LENGTH))
base_fill_crash_B = np.random.binomial(1, FILL_CRASH_PROB, size=(1,FILL_LENGTH))
base_fill_crash_C = np.random.binomial(1, FILL_CRASH_PROB, size=(1,FILL_LENGTH))
base_fill_crash_D = np.random.binomial(1, FILL_CRASH_PROB, size=(1,FILL_LENGTH))

rhythm_hihat_A = np.concatenate((base_rhythm_hihat_A, base_rhythm_hihat_A, base_rhythm_hihat_A, np.concatenate((base_rhythm_hihat_A[0, 0:17-FILL_LENGTH], base_fill_hihat_A[0]), axis=0)[np.newaxis]), axis=1)
rhythm_hihat_B = np.concatenate((base_rhythm_hihat_B, base_rhythm_hihat_B, base_rhythm_hihat_B, np.concatenate((base_rhythm_hihat_B[0, 0:17-FILL_LENGTH], base_fill_hihat_B[0]), axis=0)[np.newaxis]), axis=1)
rhythm_hihat_C = np.concatenate((base_rhythm_hihat_C, base_rhythm_hihat_C, base_rhythm_hihat_C, np.concatenate((base_rhythm_hihat_C[0, 0:17-FILL_LENGTH], base_fill_hihat_C[0]), axis=0)[np.newaxis]), axis=1)
rhythm_hihat_D = np.concatenate((base_rhythm_hihat_D, base_rhythm_hihat_D, base_rhythm_hihat_D, np.concatenate((base_rhythm_hihat_D[0, 0:17-FILL_LENGTH], base_fill_hihat_D[0]), axis=0)[np.newaxis]), axis=1)

rhythm_tom_h_A = np.concatenate((base_rhythm_tom_h_A, base_rhythm_tom_h_A, base_rhythm_tom_h_A, np.concatenate((base_rhythm_tom_h_A[0, 0:17-FILL_LENGTH], base_fill_tom_H_A[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_h_B = np.concatenate((base_rhythm_tom_h_B, base_rhythm_tom_h_B, base_rhythm_tom_h_B, np.concatenate((base_rhythm_tom_h_B[0, 0:17-FILL_LENGTH], base_fill_tom_H_B[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_h_C = np.concatenate((base_rhythm_tom_h_C, base_rhythm_tom_h_C, base_rhythm_tom_h_C, np.concatenate((base_rhythm_tom_h_C[0, 0:17-FILL_LENGTH], base_fill_tom_H_C[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_h_D = np.concatenate((base_rhythm_tom_h_D, base_rhythm_tom_h_D, base_rhythm_tom_h_D, np.concatenate((base_rhythm_tom_h_D[0, 0:17-FILL_LENGTH], base_fill_tom_H_D[0]), axis=0)[np.newaxis]), axis=1)

rhythm_tom_m_A = np.concatenate((base_rhythm_tom_m_A, base_rhythm_tom_m_A, base_rhythm_tom_m_A, np.concatenate((base_rhythm_tom_m_A[0, 0:17-FILL_LENGTH], base_fill_tom_M_A[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_m_B = np.concatenate((base_rhythm_tom_m_B, base_rhythm_tom_m_B, base_rhythm_tom_m_B, np.concatenate((base_rhythm_tom_m_B[0, 0:17-FILL_LENGTH], base_fill_tom_M_B[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_m_C = np.concatenate((base_rhythm_tom_m_C, base_rhythm_tom_m_C, base_rhythm_tom_m_C, np.concatenate((base_rhythm_tom_m_C[0, 0:17-FILL_LENGTH], base_fill_tom_M_C[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_m_D = np.concatenate((base_rhythm_tom_m_D, base_rhythm_tom_m_D, base_rhythm_tom_m_D, np.concatenate((base_rhythm_tom_m_D[0, 0:17-FILL_LENGTH], base_fill_tom_M_D[0]), axis=0)[np.newaxis]), axis=1)

rhythm_tom_l_A = np.concatenate((base_rhythm_tom_l_A, base_rhythm_tom_l_A, base_rhythm_tom_l_A, np.concatenate((base_rhythm_tom_l_A[0, 0:17-FILL_LENGTH], base_fill_tom_L_A[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_l_B = np.concatenate((base_rhythm_tom_l_B, base_rhythm_tom_l_B, base_rhythm_tom_l_B, np.concatenate((base_rhythm_tom_l_B[0, 0:17-FILL_LENGTH], base_fill_tom_L_B[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_l_C = np.concatenate((base_rhythm_tom_l_C, base_rhythm_tom_l_C, base_rhythm_tom_l_C, np.concatenate((base_rhythm_tom_l_C[0, 0:17-FILL_LENGTH], base_fill_tom_L_C[0]), axis=0)[np.newaxis]), axis=1)
rhythm_tom_l_D = np.concatenate((base_rhythm_tom_l_D, base_rhythm_tom_l_D, base_rhythm_tom_l_D, np.concatenate((base_rhythm_tom_l_D[0, 0:17-FILL_LENGTH], base_fill_tom_L_D[0]), axis=0)[np.newaxis]), axis=1)

rhythm_snare_A = np.concatenate((base_rhythm_snare_A, base_rhythm_snare_A, base_rhythm_snare_A, np.concatenate((base_rhythm_snare_A[0, 0:17-FILL_LENGTH], base_fill_snare_A[0]), axis=0)[np.newaxis]), axis=1)
rhythm_snare_B = np.concatenate((base_rhythm_snare_B, base_rhythm_snare_B, base_rhythm_snare_B, np.concatenate((base_rhythm_snare_B[0, 0:17-FILL_LENGTH], base_fill_snare_B[0]), axis=0)[np.newaxis]), axis=1)
rhythm_snare_C = np.concatenate((base_rhythm_snare_C, base_rhythm_snare_C, base_rhythm_snare_C, np.concatenate((base_rhythm_snare_C[0, 0:17-FILL_LENGTH], base_fill_snare_C[0]), axis=0)[np.newaxis]), axis=1)
rhythm_snare_D = np.concatenate((base_rhythm_snare_D, base_rhythm_snare_D, base_rhythm_snare_D, np.concatenate((base_rhythm_snare_D[0, 0:17-FILL_LENGTH], base_fill_snare_D[0]), axis=0)[np.newaxis]), axis=1)

rhythm_kick_A = np.concatenate((base_rhythm_kick_A, base_rhythm_kick_A, base_rhythm_kick_A, np.concatenate((base_rhythm_kick_A[0, 0:17-FILL_LENGTH], base_fill_kick_A[0]), axis=0)[np.newaxis]), axis=1)
rhythm_kick_B = np.concatenate((base_rhythm_kick_B, base_rhythm_kick_B, base_rhythm_kick_B, np.concatenate((base_rhythm_kick_B[0, 0:17-FILL_LENGTH], base_fill_kick_B[0]), axis=0)[np.newaxis]), axis=1)
rhythm_kick_C = np.concatenate((base_rhythm_kick_C, base_rhythm_kick_C, base_rhythm_kick_C, np.concatenate((base_rhythm_kick_C[0, 0:17-FILL_LENGTH], base_fill_kick_C[0]), axis=0)[np.newaxis]), axis=1)
rhythm_kick_D = np.concatenate((base_rhythm_kick_D, base_rhythm_kick_D, base_rhythm_kick_D, np.concatenate((base_rhythm_kick_D[0, 0:17-FILL_LENGTH], base_fill_kick_D[0]), axis=0)[np.newaxis]), axis=1)


print(rhythm_hihat_A)
print(rhythm_tom_h_A)
print(rhythm_tom_m_A)
print(rhythm_tom_l_A)
print(rhythm_snare_A)
print(rhythm_kick_A)
print("----")




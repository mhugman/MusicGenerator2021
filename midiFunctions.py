
import mido
import numpy as np
from mido import MidiFile
from mido.midifiles import MidiTrack
from mido import MetaMessage
from mido import Message
from globals import SONG_LENGTH
from globals import TEMPO
from globals import TIME_SIG

NUM_16th_PER_BAR = TIME_SIG * 4

MAX_SUSTAIN = 200 # maximum time to sustain a note before it gets removed
MIN_LENGTH = 100

NUM_TRACKS = 8

def createMidiFile(noteArray, velocityArray, onOffArray, tempo, filename, instrument = "Piano"): 

    adjTempo = int(round(60000000 / tempo))

    '''
    This function will take a 3D numpy note Array (e.g. parsed from a midi file), and turn it into 
    a midi file which can be played back. 
    '''

    with MidiFile() as mid:
    
        # add an empty first track (for testing)
    
        #mid.add_track(name= str(0))
        #track = mid.tracks[0]
            
        #track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=96, notated_32nd_notes_per_beat=8, time=0))
        

        numMessages = 0 
    
        for i in range(noteArray.shape[0]): 
            
            mid.add_track(name= str(i))
            track = mid.tracks[i]

            track.append(MetaMessage('set_tempo', tempo=adjTempo, time=0))
            track.append(MetaMessage('time_signature', numerator = TIME_SIG, denominator = 4, clocks_per_click = 24, notated_32nd_notes_per_beat = 8))

            
            #track.append(Message('control_change', channel = 1, control=0, value=0, time=0))

            # Drums
            if instrument == "Drums": 
                track.append(Message('program_change', channel = 10, program=1, time=0))
            elif instrument == "Piano": 
                track.append(Message('program_change', channel = 0, program=0, time=0))
            else: 
                print("instrument not recognized")
            '''
            if i >= 0 and i < 3: 
                # Grand Piano
                track.append(Message('program_change', channel = i, program=0, time=0))
            elif i == 3: 
                # Electric Guitar (clean)
                track.append(Message('program_change', channel = i, program=27, time=0))
            elif i == 4: 
                # Electric Bass (finger)
                track.append(Message('program_change', channel = i, program=33, time=0))
            elif i == 5: 
                # Glockenspiel
                track.append(Message('program_change', channel = i, program=9, time=0))
            else: 
                # Electric Piano
                track.append(Message('program_change', channel = i, program=4, time=0))
            '''

            #track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=96, notated_32nd_notes_per_beat=8, time=0))
            #track.append(MetaMessage('set_tempo', tempo=TEMPO, time=0))

            timeSinceLastMessage = 0
            clock = 0 
            currentNotes = []

            for j in range(min(noteArray.shape[1], velocityArray.shape[1], onOffArray.shape[1])):

                messageGenerated = False

                noteVelocity = velocityArray[i,j]
                onOff = onOffArray[i,j]

                noteValue = noteArray[i,j]

                if noteValue < 0 : 

                    noteValue = 0 

                elif noteValue > 127: 

                    noteValue = 127

                if noteVelocity < 0 : 

                    noteVelocity = 0 

                elif noteVelocity > 127: 

                    noteVelocity = 127

                for note in currentNotes: 
                    if clock - note[2] >= 120: 
                        track.append(Message('note_off', channel = 1, note= note[0], velocity=note[1], time=timeSinceLastMessage - 120))
                        currentNotes.remove(note)
                     
                if onOff > 0.9 and onOff < 1.1 and noteValue > 0 : 

                    track.append(Message('note_on', channel = 1, note= noteValue, velocity=noteVelocity, time=timeSinceLastMessage))
                    currentNotes.append((noteValue, noteVelocity, clock))
                    messageGenerated = True

                elif onOff > 1.9 and onOff < 2.1: 
                     
                    for note in currentNotes: 
                        track.append(Message('note_off', channel = 1, note= note[0], velocity=note[1], time=timeSinceLastMessage - 120))

                    currentNotes = []
                    messageGenerated = True

                else: 
                    # onOff value is 0, don't do anything
                    pass


                # if a message was generated (either note_on or note_off), then reset the time
                # since last message to 0
                if messageGenerated == True: 
                    # the value here resets to 1 instead of 0, because its been at least one tick 
                    # since the last message

                    timeSinceLastMessage = 120
                else: 
                    # if there was no message, simply increment the time since the last message
                    timeSinceLastMessage = timeSinceLastMessage + 120

                clock += 120

        mid.save("midi/" +  filename + '.mid')

def parseMidi(mid): 
    
    # Exclude certain tracks from being parsed, such as percussion
    exclusions = []

    noteArray = np.zeros((NUM_TRACKS, SONG_LENGTH)).astype("int")
    velocityArray = np.zeros((NUM_TRACKS, SONG_LENGTH)).astype("int")
    onOffArray = np.zeros((NUM_TRACKS, SONG_LENGTH)).astype("int")

    maxSongLength = noteArray.shape[1]

    #print("max Song Length: ", maxSongLength)
        
    
    for i, track in enumerate(mid.tracks):
    
        #print 'Track {}: {}'.format(i, track.name)
        
        currentNotes = []

        delQ = []

        timeQ = []
        
        if track.name not in exclusions: 
            
            currentTime = 0
            for message in track:

                #print("message: ", message)

                if currentTime >= maxSongLength - MIN_LENGTH: 

                    break
                
                if message.type == "note_on" or message.type == "note_off":
                    prevTime = currentTime
                    currentTime = currentTime + round(message.time / 120)

                    #print("Current time: " + str(currentTime))

                    # previous notes are the same as (not yet updated) current notes, 
                    # but the third value is 0 instead of 1 (denoting the fact that 
                    # the note is sustained, rather than hit)
                    prevNotes = []
                    for x in currentNotes: 
                         prevNotes.append((x[0], x[1], 0))
                    
                    # Fill in all the values since the previous message, and up to 
                    # but not including the time of the current message, with the
                    # previous notes
                    '''
                    if len(prevNotes) > 0:     
                        deltaTime = currentTime - prevTime
                        for j in range(0, deltaTime - 1): 

                            noteArray[i][currentTime - 1 - j] = prevNotes[0][0]
                            velocityArray[i][currentTime - 1 - j] = prevNotes[0][1]
                            onOffArray[i][currentTime - 1 - j] = prevNotes[0][2]
                    '''

                    # update the current Notes being played with the information in the
                    # message
                    if message.type == "note_on": 
                                
                        currentNotes.append((message.note, message.velocity,1))

                        delQ.append((message.note, message.velocity,1))
                        timeQ.append(MAX_SUSTAIN)

                        # fill in the value for this particular time with the current Notes
                        if len(currentNotes) > 0:  

                            noteArray[i][currentTime] = np.asarray(currentNotes[0][0])
                            velocityArray[i][currentTime] = np.asarray(currentNotes[0][1])
                            onOffArray[i][currentTime] = np.asarray(currentNotes[0][2])
                     
                        for x in currentNotes: 
                            if x[0] == message.note: 
                                try: 
                                    x_idx = delQ.index(x)
                                    delQ.pop(x_idx)
                                    timeQ.pop(x_idx)
                                    currentNotes.remove(x)
                                except: 

                                    print("timeQ: ", timeQ)
                                    print("trying to remove ", x)


                            ## TO DO : add -1 to onOffArray in appropriate place
                
                timeQ = [x - 1 for x in timeQ]

                while timeQ.count(0) > 0 : 

                    zeroIdx = timeQ.index(0)
                    try: 
                        currentNotes.remove(delQ[zeroIdx])
                    except: 
                        print("currentNotes: ", currentNotes)
                        print("trying to delete: ", delQ[zeroIdx])
                    delQ.pop(zeroIdx)
                    timeQ.pop(zeroIdx)

    print("$$$$$$$$$$$$$$$$$$$$$$$$$")

    indices_5 = np.argwhere(noteArray[0] == 36)
    noteArray[0][indices_5] = 1

    indices_3 = np.argwhere(noteArray[1] == 38)
    noteArray[1][indices_3] = 1

    indices_1 = np.argwhere(noteArray[2] == 46)
    noteArray[2][indices_1] = 2

    indices_2 = np.argwhere(noteArray[2] == 42)
    noteArray[2][indices_2] = 1

    indices_4 = np.argwhere(noteArray[3] == 51)
    noteArray[3][indices_4] = 1

    indices_6 = np.argwhere(noteArray[4] == 48)
    noteArray[4][indices_6] = 1

    indices_7 = np.argwhere(noteArray[5] == 47)
    noteArray[5][indices_7] = 1

    indices_8 = np.argwhere(noteArray[6] == 41)
    noteArray[6][indices_8] = 1

    indices_9 = np.argwhere(noteArray[7] == 49)
    noteArray[7][indices_9] = 1

    return noteArray, velocityArray, onOffArray
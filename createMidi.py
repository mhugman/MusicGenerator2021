
import mido
import numpy as np
from mido import MidiFile
from mido.midifiles import MidiTrack
from mido import MetaMessage
from mido import Message

import globalvars


SONG_LENGTH = globalvars.SONG_LENGTH
MAX_POLYPHONY = globalvars.MAX_POLYPHONY
NUM_MIDI_TRACKS = globalvars.NUM_MIDI_TRACKS
TEMPO = globalvars.TEMPO 

MAX_SUSTAIN = 200 # maximum time to sustain a note before it gets removed
MIN_LENGTH = 100


NUM_TRACKS = NUM_MIDI_TRACKS * MAX_POLYPHONY

def createMidiFile(noteArray, velocityArray, onOffArray, adjTempo, filename): 

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
            
            #track.append(Message('control_change', channel = 1, control=0, value=0, time=0))

            # Grand Piano
            track.append(Message('program_change', channel = 1, program=0, time=0))
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
                    
                    
                if onOff > 0.6: 

                    track.append(Message('note_on', channel = 1, note= noteValue, velocity=noteVelocity, time=timeSinceLastMessage))
                    messageGenerated = True

                elif onOff < -0.6: 
                     

                    track.append(Message('note_off', channel = 1, note= noteValue, velocity=noteVelocity, time=timeSinceLastMessage))
                    messageGenerated = True

                else: 
                    # onOff value is 0, don't do anything
                    pass


                # if a message was generated (either note_on or note_off), then reset the time
                # since last message to 0
                if messageGenerated == True: 
                    # the value here resets to 1 instead of 0, because its been at least one tick 
                    # since the last message

                    timeSinceLastMessage = 1
                else: 
                    # if there was no message, simply increment the time since the last message
                    timeSinceLastMessage = timeSinceLastMessage + 1

        mid.save("midi/" +  filename + '.mid')
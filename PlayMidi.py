# A script for listing the available midi devices, connecting to a user
# specified device, and printing all MIDI events from that device.
# This script uses pygame.midi, for more info go to:
# http://www.pygame.org/docs/ref/midi.html


import pygame.midi as midi
import pygame


# Initiate pygame

pygame.init()
pygame.fastevent.init()
midi.init()

# Print default MIDI device

print("Default input device is: ")
print(midi.get_default_input_id())

# Print device info for all MIDI devices

for i in range(midi.get_count()):
    print midi.get_device_info(i)

# Prompt user for input device

ipDev = input("Choose input device:")

x = midi.Input(ipDev,0)

x.read(1)

# Prompt user for output device

opDev = input("Choose output device:")

player = midi.Output(2, latency = 0)
player.set_instrument(2)

# Continous loop which checks for MIDI events from the input device and plays
# them on the output device.
while True:
    if x.poll(): # if there is a MIDI event
        midiEvents = x.read(1)[0] # read the event
        note = midiEvents[0][1]
        vel = midiEvents[0][2]
        
        if vel != 0:
            player.note_on(note,vel)
        else:
            player.note_off(note,vel)
            
        
        

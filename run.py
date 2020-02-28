import mido


inport = mido.open_input('CH345 MIDI 1')

for msg in inport:
    print(msg)

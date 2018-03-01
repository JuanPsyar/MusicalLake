'''theMusicalLake.py'''

import sys

def main():
    output=""
    inputs = open(sys.argv[1], 'r')

    song1 = ['brr', 'fiu', 'cric-cric', 'brrah']
    song2 = ['pep', 'birip', 'trri-trri', 'croac']
    song3 = ['bri-bri', 'plop', 'cric-cric', 'brrah']

    def findSong(song, inputSound):
        soundChain = ''
        if inputSound in song:
            for sound in song:
                if (song.index(sound) > song.index(inputSound)):
                    soundChain += sound + '\t'
        return (soundChain + '\n') if soundChain != '' else ''

    for line in inputs:
        inputSound = line.strip()
        if inputSound != 'croac' or inputSound != 'brrah':
            output2 = ''
            output2 += findSong(song1, inputSound)
            output2 += findSong(song2, inputSound) if output2 == '' else ''
            output2 += findSong(song3, inputSound) if output2 == '' else ''
            output += output2
        else:
            output += 'No sound\n'

    inputs.close()
    print output.strip()

if __name__ == "__main__": main()

# converts the 1000 song samples in music genre classifier project from au to wav files

import os
from pydub import AudioSegment

for file in os.listdir(r'D:\Coding\Python\Bowler\Music\songList'):
    song = AudioSegment.from_file((r'D:\Coding\Python\Bowler\Music\songList\\' + file), 'au')
    song.export(r'D:\Coding\Python\Bowler\Music\songList\\' + file[:-3] + '.wav', format = 'wav')
    os.remove(r'D:\Coding\Python\Bowler\Music\songList\\' + file)
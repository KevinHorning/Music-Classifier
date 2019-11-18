              Brent Mckinney                                                      Kevin Horning
              bmckinney12@student.gsu.edu                                         Khorning2@student.gsu.edu


Our goal was to create a music classifier that would identify the genre of a small music sample. In order to accomplish this, we trained a Convolutional Neural Network on an online dataset of 1000 songs in 10 genres. After 5 epochs, the CNN was found to have 96% accuracy on classifying test songs from the dataset.

We found the online dataset of songs at http://opihi.cs.uvic.ca/sound/ to experiment on. We wanted try the approach of training the network with input of spectrograms instead of directly from the audio files. To do this, we had to convert the song files, in .au format, to .wav files using the AU_to_WAV.py script. This allowed librosa to convert each file to a spectrogram image and folders were created for each genre with the spectrogram images in them with the create_spectrogram.py script. After this, the create_dataset.py script vectorizes and shuffles the spectrogram images so that they, and their classification, can be put into the CNN for training and testing. Finally, the CNN was set up and trained on the input data using the neuralnet.py script. 

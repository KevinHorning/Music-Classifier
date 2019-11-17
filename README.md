# Music-Classifier

              Brent Mckinney                                                      Kevin Horning
              bmckinney12@student.gsu.edu                                         Khorning2@student.gsu.edu


Abstract:

Our project is to train our model to classify a specific song to a music genre and to be able to recognize a specific song to be in a specific music genre in our testing. We were motivated because we love music and want to better understand how different classification of music work and to see if a machine can automatically predict the genre of a song. This task will challenge us to use Python and apply it to a topic that we’re passionate about.

Running our program:

We first downloaded a public dataset from the following link: http://opihi.cs.uvic.ca/sound/ From here we ran the create_spectrogram.py script. This created folders for each genre, and populated them with the corresponding spectrograms. Then we spent a lot of time trying to manipulate them into training and test data set with create_dataset.py, but ultimately figured out a way to achieve this using Keras. We accomplished this step, as well as building our neural network in the neuralnet_py.py script. 




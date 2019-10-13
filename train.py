from textgenrnn import textgenrnn
t = textgenrnn('/home/sol/Documents/babel/textgenrnn_weights_2.hdf5')
import sys
t.train_from_file(sys.argv[1], new_model=True, num_epochs=30, rnn_layers=3, batch_size=160)

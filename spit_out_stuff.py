from textgenrnn import textgenrnn
t = textgenrnn(weights_path='textgenrnn_weights.hdf5',vocab_path='textgenrnn_vocab.json', config_path='textgenrnn_config.json')
t.generate(100,temperature=0.5)

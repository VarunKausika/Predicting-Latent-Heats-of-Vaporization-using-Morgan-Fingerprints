# Predicting-Latent-Heats-of-Vaporization-using-Morgan-Fingerprints
An ANN was trained to take the bitvectors of the Morgan fingerprints on a set of 2636 molecules,  was tested on 659 molecules.

The optimal hyperparameters of the neural network are: 
{'activation': 'logistic', 'alpha': 0.05, 'hidden_layer_sizes': (10,), 'solver': 'lbfgs'}

Optimal Testing set accuracy: 0.8630428886480798
Optimal Training set accuracy: 0.9987399275199881

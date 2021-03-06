# -*- coding: utf-8 -*-
'''
Object for robust implementations, both at master and worker
'''

__author__ = "Marcos Fernández Díaz"
__date__ = "September 2020"


import numpy as np



class Robust_Master:
    """
    This class implements robust aggregation methods for different algorithms, runs at Master node.
    """
    def __init__(self, method='average'):
        """
        Create a class `Robust_Master` instance.

        Parameters
        ----------
        method: String
            Name of the aggregation method to use
        """
        self.method = method.lower() # Convert string to lowercase


    def aggregate(self, list_weights):
        """
        Method for aggregating models.

        Parameters
        ----------
        list_weights: List of lists of numpy arrays
            Object containing the models trained in each of the workers. Each model from a worker is represented as a list of numpy arrays.

        Returns
        ----------
        new_weights: List of numpy arrays
            Object containing the aggregated model combining all the models from the different workers
        """
        if self.method == 'average':
            new_weights = []
            for index_layer in range(len(list_weights[0])):
                layer_weights = []
                for worker in range(len(list_weights)):
                    layer_weights.append(list_weights[worker][index_layer])                 
                mean_weights = np.mean(layer_weights, axis=0) # Average layer weights for all workers
                new_weights.append(mean_weights)

        else:
            raise NotImplementedError

        return new_weights
        

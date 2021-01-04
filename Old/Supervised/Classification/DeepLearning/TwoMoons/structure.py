import sys
sys.path.append('/home/ubuntu/workspace/utils')

import numpy as np
import matplotlib.pyplot as plt
import mglearn as mglearn
from IPython.display import display
import pydot 

dot = mglearn.plots.plot_logistic_regression_graph()
dot.format = 'png'
dot.render(filename='structure1');  

dot = mglearn.plots.plot_single_hidden_layer_graph()
dot.format = 'png'
dot.render(filename='structure2');  

dot = mglearn.plots.plot_two_hidden_layer_graph()
dot.format = 'png'
dot.render(filename='structure3');  

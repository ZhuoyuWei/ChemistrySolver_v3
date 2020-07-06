import torch
from torch import nn

'''
Simplest GNN
represent a graph into a tensor
'''
class GNN(nn.Module):
    def __init__(self):
        self.input_layer=None
        self.embedding_layer=None
        self.merge_layer=None
        self.output_layer=None

    def foward(self,input,label=None):
        hidden_states=None
        loss=None
        if label is not None:
            #calculate loss
            loss=0
        return hidden_states,loss
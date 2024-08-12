######################################################################
# Replay Memory
# -------------
#
# We will implement replay memory to facilitate the training of our DQN.
# This memory keeps track of the transitions observed by the agent,
# allowing for the reuse of this information later. By randomly sampling
# from the memory, we can decorrelate the transitions that form a batch,
# which has been shown to significantly enhance the stability and effectiveness
# of the DQN training process.
#
# To achieve this, we need to define two classes:
#
# - **Transition**: a named tuple that represents an individual transition
#   within our environment. It correlates (state, action) pairs with their
#   resulting (next_state, reward), where the state refers to the image 
#   of the screen difference, as will be explained later.
# - **ReplayMemory**: a fixed-size cyclic buffer that stores the most
#   recently observed transitions. This class also includes a `.sample()`
#   method to randomly select a batch of transitions for the training process.
#

import random
from collections import namedtuple

Transition = namedtuple('Transition', ('state', 'action', 'reward', 'next_state', 'done'))

class ReplayMemory(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    '''
    def push(self, *.args): ## *args):
        """Saves a transition."""
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)
        self.position = (self.position + 1) % self.capacity    
    '''    
    
       
    def push(self, batch):
        self.memory.append(batch)
        if len(self.memory) > self.capacity:
            del self.memory[0]    
       

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
from multiprocessing import Pool 
import tqdm
import os

# List of lists to single list
from itertools import chain

# Sending keyword arguments in map
from functools import partial

print(os.cpu_count())

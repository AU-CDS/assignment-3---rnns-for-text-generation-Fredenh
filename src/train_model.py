# data processing tools
import string, os 
import pandas as pd
import numpy as np
np.random.seed(42)

# keras module for building LSTM 
import tensorflow as tf
tf.random.set_seed(42)
import tensorflow.keras.utils as ku 
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# surpress warnings
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
sys.path.append(".")
import utils.requirements_functions as rf

# loading data
data_dir = os.path.join("..", "data", "news_data")

all_comments = []
for filename in os.listdir(data_dir): # go trhoug everything in the directory
    if 'Comments' in filename: # if the string "comments" is in the directory
        comment_df = pd.read_csv(data_dir + "/" + filename) # make it into a pd dataframe. joining dataframe "/" filename
        all_comments.extend(list(comment_df["commentBody"].values)) # creates a list of the extend


corpus = [rf.clean_text(x) for x in all_comments] #string cleaning function. 
corpus[:10]
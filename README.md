[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/5f7lMH9Y)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10587497&assignment_repo_type=AssignmentRepo)
# Assignment 3 - Language modelling and text generation using RNNs
This is the third of five assignments for the Language Analytics course

# Contribution
Initially, I sparred with my fellow students for this assignment. For the actual code itself, i took great inspiration from the notebooks that touched upon the concept of model training and text generation with ```TensorFlow```. I also consulted the link provided further down in Ross' instructions when it came to saving a trained model. 

# Ross' instructions
Text generation is hot news right now!

For this assignemnt, you're going to create some scripts which will allow you to train a text generation model on some culturally significant data - comments on articles for *The New York Times*. You can find a link to the data [here](https://www.kaggle.com/datasets/aashita/nyt-comments).

You should create a collection of scripts which do the following:

- Train a model on the Comments section of the data
  - [Save the trained model](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model)
- Load a saved model
  - Generate text from a user-suggested prompt

## Objectives

Language modelling is hard and training text generation models is doubly hard. For this course, we lack somewhat the computationl resources, time, and data to train top-quality models for this task. So, if your RNNs don't perform overwhelmingly, that's fine (and expected). Think of it more as a proof of concept.

- Using TensorFlow to build complex deep learning models for NLP
- Illustrating that you can structure repositories appropriately
- Providing clear, easy-to-use documentation for your work.

# Data
The data used for this assignment is the [New York Times Comments dataset](https://www.kaggle.com/datasets/aashita/nyt-comments) provided by Kaggle user Aashita Keserwani: "The data contains information about the comments made on the articles published in New York Times in Jan-May 2017 and Jan-April 2018". The data comes as a zip file once downloaded. It will be unzipped from the pipeline within the _train_model.py_ script. 

# Packages
* ```os``` is used for navigating paths
* ```pandas``` is used to read the CSV into a pd object
* ```numPy``` is used to set a random seed as well as shuffling the subset of data used for training
* ```tensorflow``` is used for tokenizing and model training 
* ```warnings``` is used to suprress warnings
* ```sys``` is used to navigate the directories and helps importing the functions from the _requirements_functions.py_ script in _utils_
* ```zipfile``` is used to unzip the data 

# Methods 
There are two scripts in the submission for this assignment. The first one i will describe is the _train_model.py_ script. The script starts by unzipping the data into the _data_ folder and loads it into the scripts afterwards. Then a for loop iterates through everything in the _news_data_ folder and selects only the CSV's containing the comments. Then a sample size of 1000 comments is selected and randomized using ```numPy``` before it is cleaned so that intergers are omitted. Then the data is tokenized using ```Tokenizer()``` from ```TensorFlow```. Then a model is trained on the data with the help of the ```rf.create_model()``` function from the _requirements_functions.py_ script. Then the model is saved to the folder called _models_ via the documentation from this [link](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model). The script ends with a print statement that tests if the models has trained successfully using a preset prompt.
The second script is the _text_gen.py_ script which lets the user generate text with a user-suggested promt. This is done via the ```argparse``` code presented in the script. It lets the user choose which prompt the text generator should use as well as the amount of words after the prompt. It also makes it possible to load a different trained model to generate text from. Then the script loads in the model, and proceeds to tokenize using the same principles as in the previous script. Then the script uses the ```rf.generate_text()``` function from the _requirements_functions.py_ script, which takes the ´´´argparse``` arguments mentioned before, and prints the result to the terminal.








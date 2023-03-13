import numpy as np
import json as json
from flask import Flask,request,jsonify
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import colorama
colorama.init()
from colorama import Fore,Style,Back

import random
import pickle

with open ('intent.json') as file:
   data=json.load(file)

def chat():
   # load trained model
   model=keras.models.load_model('chat_model')

   #load tikenizer object
   with open('tokenizer.pickle','rb') as handle:
      tokenizer=pickle.load(handle)




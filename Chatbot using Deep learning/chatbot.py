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

with open ("intent.json") as file:
   data=json.load(file)

def chat():
   # load trained model
   model=keras.models.load_model('chat_model')

   #load tikenizer object
   with open('tokenizer.pickle','rb') as handle:
      tokenizer=pickle.load(handle)

  # load label encoder object
   with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc) 
        print("---------------------------")
        print (lbl_encoder)   


   # parameters
   max_len = 20
    
   while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == "quit":
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
        
        print(result)

        #For decoding labels
        tag = lbl_encoder.inverse_transform(([np.argmax(result)]))
        print("******************")
        print(tag)
        print("******************")
        for i in data['intents']:
            # print("-------------------")
            # print(i)
            if i['tag'] == tag:
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))

        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chat()     




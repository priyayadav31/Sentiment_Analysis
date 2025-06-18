# Step 1 : Impporting Libraries and Load the Model

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model


# Load the IMDB datsets word index

word_index = imdb.get_word_index()

reverse_word_index = {value:key for key,value in word_index.items()}


# Load the pre-trained model with Relu Activation
model = load_model('IMDB Review Sentiment Analysis_1.h5')



# Step 2 : Helper function
# Function to decod reviews

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3,'?') for i in encoded_review])

# Function to preprocess user input

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word,2) + 3 for word in words]
    padded_reviews = sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_reviews


# Step 3 : Prediction Function

def prediction_sentiment(review):
    preprocessed_input = preprocess_text(review)

    prediction = model.predict(preprocessed_input)

    sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"

    return sentiment, prediction[0][0]

# Step 4 : Streamlit App for Prediction

import streamlit as st

st.title("IMDB Review Sentiment Analysis")

user_input = st.text_area("Enter Movie Review")

if st.button('Classify'):

    # preproceesed input
    preprocessed_input = preprocess_text(user_input)

    # make prediction
    prediction = model.predict(preprocessed_input)
    sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"

    # Display the result
    st.write(f'Review:{user_input}')
    st.write(f'Senitment:{sentiment}')
    st.write(f'Prediction Score:{prediction[0][0]}')
else:
    st.write('Please Enter a Movie Review For Analysis.')
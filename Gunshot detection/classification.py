import numpy as np
import librosa
from python_speech_features import mfcc
from sklearn.mixture import GaussianMixture
import pickle

# Load the trained GMM model
with open('gmm_model_mp5.pkl', 'rb') as file:
    gmm_classifier = pickle.load(file)

# Test audio file path
audio_file = "C:/Users/Avishi Bansal/Downloads/archive/3 (12).wav"

# Load the audio file
signal, rate = librosa.load(audio_file, sr=16000)

# Extract MFCC features
mfcc_features = mfcc(signal, rate, numcep=16)
mfcc_features = np.mean(mfcc_features, axis=0)  # Averaging the MFCC features over the frames

# Make prediction using the GMM classifier
prediction = gmm_classifier.predict([mfcc_features])

# Display the predicted class label
print(f"Predicted Class: {prediction[0]}")

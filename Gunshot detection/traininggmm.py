import os
import numpy as np
import librosa
import pickle
from sklearn.mixture import GaussianMixture

# Define dataset path
dataset_path = "C:/Users/Avishi Bansal/Downloads/archive/MP5"

# List all audio files
audio_files = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) if f.endswith(".wav")]

# Assign labels (Modify based on your dataset)
labels = list(range(len(audio_files)))  # Example: Assign unique labels

# Prepare training data
X_train = []
y_train = []

for i, file in enumerate(audio_files):
    print(f"Processing: {file}")  # Debugging

    # Load audio file
    signal, sr = librosa.load(file, sr=16000)

    # Extract MFCC features
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=16)

    # Take mean MFCC features for classification
    X_train.append(np.mean(mfcc_features, axis=1))
    y_train.append(labels[i])

# Convert to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)

# Train the GMM model
gmm_classifier = GaussianMixture(n_components=len(audio_files))  # Number of unique sounds
gmm_classifier.fit(X_train)

# Save the trained model
with open("gmm_model_mp5.pkl", "wb") as file:
    pickle.dump(gmm_classifier, file)

print("✅ GMM model trained and saved as 'gmm_model_mp5.pkl'!")

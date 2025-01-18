import sounddevice as sd
import numpy as np
import pywt
from python_speech_features import mfcc
from sklearn.mixture import GaussianMixture

# Parameters
SAMPLE_RATE = 16000
FRAME_SIZE = 2048
OVERLAP = 1024
WAVELET = 'db6'

# Initialize GMM classifier (placeholder for testing)
gmm_classifier = GaussianMixture(n_components=4)

# Real-time audio callback function
def audio_callback(indata, frames, time, status):
    if status:
        print("Audio Status:", status)

    # Preprocess audio frame
    audio_frame = indata[:, 0]  # Single channel
    wavelet_coeffs = pywt.wavedec(audio_frame, WAVELET, level=3)
    
    # Compute tree energy
    tree_energy = sum([np.sum(coeff**2) for coeff in wavelet_coeffs])
    print(f"Tree Energy: {tree_energy}")  # Debugging

    # Transient detection logic
    detection_threshold = 100 # Lower threshold for debugging
    if tree_energy > detection_threshold:
        print("Transient detected!")
        
        # Extract MFCC features for classification
        mfcc_features = mfcc(audio_frame, SAMPLE_RATE, numcep=16)
        prediction = "dummy_class"  # Replace with actual GMM prediction
        print(f"Classified as: {prediction}")

# Start audio stream
stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=1,
    blocksize=FRAME_SIZE,
    callback=audio_callback
)

print("Starting audio stream...")
with stream:
    sd.sleep(10000)  # Stream for 10 seconds

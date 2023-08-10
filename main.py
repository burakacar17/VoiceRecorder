import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


freq = 44100

duration = 15

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()

write("recording0.wav", freq, recording)

# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)

import numpy as np

# Load the audio signal from the .npy file
audio_signal = np.load('pulse_arim.npy')

#spectrogram이 어려운게, 일단, 시간상 값이 어떻게 나타났는지에 대해서 정확히 모른다
#그러니 npy 파일에 저장된 x,y이 정확히 어떤건지 확인한후 sample_rate를 조절해야될듯

from scipy import signal
import matplotlib.pyplot as plt
sample_rate = 10

# Compute the spectrogram
f, t, Sxx = signal.spectrogram(audio_signal, fs=sample_rate)

# Plot the spectrogram
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto')
plt.title('Spectrogram of Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.colorbar(label='Power/Frequency (dB/Hz)')
plt.show()


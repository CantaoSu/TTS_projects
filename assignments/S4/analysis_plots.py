import os
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

# Function to plot the waveform
def plot_waveform(ax, audio, sr, title):
    ax.plot(audio)
    ax.set_title(title)
    ax.set_ylabel('Amplitude')

# Function to plot the spectrum
def plot_spectrum(ax, audio, sr, title):
    fft = np.fft.fft(audio)
    magnitude = np.abs(fft)
    frequency = np.linspace(0, sr, len(magnitude))
    ax.plot(frequency[:int(len(frequency)/2)], magnitude[:int(len(magnitude)/2)])
    ax.set_title(title)
    ax.set_ylabel('Magnitude')
    ax.set_xlabel('Frequency')

# Function to plot the spectrogram
def plot_spectrogram(ax, audio, sr, title):
    Sxx, freqs, bins, im = ax.specgram(audio, Fs=sr, NFFT=2048, noverlap=1024, cmap='viridis')
    ax.set_title(title)
    ax.set_ylabel('Frequency (Hz)')
    ax.set_xlabel('Time (s)')
    return Sxx, freqs, bins, im

def generate_and_save_plots(original_audio_path, vocoded_audio_path, file_type, save_dir):
    original_sr, original_audio = wavfile.read(original_audio_path)
    vocoded_sr, vocoded_audio = wavfile.read(vocoded_audio_path)

    if original_sr != vocoded_sr:
        raise ValueError(f"Sample rates are different for {file_type}. Resampling might be necessary.")

    fig, axs = plt.subplots(6, 1, figsize=(10, 12))  # 6 rows, 1 column

    # Waveform plots
    plot_waveform(axs[0], original_audio, original_sr, 'Original Audio Waveform')
    plot_waveform(axs[1], vocoded_audio, vocoded_sr, 'Vocoded Audio Waveform')

    # Spectrum plots
    plot_spectrum(axs[2], original_audio, original_sr, 'Original Audio Spectrum')
    plot_spectrum(axs[3], vocoded_audio, vocoded_sr, 'Vocoded Audio Spectrum')

    # Spectrogram plots
    plot_spectrogram(axs[4], original_audio, original_sr, 'Original Audio Spectrogram')
    plot_spectrogram(axs[5], vocoded_audio, vocoded_sr, 'Vocoded Audio Spectrogram')

    fig.suptitle(f'{file_type.capitalize()} Speech Comparison', fontsize=16)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    save_path = os.path.join(save_dir, f'{file_type}_speech_comparison.png')
    plt.savefig(save_path)
    plt.close()

    print(f"Saved: {save_path}")

# Specify the directories
original_dir = 'recordings/'  
vocoded_dir = 'vocoded/'      
save_dir = 'plots/comparison with vocoded of unchanged pitch/' 

# Automatically match files in both directories and generate plots
for original_file in os.listdir(original_dir):
    file_type = original_file.replace('recording_', '').replace('.wav', '')
    vocoded_file = f"vocoded_{original_file}"

    original_audio_path = os.path.join(original_dir, original_file)
    vocoded_audio_path = os.path.join(vocoded_dir, vocoded_file)

    if os.path.isfile(original_audio_path) and os.path.isfile(vocoded_audio_path):
        generate_and_save_plots(original_audio_path, vocoded_audio_path, file_type, save_dir)

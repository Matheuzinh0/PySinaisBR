from scipy.io import wavfile

# Carregar arquivo WAV
taxa, audio = wavfile.read('audio.wav')

# Analisar espectro
freq, espectro = Transformadas.fourier(audio[:,0], 1/taxa)

# Filtrar ruído
audio_limpo = ProcessamentoSinal.filtrar(
    audio,
    freq_corte=4000,
    taxa_amostragem=taxa
)

# Gerar sinal de teste via CLI
python -m pysinaisbr.gerador_sinal -f 50 -d 1 -o sinal.csv

# Plotar sinal diretamente
python -m pysinaisbr.visualizador plotar sinal.csv

from pysinaisbr import Transformadas, Visualizacao
import numpy as np

t = np.linspace(0, 1, 1000)
sinal = np.sin(2*np.pi*50*t) + 0.5*np.random.normal(size=1000)

freq, espectro = Transformadas.fourier(sinal, t)
Visualizacao.plotar_espectro(freq, espectro)

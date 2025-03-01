from pysinaisbr import ModulacaoDigital

bits = np.random.randint(0, 2, 1000)
sinal_modulado, _ = ModulacaoDigital.qpsk(bits)

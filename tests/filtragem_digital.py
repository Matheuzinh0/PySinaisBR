from pysinaisbr import ProcessamentoSinal

sinal_ruidoso = sinal + 0.8*np.random.randn(1000)
sinal_filtrado = ProcessamentoSinal.filtrar(sinal_ruidoso, 100, 1000)

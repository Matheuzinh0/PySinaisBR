# Sistema de comunicação completo
bits = np.random.randint(0, 2, 1000)
codificador = CodificacaoCanal(t_correcao=3)
bits_protegidos = codificador.codificar_reed_solomon(bits)
sinal_tx, _ = ModulacaoDigital.qpsk(bits_protegidos)

# Canal com ruído
sinal_rx = sinal_tx + 0.1*np.random.randn(len(sinal_tx))

# Recepção
bits_rx = ModulacaoDigital.demodular_qpsk(sinal_rx)
bits_decod = codificador.decodificar_reed_solomon(bits_rx)

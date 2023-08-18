# Coleta a Entrada
print("\n ***************** PREPARAÇÃO DE MOTORES ***************** \n")
diametroPistao = float(input("Digite o Diametro do Pistão (mm): ").replace(",", "."))
cursoPistao = float(input("Digite o Curso do Pistão (mm): ").replace(",", "."))
nCil = int(input("Digite a Quantidade de Cilindros: "))
mmCabecote = float(input("Digite a Espessura da Junta de Cabeçote (mm): ").replace(",", "."))
txAtual = float(input("Digite a Taxa de Compressão Atual: ").replace(",", "."))
txDesejada = float(input("Digite a Taxa de Compressão Desejada: ").replace(",", "."))

# Faz o Calculo
raioPistao = diametroPistao / 2
areaPistao = raioPistao **2 * 3.141592
volJunta = areaPistao * mmCabecote / 1000
volumePistao = raioPistao ** 2 * cursoPistao * 3.141592 / 1000
Cil = volumePistao * nCil
volMortoDesejado = volumePistao / (txDesejada - 1)
volMortoAtual = volumePistao / (txAtual - 1)
volCamAtual = volMortoAtual - volJunta
volCamDesejado = volMortoDesejado - volJunta
volCamAtualCorr = volCamAtual ** (1/3)
volCamDesejadoCorr = volCamDesejado ** (1/3)
rebaixarCabecote = (volCamAtualCorr - volCamDesejadoCorr) * 10

# Printa na Tela
print("\n ***************** RESULTADO ***************** \n")
print("A sua cilindrada é:", Cil)
print("A sua Taxa de Compressão Atual é:", txAtual)
print("A sua Taxa de Compressão Desejada é:", txDesejada)
print("Rebaixe o Cabeçote em:", rebaixarCabecote, "mm")
print("\n ***************** PAULO HENRIQUE AZEVEDO DO NASCIMENTO ***************** \n")

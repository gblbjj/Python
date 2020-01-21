import pycep_correios

def meu_cep(seu_cep):
    endereco = pycep_correios.consultar_cep(seu_cep)
    return endereco

seu_cep = input("digite seu cep:\n")
p = (len(seu_cep))

while (p != 8):
    seu_cep = input("cep invalido digite novamente seu cep:\n")
    p = (len(seu_cep))
   
x = meu_cep(seu_cep)
print(x['end'])
    
    

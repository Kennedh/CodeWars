"""
Uma criança está brincando com uma bola no enésimo andar de um prédio alto.
A altura desse andar em relação ao nível do solo, h, é conhecida.

Ela joga a bola pela janela. A bola quica (por exemplo) a dois terços de sua altura (um quique de 0,66).

Sua mãe olha pela janela a 1,5 metro do chão.

Quantas vezes a mãe verá a bola passar em frente à sua janela (incluindo quando ela estiver caindo e quicando)?

Três condições devem ser atendidas para que um experimento seja válido:
O parâmetro de flutuação "h" em metros deve ser maior que 0
O parâmetro de flutuação "bounce" deve ser maior que 0 e menor que 1
O parâmetro de flutuação "window" deve ser menor que h.
Se todas as três condições acima forem atendidas, retorne um inteiro positivo; caso contrário, retorne -1.

Observação:
A bola só poderá ser vista se a altura da bola que quica for estritamente maior que o parâmetro da janela.
"""

def bouncing_ball(h, bounce, window):
    res = 0
    bouncing = h
    if h > 0 and (bounce > 0 < 1) and window < h:
        while bouncing > window:
            res += 1
            bouncing = bounce * bouncing
            if bouncing > window:
                res += 1
        return res
    else:
        return -1

# Teste

print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(30, 0.75, 1.5))
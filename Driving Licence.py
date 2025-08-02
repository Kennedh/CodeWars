"""Tarefa
O número de motorista do Reino Unido é composto pelos dados pessoais do motorista. As letras e dígitos individuais podem
ser codificados usando as informações abaixo.
Regras
1–5: Os cinco primeiros caracteres do sobrenome (completados com 9s se houver menos de 5 caracteres)

6: O dígito da década a partir do ano de nascimento (por exemplo, para 1987, seria 8)

7–8: O mês de nascimento (o 7º caractere é incrementado em 5 se a motorista for do sexo feminino, ou seja, 51–62 em vez
de 01–12)

9–10: A data dentro do mês de nascimento

11: O dígito do ano a partir do ano de nascimento (por exemplo, para 1987, seria 7)

12–13: A letra inicial do primeiro nome e do nome do meio, complet ada com um 9 se não houver nome do meio

14: Dígito arbitrário – geralmente 9, mas decrementado para diferenciar motoristas com os primeiros 13 caracteres em
comum. Sempre usaremos 9

15–16: Dois dígitos de verificação do computador. Sempre usaremos "AA"
Sua tarefa é codificar um número de carteira de habilitação do Reino Unido usando uma matriz de dados. A matriz terá a
seguinte aparência:

data = ["John","James","Smith","01-Jan-2000","M"]
Onde os elementos são os seguintes

0 = Nome
1 = Nome do meio (se houver)
2 = Sobrenome
3 = Data de nascimento (no formato Dia Mês Ano, pode incluir o nome completo do mês ou apenas uma abreviação, ou seja,
setembro ou set)
4 = M - Masculino ou F - Feminino
Você precisará digitar o número completo da carteira de motorista de 16 dígitos, em LETRAS MAIÚSCULAS.

Boa sorte e aproveite!"""

def mounth(m):
    mounths = {
        'jan': '01', 'january': '01',
        'feb': '02', 'february': '02',
        'mar': '03', 'march': '03',
        'apr': '04', 'april': '04',
        'may': '05',
        'jun': '06', 'june': '06',
        'jul': '07', 'july': '07',
        'aug': '08', 'august': '08',
        'sep': '09', 'september': '09', 'sept': '09',
        'oct': '10', 'october': '10',
        'nov': '11', 'november': '11',
        'dec': '12', 'december': '12',
    }
    return mounths[m.strip().lower()]

def driver(data):
    m = mounth(data[3].split("-")[1])
    if data[-1].lower() == "f":
        m = int(m) + 50
    d = data[3].split("-")[0]
    n = data[0][0]
    if data[1] == "":
        n += "9"
    else:
        n += data[1][0]
    return data[2][:5].upper().ljust(5,"9") + data[3][-2] + str(m) + d + data[3][-1] + n + "9" + "AA"

# Teste

print(driver(["John", "James", "Smith", "01-Jan-2000", "M"]))
print(driver(["Johanna", "", "Gibbs", "13-Dec-1981", "F"]))
print(driver(["Andrew", "Robert", "Lee", "02-September-1981", "M"]))
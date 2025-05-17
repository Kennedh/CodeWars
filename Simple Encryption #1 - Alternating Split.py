"""
Implemente um algoritmo de pseudocriptografia que,
dada uma string Se um inteiro N,
concatene todos os caracteres indexados ímpares de Scom todos os caracteres indexados pares de S.
Esse processo deve ser repetido Nvárias vezes.

Exemplos:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Junto com a função de criptografia, você também deve implementar uma função de descriptografia que reverta o processo.

Se a string Sfor um valor vazio ou o inteiro Nnão for positivo, retorne o primeiro argumento sem alterações.
"""

def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    else:
        while n > 0:
            n -= 1
            t1 = encrypted_text[:int(len(encrypted_text) / 2)]
            t2 = encrypted_text[int(len(encrypted_text) / 2):len(encrypted_text)]
            t1 += "ª"
            encrypted_text = "".join(y + x for x, y in zip(t1, t2))
            encrypted_text = encrypted_text.replace("ª","")
    return encrypted_text


def encrypt(text, n):
    i = ""
    p = ""
    if not text or n <= 0:
        return text
    else:
        while n > 0:
            n -= 1
            for idx, l in enumerate(text):
                if idx % 2 == 0:
                    p += l
                else:
                    i += l
            text = i + p
            i = ""
            p = ""
    return text

# Teste

print(encrypt("This is a test!", 0))
print(encrypt("This is a test!", 1))
print(encrypt("This is a test!", 2))
print(encrypt("This is a test!", 3))
print(encrypt("This is a test!", 4))

print(decrypt("hsi  etTi sats!", 1))
print(decrypt("s eT ashi tist!", 2))
print(decrypt(" Tah itse sits!", 3))
print(decrypt("This is a test!", 4))


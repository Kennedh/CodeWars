"""
Descrição:
Criptografe isso!

Você quer criar mensagens secretas que possam ser decifradas pelo kata " Decipher this! ". Aqui estão as condições:

Sua mensagem é uma sequência contendo palavras separadas por espaços.
Você precisa criptografar cada palavra na mensagem usando as seguintes regras:
A primeira letra deve ser convertida em seu código ASCII.
A segunda letra deve ser trocada pela última letra
Mantendo a simplicidade: não há caracteres especiais na entrada.
"""

def encrypt_this(text):
    res = []
    temp = []
    for word in text.split():
        if len(word) > 2:
            temp = list(word)
            temp[1], temp[-1] = temp[-1], temp[1]
            temp[0] = str(ord(temp[0]))
            res.append("".join(temp))
        else:
            temp = list(word)
            temp[0] = str(ord(temp[0]))
            res.append("".join(temp))
    return " ".join(res)

# Teste

print(encrypt_this('OxlIyHAKtTlHaWoZ aUVoJhRZoq BnFnWiNdpIQwDAAaI ITjpRIcvzTxGvYdbrp uIn SIeib uwPlbObCkM UkkNl XiHzljgLMzeTzUvMGu wkDgqXcWrufGWS UhCu oEpmwMGohRWuQlpg IRoTXouzevhNucH GiRK Rg v brKUkfSGRyhj pHpUUjiWUHobdPIls KLCOfgnc EdKPtmiolvc gNeCcY emL PEX qGLkdvAyRySUJ zTJqtDMoQ SfKIvnFpUFAisIOFdpkh rZzHgynFcp zukHqJ zv nHqiPXCdDNMcg kuTbhPMJ M zO JMBmHuy CMDMiKtZtcsnHmuAVP IpKHzeMKEMIOiIGgqHP NTVIMXlkbAYGdgyyKDL v gvLoSQIqzKJSl mcqRuiRqfQMa zoSjieR oJyfXXoIe gKvXXXOexlk SgE bBFDLqFEgXdcIWbYRo pLbATrqToFLdrpuVgAi IgT meVaiCFZPXLIRgZWMP Mkxde'))
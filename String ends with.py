"""
Complete a solução para que ela retorne verdadeiro se o primeiro argumento (string)
passado terminar com o segundo argumento (também uma string).
"""

def solution(text, ending):
    if ending in text:
        leng = len(ending)
        if text[-leng:] == ending:
            return True
        else:
            return False
    else:
        return False
# Teste

print(solution( "samurai", "ai"    ))
print(solution( "ninja",   "jaf"    ))
print(solution("sensei",  "i"))
print(solution("abc",     "te"))
print(solution("abcabc",  "bc"))
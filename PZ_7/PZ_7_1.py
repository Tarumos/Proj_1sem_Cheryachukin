# Вариант 29
# Дан символ C и строки S, S0. После каждого вхождения символа C в строку S вставить строку S0
import random

ru_letters = u"абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_letters = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
tj_letters = u"ғӣқӯҳҷҒӢҚӮҲҶ"

letters = ru_letters + en_letters + tj_letters

K = random.randrange(1, 21)  # после каждого вхождения символа в S символ вставляется в S0
S = ''.join(random.choice(letters) for _ in range(K))
C = random.choice(S)
S0 = '***'
print("K:", K)
print("String:", S)
print("S0:", S0)
print("Character: ", C)

S_new = ""
for i in S:  # цикл for
    if i == C:
        S_new += S0
    S_new += i
print("New string:", S_new)

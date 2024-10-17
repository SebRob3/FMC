def primes(m):
    p = 1
    q = m
    
    if ((m)**(1/2))%2 == 0: return max_num
    
    max_num = int((m)**(1/2))
    
    for i in range(2,max_num):
        if (m/i) == m//i:
            p = i
            q = m//i
            return p,q
    
    return p,q

def euclides(a, b):
    qi = []
    ri = []
    gcd = None
    
    r = b
    q = a // b
    mod = a % b
    ri.append(a)
    ri.append(b)
    qi.append(None)
    qi.append(q)
    while mod != 0:
        r, q, mod = mod, r//mod, r % mod
        ri.append(r)
        qi.append(q)
    
    gcd = ri[-1]
    return gcd, ri, qi

def extendido_euclides(qi):
    si = [1,0]
    ti = [0,1]
    for i in range(2, len(qi)):
        si.append(si[i-2] - (qi[i-1]*si[i-1]))
        ti.append(ti[i-2] - (qi[i-1]*ti[i-1]))
    
    return si[-1], ti[-1]

def square_and_multiply(base, exp, mod):
    bin_exp = list(str(bin(exp)))[2:]
    result = 1
    for i in bin_exp:
        if i == "1":
            result = ((result**2) * base) % mod
        else:
            result = (result**2) % mod
    
    return result

def encrypt_rsa(message, p, q, e):
    m = p*q
    phi_m = (p - 1) * (q - 1)

    gcd, ri, qi = euclides(e, phi_m)
    d, s = extendido_euclides(qi)
    d += phi_m if d < 0 else 0
    
    return square_and_multiply(message, e, m), d

def des_encrypt_rsa(message, m, e):
    p, q = primes(m)
    phi_m = (p - 1) * (q - 1)
    
    gcd, ri, qi = euclides(e, phi_m)
    d, s = extendido_euclides(qi)
    d += phi_m if d < 0 else 0
    
    return square_and_multiply(message, d, p*q)

p = 83
q = 97
e = 5
message = 100
c = encrypt_rsa(message, p, q, e)[0]
d = encrypt_rsa(message, p, q, e)[1]
print(message, c, d)
print(des_encrypt_rsa(c, p*q, e))

abcdario = list("abcdefghijklmnopqrstuvwxyz") 

def format_message(message):
    tilde = {
        "á" : "a",
        "é" : "e",
        "í" : "i",
        "ó" : "o",
        "ú" : "u"
    }
    message = message.lower()
    message = list(message)
    for i, char in enumerate(message):
        if char in list(tilde.keys()):
            message[i] = tilde[char]
        elif char not in abcdario:
            message[i] = ""
    
    return "".join(message)

def encrypt_afin(message, a, b):
    message = format_message(message)
    return "".join(list(abcdario[((a*abcdario.index(m))+b)%len(abcdario)] for m in message))

def des_encrypt_afin(message, a, b):
    message = format_message(message)
    inverso_a = extendido_euclides(euclides(a, len(abcdario))[2])[0]

    return "".join(list(abcdario[(inverso_a*(abcdario.index(m)-b))%len(abcdario)] for m in message))

message = "Si la gente no cree que las matemáticas son simples, es solo porque no se dan cuenta de lo complicado que es la vida"
encriptacion = encrypt_afin(message, 7, 2)
print(encriptacion)
print(des_encrypt_afin(encriptacion, 7, 2))
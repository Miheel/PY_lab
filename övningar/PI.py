import math
def fak(n):
    if n == 0:
        return 1
    else:
        return n * fak(n - 1)

def ser_term_chu(k):
    T = 13591490 + 545140134 * k
    N = pow(-262537412640768000, k)
    FT =  fak(6 * k)
    FN = fak(3 * k) * pow(fak(k), 3)
    term = (FT * T)/(FN * N)
    return term

def chudnovsky(n):
    const = 426880 * math.sqrt(10005)
    pi, k, fin_sum= 0, 0, 0

    while k < n:
        #print("K: ", k)
        S = ser_term_chu(k)
        fin_sum += S
        k += 1
    pi = const / fin_sum
    return pi

def leibnitz(k):
    S, n = 0, 0
    while n <= k:
        S += 4 * (pow(-1, n)/(2 * n + 1))
        #print(S, n)
        n += 1
    return S

def ser_term_ram(k):
    T = 1103 + 26390 * k
    N = pow(396, 4 * k)
    FT = fak(4 * k)
    FN = pow(fak(k), 4)
    term = (FT * T) / (FN * N)
    return term

def ramanujans():
    fin_sum, k, pi = 0, 0, 0
    const = (2 * math.sqrt(2)) / 9801
    pi_loop = True
    while pi_loop:

        S = ser_term_ram(k)
        #print("K: ", k)
        fin_sum += S

        if S < 1e-40:
            pi_loop = False
        else:
            k += 1
    pi = 1/(fin_sum * const)
    return pi

print("ram: ", ramanujans(), "\nlei: ", leibnitz(10000), "\nchu: ", chudnovsky(100))

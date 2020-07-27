import sys

no_1 = int(sys.argv[1])
no_2 = int(sys.argv[2])

def extended_gcd(no_1, no_2):
    if no_1 == 0:
        return no_2, 0, 1

    gcd, u1, v1 = extended_gcd(no_2 % no_1, no_1)

    u = v1 - (no_2 // no_1) * u1
    v = u1

    return gcd, u, v

g, u, v = extended_gcd(no_1, no_2)
print("gcd = " + str(g))
print("u = " + str(u))
print("v = " + str(v))

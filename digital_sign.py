import random
from miller_rabin import is_prime_mr
from eucledian import extended_eucledian
from chinese_rem import chinese_rem
from modular_exp import  modular_exp

sep = f"\n{'-'*37}\n"

def generate_large_primes():
    number_one = random.getrandbits(128)
    number_two = random.getrandbits(128)

    while not(is_prime_mr(number_one) and is_prime_mr((number_two))) and number_one != number_two:
        number_one = random.getrandbits(128)
        number_two = random.getrandbits(128)
        
    return number_one, number_two

def generate_e_and_d(phin):
    # e must be between 1 and phin
    # e and phin must be relative primes
    random_e = random.randrange(1+1, phin)
    result = extended_eucledian(phin, random_e)

    # first value is the GCD,
    # if we supply the paramters in this order: phin, e
    # then the last value (y) is the d key
    while result[0] != 1:
        random_e = random.randrange(1+1, phin)
        result = extended_eucledian(phin, random_e)

    temp_d = result[2]

    # the d value must be greater than 1 and less than phin
    if temp_d < 1:
        temp_d += phin
    elif temp_d >= phin:
        temp_d -= phin

    return random_e, temp_d

if __name__ == '__main__':
    # Generateing two large UNIQUE prime numbers
    print("Step 1: Generating two unqiue large prime numbers.")
    (p, q) = generate_large_primes()
    print(f"Generated: {p} and {q} prime numbers.")
    print(f"Output of Miller Rabin with input p ({is_prime_mr(p)})  and q ({is_prime_mr(q)})", sep)

    # Calculating the RSA modulus
    modulus = p*q
    print(f"Calculated RSA modulus: {modulus}", sep)

    # Number of possible keys
    phin = (p-1)*(q-1)
    print(f"Number of possible keys: {phin}", sep)


    # Generating the encrypting and decrypting values
    (e, d) = generate_e_and_d(phin)
    print(f"Value of e and d: ", e, d, sep)

    # Signing
    message = 11 # message: a number
    print(f"Input message: {message}")

    # chinese_rem paramters: message, q and p primes,  secret key, RSA modulus
    S = chinese_rem(message, q, p, d, modulus)
    print(f"Signed message: {S}")

    # Verification
    # Decrypting the encrypted message
    decreptyed = modular_exp(S, e, modulus)
    print(f"Decrepted message: {decreptyed}")
    print(f"Is the message and the decreptyed message the same? {message == decreptyed}")
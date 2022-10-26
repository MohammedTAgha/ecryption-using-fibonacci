def isPrime(n):
    num =n
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def get_fPrimes(n):
    list = []
    nterms = n
    n1, n2 = 0, 1
    count = 0
    # check if the number of terms is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       while count < nterms:
           if isPrime(n1):
               list.append(n1)
               print(n1)
               count += 1
           nth = n1 + n2
           n1 = n2
           n2 = nth
    return list

get_fPrimes(4)
isPrime(7)
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
               count += 1
           nth = n1 + n2
           n1 = n2
           n2 = nth
    return list

def main ():
    i = ''
    plan = input('enter plan text :')
    primes=get_fPrimes(len(plan))
    print(primes)
    key = input('enter encryption key :')
    keyAscii=ord (key)
    targetList =list(map(chr, range(keyAscii, keyAscii+ primes[len(primes)-1])))
    for j in range(0 , len(primes)):
        print(primes[j])
        i = i + targetList[primes[j]-1]


    print(i)
    print(targetList)
    # plan = input('enter plan text :')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # print(list(map(chr, range(97, 123))))
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

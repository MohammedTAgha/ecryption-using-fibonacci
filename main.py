import re
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
    if nterms <= 0:
       print("Please enter a positive integer")
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
    cipher=''
    plan = input('enter plan text :')
    primes=get_fPrimes(len(plan))

    key = input('enter encryption key :')
    keyAscii=ord (key)
    targetList =list(map(chr, range(keyAscii, keyAscii+ primes[len(primes)-1]))) #genarate char sequance
    for j in range(0 , len(primes)): # replace plan text chars and generate intermediate text
        i = i + targetList[primes[j]-1]

    #convert plan and intermediate text int list
    list1 = [*plan]
    list2 = [*i]
    #convert tow list into asci
    ascii1 = [ord(x) for x in list1]
    ascii2 = [ord(x) for x in list2]

    #
    print('*=> step 1 :')
    print('plan text ascii', ascii1)
    print('*=> step 2 :')
    print('our fib primes are ', primes)
    print('intermediate text is ', i)
    print('*=> step 3 :')
    print('intermediate text ascii', ascii2)

    #
    #get summation of tow lists
    sum = []
    for planChar in range(len(ascii1)):
        sum.append(ascii1[planChar] + ascii2[planChar])
        #converting each added to unicode
        charcipher = (re.sub('.', lambda x: r'% 4X' % ord(x.group()), str(sum[planChar])))
        cipher = cipher + charcipher
    print('*=> step 4 :')
    print('Add ASCII codes of plain text to Intermediate text' , sum)
    print('*=> step 5 :')
    print('previous converted to uni code')
    print(cipher)

    # print(i)
    # print(targetList)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # print(list(map(chr, range(97, 123))))
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

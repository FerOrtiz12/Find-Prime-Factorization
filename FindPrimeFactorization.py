def isPrime (num):
    import math
    if ( num < 2 or num % 2 == 0 ):
        return (num==2)
    divisor=3
    while (divisor <= math.sqrt( num )):
        if ( num % divisor == 0 ):
            return False
        else:
            divisor += 2
    return True

def findNextPrime (num):
    if (num<2):
        return 2
    if (num%2==0):
        num -= 1
    guess=num+2
    while (not isPrime(guess)):
        guess += 2
    return guess

def main():
    print("Find Prime Factors:")
    while (True):
        num=int(input("Enter a positive integer (or 0 to stop): "))
        if (num==0):
            print("Goodbye!")
            break
        elif (num==1):
            print("  1 has no prime factorization.")
            print()
        elif (num < 0):
            print("  Negative integer entered.  Try again.")
            print()
        elif (isPrime(num) == True):
            prime=list([num])
            print("  The prime factorization of", num, "is:", prime)
            print()
        else:
            factors=list()
            d=2
            newnum=num
            while (newnum!=1):
                if (newnum % d == 0):
                    factors.append(d)
                    newnum=newnum/d
                elif (newnum % d != 0):
                    d=findNextPrime(d)
                
            print("  The prime factorization of", num, "is:", factors)
            print()
                    
                    
            
main()

#FizzBuzz
#program to solve fizzbuzz probleam
def fizzbuzz(n):
    for i in range(1,n):
        if(i%3==0 and i%5==0):
            print(str(i)+" =FizzBuzz")
        else:
            if(i%3==0):
                print(str(i)+" =Fizz")
            else:
                if(i%5==0):
                    print(str(i)+" =Buzz")
                else:
                    print(str(i))
fizzbuzz(1001)

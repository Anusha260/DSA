def birthdayCakeCandles(candles):
    a=max(candles)
    candles_count=0
    for i in candles:
        if i==a:
            candles_count+=1
    print(candles_count)
            


candles_count = int(input("enter the number").strip())

candles = list(map(int, input("enter the number").rstrip().split()))

result = birthdayCakeCandles(candles)



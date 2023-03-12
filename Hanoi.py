def Hanoi( n, start, finish ):
    if n <=0: return
    temp = 6 - start - finish
    Hanoi( n-1, start, temp )
    print( "Перенести диск",n, "із стержня", start,"На стержень", finish )
    Hanoi( n-1, temp, finish )
Hanoi(3,1,3)
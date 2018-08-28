for i in range(0,10):
    print(i)
    if i == 4 :
        pass
        #raise Exception ("Failing because i = 4 ")

try :
    print(10/0)

except ZeroDivisionError :
    print ("Division from Zero is not possible ")
except Exception :
    pass
except : pass 
finally :
    print("Success !!!!")

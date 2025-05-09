A = 1325

#def dec_bin(A):    
    #if A == 0:
        #return "0"
    #else :   
        #return dec_bin(A // 2) + str(A % 2) #and dec_bin(A // 16) +str(A % 16)

#print (dec_bin(A))

def dec_binhex(A):
    y = dec_binhex(A//2) + str(A % 2)
    x = dec_binhex(A // 16) + str(A % 16)
    return (x, y)

print(f"{dec_binhex(A)}")
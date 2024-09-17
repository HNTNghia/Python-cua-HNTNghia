import  math

try:
        r=float(input("nhap ban kinh: "))
        cv=2*math.pi*2
        dt=r*r*math.pi
        print("chu vi: ",cv)
        print(" dien tich: ",dt)

except:
    print("loi")
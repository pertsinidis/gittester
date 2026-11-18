def monaziga(ar):
    if ar%2==0:
        print("o arithmos",ar,"einai zigos")
        return ar
    else:
        print("o arithmos",ar,"einai monos")
        return ar



if __name__ == '__main__':
    x=int(input("dwse arithmo(gia telos 0):"))
    while x != 0:
        monaziga(x)
        x = int(input("dwse arithmo(gia telos 0):"))
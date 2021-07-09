#-----main function------
def main():
    captureData()

#----captureData------
def captureData():
    Notas = []
    pRevisar, pRecordadas = input().split()
    pRevisar = int(pRevisar)
    pRecordadas = int(pRecordadas)
    Notas = input().split()
    processData(Notas, pRecordadas)

#----process data-----
def processData(Notas, pRecordadas):
    NotasF = []
    Totalcopias = 0;
    TotalRecordadas = pRecordadas;

    for i in Notas:
        if i in NotasF:
            Totalcopias+=1
        else:
            a = "{}".format(i)
            NotasF.append(a)
    if TotalRecordadas > Totalcopias:
        TotalRecordadas = Totalcopias    
    print(Totalcopias, TotalRecordadas)


#------main------
if __name__ == "__main__":
    main()

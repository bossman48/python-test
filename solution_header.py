
import sys
import csv
from email import header

class CsvReaderClass():
        try:
            file = open("customersTest2.csv")
            type(file)
            csvreader = csv.reader(file)
            header = []
            header = next(csvreader)
            rows = []
            for row in csvreader:
                rows.append(row)
                
            file.close()
        except:
            print("Cannot open csv file or csv file is empty")

class MaskerClass(CsvReaderClass):
    minNameLenght=sys.float_info.max
    maxNameLenght=0
    avarageNameLenght=0
    minBilling=sys.float_info.max
    maxBilling=0
    avarageBilling=0

    def printAll(self):
        print("Rows type: ",type(self.rows))
        print("Rows : ",self.rows)
        print("Header type : ",type(self.rows))
        print("Header : ",self.header)


    #find the ascii value of the every character to replace with "X"
    def makeConfidentialString(self,string):
        result=""
        for character in string:
            if(ord(character)>=48 and ord(character)<=57):
                result+="X"
            elif(ord(character)>=65 and ord(character)<=90):
                result+="X"
            elif(ord(character)>=97 and ord(character)<=122):
                result+="X"
            else:
                result+=character
        return result

    def makeAllMailsConfidential(self):
        try:
            for row in self.rows:
                row[2]=self.makeConfidentialString(row[2])
        except:
            print("Mail cannot be make confidential")
    
    def makeAllAdressesConfidential(self):
        try:
            for row in self.rows:
                row[4]=self.makeConfidentialString(row[4])
        except:
            print("Adress cannot be make confidential")

    def makeAllNamesConfidential(self):
        try:
            for row in self.rows:
                row[1]=self.makeConfidentialString(row[1])
        except:
            print("Names cannot be make confidential")

    def saveCsvFile(self):
        try:
            with open('masked_clients.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                # write the header
                writer.writerow(self.header)
                # write the data
                writer.writerows(self.rows)
        except:
            print("Cannot save masked_clients.csv")

    def saveCsvFileForExtraPart(self):
        try:
            header = [' ', 'Max', 'Min', 'Avarage']
            data = [["Name",self.maxNameLenght,self.minNameLenght,self.avarageNameLenght],
            ["Billing",self.maxBilling,self.minBilling,self.avarageBilling]]
            with open('report.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                # write the header
                writer.writerow(header)
                # write multiple rows
                writer.writerows(data)
        except:
            print("Cannot save report.csv")
        

    def getAvarageAndChangeBillingColoum(self):
        result=0
        try:
            rowCounter=len(self.rows)
            for row in self.rows:
                try:
                    if(row[3]=="" or row[3]==" "):
                        self.minBilling=0
                    if(float(row[3])>self.maxBilling):
                        self.maxBilling=float(row[3])
                    if(float(row[3])<self.minBilling):
                        self.minBilling=float(row[3])

                    result+=float(row[3])
                except:
                    print("String-float conversion error")
            for row in self.rows:
                row[3]=result/rowCounter
            self.avarageBilling=result/rowCounter
        except:
            print("Billing cannot be calculated")

        if(self.minBilling==sys.float_info.max):
            self.minBilling=0

    def getNamesLenght(self):
        result=0
        try:
            rowCounter=len(self.rows)
            for row in self.rows:
                try:
                    if(row[1]=="" or row[1]==" "):
                        self.minNameLenght=0
                    if(len(row[1])>self.maxNameLenght):
                        self.maxNameLenght=len(row[1])
                    if(len(row[1])<self.minNameLenght):
                        self.minNameLenght=len(row[1])

                    result+=len(row[1])
                except:
                    print("String's len function cannot run")
            self.avarageNameLenght=result/rowCounter
        except:
            print("Name lenght cannot be calculated")
        

        if(self.minNameLenght==sys.float_info.max):
            self.minNameLenght=0

    def challangeResult(self):
        self.makeAllMailsConfidential()
        self.makeAllNamesConfidential()
        self.makeAllAdressesConfidential()
        self.getAvarageAndChangeBillingColoum()
        self.saveCsvFile()

    def challangeExtraResult(self):
        self.getAvarageAndChangeBillingColoum()
        self.getNamesLenght()
        self.saveCsvFileForExtraPart()
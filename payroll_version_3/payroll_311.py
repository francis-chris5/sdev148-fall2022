# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:30:25 2022

Fall 2022 Projects

@author: c.s.francis
"""

import datetime

import csv

def writeCSVFile():
    with open("employeeComma.csv", "a") as toFile:
        more = input("is there another employee to enter data for? (yes/no) ")
        while more.lower() == "yes":
            name = input("TELL ME WHO IT IS THEN!!! ")
            rateOfPay = input("HOW MUCH DO THEY MAKE!!!! ")
            
            writer = csv.writer(toFile)
            
            writer.writerow([name, rateOfPay])

            more = input("is there another employee to enter data for? (yes/no) ")
            

def readCSVFile():
    employeeData = []
    with open("employeeComma.csv", "r") as fromFile:
        reader = csv.reader(fromFile)
        for line in fromFile.readlines():
            employeeData.append(line.replace("\n", "").split(","))
        print(employeeData)
    return employeeData

def getHours(name):
    hw = float(input(f"GIMME {name}'s HOURS!!!! "))
    return hw


def calculatePay(hoursworked, rateofpay):
    if hoursworked < 40:
        grosspay = hoursworked * rateofpay
    else:
        grosspay = (hoursworked-40) * rateofpay * 1.5 + 40 * rateofpay
    
    taxdeduction = grosspay * 0.15
    
    netpay = grosspay - taxdeduction
    
    return grosspay, taxdeduction, netpay

#nextuser = "yes"

def writePayStub():
    timestamp = datetime.date.today()
    employeeData = readCSVFile()
    payStubPrinter = open("weeklypay_csv.txt", "a")
    payStubPrinter.write("\n\n\n\n--------------------------------------------\n")
    payStubPrinter.write(str(timestamp) + "\n")
    payStubPrinter.write("Name\t\t\t\t | Gross Pay \t | Taxes \t | Net Pay\n")
    payStubPrinter.write("--------------------------------------------\n")
    
    for index in range(0, len(employeeData), 2):
        grosspay, taxdeduction, netpay = calculatePay(getHours(employeeData[index][0]), float(employeeData[index][1]))
        payStubPrinter.write(employeeData[index][0] + " \t\t\t\t | " + format(grosspay, ".2f") + " \t\t | " + format(taxdeduction, ".2f") + " \t | " + format(netpay, ".2f") + "\n\n\n")
    payStubPrinter.close()




if __name__ == "__main__":
    choice = int(input("""WHAT DO YOU WANT DO?
         --input 1 to add data to the database
         --input 2 to run weekly payroll
         --input 3 to exit
"""))
    if choice == 1:
        writeCSVFile()
    elif choice == 2:
        writePayStub()
    else:
        pass
    










###########################  WHITE SPACE FOR SCROLLING  ############

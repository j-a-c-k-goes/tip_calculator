# tip calculator
import math
from tip import tip
from total import total
from grand_total import grand_total

def main():
    print("tip calculator :)".upper())
    try:
        BILL_AMOUNT = float(input("what is the amount of your bill? "))
        if BILL_AMOUNT <= 0:
            print("try another amount that isn\'t zero or negative.")
            BILL_AMOUNT = float(input("what is the amount of your bill? "))
    except ValueError:
        print("string entered; please enter a valid number")
        BILL_AMOUNT = float(input("what is the amount of your bill? "))
    try:
        TIP_RATE = float(input("enter the tip rate: "))
        if TIP_RATE < 0:
            print("please use a positive tip rate")
            TIP_RATE = float(input("enter tip rate: "))
    except ValueError:
        print("please enter a valid number")
        TIP_RATE = float(input("enter a new tip rate: "))        
    TIP = tip(BILL_AMOUNT, TIP_RATE)
    TOTAL = total(BILL_AMOUNT, TIP_RATE)
    GRAND_TOTAL = grand_total(TOTAL)
    
if __name__ == "__main__":
    main()


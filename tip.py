# calculate tip
def tip(BILL_AMOUNT, TIP_RATE):
    tip = BILL_AMOUNT * (TIP_RATE / 100)
    tip = round(tip, 2)
    print(f'{TIP_RATE}% tip\t${tip}')
    return tip
if __name__ == "__main__":
    tip()

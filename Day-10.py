#Profit or loss calculator
cp=float(input("Enter the cost price of the product:"))
sp=float(input("Enter the selling price of the product:"))
if sp>cp:
    print("Profit is Rs.",sp-cp)
elif cp>sp:
    print("Lossis Rs.",cp-sp)
else:
    print("No profit No loss!500")

    

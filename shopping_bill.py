def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 0.18
    return total + gst

def calculateFashionGST(c, d):
    total = c + d
    gst = total * 0.13
    return total + gst

def calculateFoodGST(e):
    gst = e * 0.07
    return e + gst

def totalBill(a, b, c, d, e):
    return calculateElectronicsGST(a, b) + calculateFashionGST(c, d) + calculateFoodGST(e)

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    return total - discount

a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = total * 0.20
final = calculateDiscountedBill(a, b, c, d, e)

print(f"Electronics: (100 + 100) + 18% GST = {electronics:.2f}")
print(f"Fashion: (100 + 100) + 13% GST = {fashion:.2f}")
print(f"Food: 100 + 7% GST = {food:.2f}")
print(f"Total after GST = {total:.2f}")
print(f"20% discount on {total:.2f} = {discount:.2f}")
print(f"Final payable amount = {final:.2f}")
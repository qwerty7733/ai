# Blinkit Ordering Chatbot with Payment

print("Welcome to Blinkit")
print("-------------------")

name = input("Enter your name: ")

print("Hello", name)
print("Order your products below")

total = 0

while True:

    print("\nAvailable Products")
    print("1. Milk  - Rs 30")
    print("2. Bread - Rs 40")
    print("3. Chips - Rs 20")
    print("4. Juice - Rs 50")
    print("5. Checkout")

    choice = input("Enter your choice: ")

    if choice == '1':

        total += 30
        print("Milk added to cart")

    elif choice == '2':

        total += 40
        print("Bread added to cart")

    elif choice == '3':

        total += 20
        print("Chips added to cart")

    elif choice == '4':

        total += 50
        print("Juice added to cart")

    elif choice == '5':

        print("\nTotal Amount = Rs", total)

        print("\nSelect Payment Method")
        print("1. Cash on Delivery")
        print("2. UPI")
        print("3. Debit/Credit Card")

        payment = input("Enter payment option: ")

        if payment == '1':

            print("Cash on Delivery Selected")

        elif payment == '2':

            print("UPI Payment Successful")

        elif payment == '3':

            print("Card Payment Successful")

        else:

            print("Invalid Payment Method")

        print("\nOrder Confirmed")
        print("Your order will arrive in 10 minutes.")
        print("Thank you for ordering from Blinkit!")
        break

    else:

        print("Invalid choice")

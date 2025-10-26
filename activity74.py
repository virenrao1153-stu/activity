def calculate_return(total_bill, amount_paid):
    return amount_paid - total_bill

def main():
    print("=== Return Amount Calculator ===")
    
    total_bill = 2.50
    amount_paid = 4.00

    change = calculate_return(total_bill, amount_paid)

    print(f"Total bill: ${total_bill}")
    print(f"Amount paid: ${amount_paid}")
    print(f"Shopkeeper should return: ${change:.2f}")
    print("\nBest of luck!")

if __name__== "_main_":
    main()
def split_bill(total_bill, people, tip_percent):
    tip = total_bill * tip_percent / 100
    final_bill = total_bill + tip
    per_person = final_bill / people
    return tip, final_bill, per_person


def main():
    print("\n===== BILL SPLITTER =====")

    try:
        total_bill = float(input("Enter total bill amount: ₹"))
        people = int(input("Enter number of people: "))
        tip_percent = float(input("Enter tip percentage (%): "))

        if total_bill < 0 or people <= 0 or tip_percent < 0:
            print("Please enter valid values.")
            return

        tip, final_bill, per_person = split_bill(
            total_bill, people, tip_percent
        )

        print("\n===== BILL SUMMARY =====")
        print(f"Original Bill    : ₹{total_bill:.2f}")
        print(f"Tip Amount       : ₹{tip:.2f}")
        print(f"Final Bill       : ₹{final_bill:.2f}")
        print(f"Number of People : {people}")
        print(f"Each Person Pays : ₹{per_person:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()

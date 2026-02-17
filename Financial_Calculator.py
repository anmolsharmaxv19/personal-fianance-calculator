while True:

    print("\n===== FINANCIAL CALCULATOR =====")
    print("1. Simple Return")
    print("2. Compound Interest")
    print("3. CAGR")
    print("4. Loan EMI")
    print("5. Tax Calculator")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("You selected Simple Return") 
        Buy = float(input("Buying price :₹ "))
        Sell = float(input("Selling price :₹ "))
        Simple_Return = (Sell - Buy) / Buy   # fixed formula
        print("Total return is :", Simple_Return)

    elif choice == "2":
        print("You selected Compound Interest")
        p = float(input("Enter your principal amount: "))
        r = float(input("Enter your rate of interest: "))
        t = float(input("Enter your time interval: "))

        amount = p * (1 + r/100) ** t
        ci = amount - p 
        print("Your compound interest:", ci)
        print("Total amount:", amount)

    elif choice == "3":
        print("You selected CAGR")
        ending = float(input("Final Value (Ending Amount): ₹ "))
        begin = float(input("Initial Value (Starting Amount): ₹ "))
        year = float(input("Years: "))
        CAGR = (ending / begin) ** (1 / year) - 1 
        print("CAGR = %", CAGR * 100)

    elif choice == "4":
        print("You selected Loan EMI")
        principle = float(input("Principal amount: "))
        annual_rate = float(input("Annual rate of interest (%): ")) / 100
        months = int(input("Loan tenure (months): "))
        monthly_rate = annual_rate / 12 
        emi = principle * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1) 
        total_payment = months * emi
        total_interest = total_payment - principle 
        print("Total payment:", total_payment)
        print("Total interest:", total_interest)

    elif choice == "5":
        print("You selected Tax Calculator")

        income = float(input("Annual income: "))
        tax = 0

        if income <= 250000:
            tax = 0

        elif income <= 500000:
            tax = (income - 250000) * 0.05

        elif income <= 1000000:
            tax = (250000 * 0.05) + (income - 500000) * 0.20

        else:
            tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

        print("Total tax =", tax)
        print("Net income after tax =", income - tax)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")



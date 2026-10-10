def track():

    p = {"AAPL": 180, "TSLA": 250, "MSFT": 350, "GOOG": 140}
    
    t = 0 
    s = {} 

    while True:
        n = input("Enter stock (AAPL, TSLA, MSFT, GOOG) or 'q' to quit: ").upper()
        
        if n == 'Q':
            break
            
        if n not in p:
            print("Invalid stock.")
            continue
            
        try:
            q = int(input("Enter quantity: "))
        except ValueError:
            print("Must be an integer.")
            continue
            
        t += p[n] * q
        s[n] = s.get(n, 0) + q

    print(f"\nTotal Investment: ${t}")

    with open("portfolio.txt", "w") as f:
        f.write(f"Total Investment: ${t}\n")
        f.write("Holdings:\n")
        for k, v in s.items():
            f.write(f"{k}: {v} shares\n")
            
    print("Data saved to portfolio.txt")

track()

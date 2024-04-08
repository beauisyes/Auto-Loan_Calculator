import tkinter as tk

# CarLoanCalculator class holds the GUI for user inputs of the car loan
class CarLoanCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Car Loan Plan Calculator")
        self.master.geometry("500x500")

        # Prompts the user for the cost of the car
        self.total_amount_label = tk.Label(self.master, text="How much is the car in $: ")
        self.total_amount_label.pack(padx=5,pady=5)
        self.total_amount = tk.Entry(self.master)
        self.total_amount.pack(padx=5,pady=5)

        # Prompts the user for the interest rate of the car
        self.interest_rate_label = tk.Label(self.master, text="What is the interest rate in decimal form? ")
        self.interest_rate_label.pack(padx=5,pady=5)
        self.interest_rate = tk.Entry(self.master)
        self.interest_rate.pack(padx=5,pady=5)

        # Prompts the user for the length of the loan
        self.loan_term_label = tk.Label(self.master, text="How long is the loan in years? ")
        self.loan_term_label.pack(padx=5,pady=5)
        self.loan_term = tk.Entry(self.master)
        self.loan_term.pack(padx=5,pady=5)

        # Prompts the user for the down payment of the loan
        self.down_payment_label = tk.Label(self.master, text="How much is your down payment?")
        self.down_payment_label.pack(padx=5,pady=5)
        self.down_payment = tk.Entry(self.master)
        self.down_payment.pack(padx=5,pady=5)

        # Prompts the user for the value of a trade in
        self.trade_in_amount_label = tk.Label(self.master, text="How much is your trade in?")
        self.trade_in_amount_label.pack(padx=5,pady=5)
        self.trade_in_amount = tk.Entry(self.master)
        self.trade_in_amount.pack(padx=5,pady=5)

        # Constructs the button to calculate the monthly payment of the loan
        self.button = tk.Button(self.master, text="Open results", command=self.open_results)
        self.button.pack()
        
    # Function that opens the Results GUI
    def open_results(self):
        # The function uses try incase the user doesn't provide valid inputs, and if the user provides an invalid input, the program prints a message letting the user know
        try:
            #The variables serve as conversions from the inputs in the GUI
            total_amount = int(self.total_amount.get())
            interest_rate = float(self.interest_rate.get())
            loan_term = int(self.loan_term.get())
            down_payment = int(self.down_payment.get())
            trade_in_amount = int(self.trade_in_amount.get())
            self.new_window = tk.Toplevel(self.master)

            #Calls upon the results class opening the second GUI
            results = Results(self.new_window, total_amount, interest_rate, loan_term, down_payment, trade_in_amount)
        except:
            # Tells the user 
            print("Could not open the results, most likely caused by an invalid input")
        
# Results class calculates the monthly payment plan of the loan and displays it to the GUI
class Results:
    def __init__(self, master, total_amount, interest_rate, loan_term, down_payment, trade_in_amount):
        self.master = master
        self.master.title("Results")
        self.master.geometry("400x400")

        # Calculates the monthly payment of the loan
        total_amount = total_amount - (down_payment + trade_in_amount)
        numerator = total_amount * (interest_rate/12)
        denominator = 1-(1+(interest_rate/12))**(-1*loan_term * 12)
        mp = round(numerator/denominator, 2)

        # Displays the monthly payment of the loan
        self.title_results = tk.Label(self.master, text="Your monthly payment is")
        self.title_results.pack(padx=5,pady=5)

        self.results_label = tk.Label(self.master, text="$" + str(mp), font=('Arial', 20))
        self.results_label.pack()


        self.button = tk.Button(self.master, text="Close", command=self.close_window)
        self.button.pack()
    
    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = CarLoanCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
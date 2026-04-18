import math
import tkinter as tk


#Define the function to calculate a prime number
def Prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

#Define the function to check if the input is a prime number and update the result label
def check_prime():
    user_input = entry.get()

#Check if the user wants to close the application
    if user_input == "close":
        root.destroy()
        return
    try:
        number = int(user_input)
        if Prime(number):
            result_label.config(text=f"{number} is a Prime numeral ✓")

        else:
            result_label.config(text=f"{number} is not a Prime numeral x")
    
#Handle the case where the user input is not a valid integer
    except ValueError:
        result_label.config(text="Please enter a valid integer or 'close' to exit.")                

#Gui window
root = tk.Tk()
root.title("Prime Number Scanner")
root.geometry("400x300")

entry = tk.Entry(root)
entry.pack(pady=20)

tk.Button(root, text="Check", command=check_prime).pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

tk.Label(root, text="By Sabah").pack(side="bottom")

#Run the GUI
root.mainloop() 
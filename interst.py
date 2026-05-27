from tkinter import *
from tkinter import messagebox

def calc():
    try:
        p = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())

        # Simple Interest
        si = (p * r * t) / 100

        # Compound Interest
        ci = p * (pow((1 + r / 100), t)) - p

        # Display Results
        label_si_result.config(text=f"Simple Interest: {round(si,2)}")
        label_ci_result.config(text=f"Compound Interest: {round(ci,2)}")

        # Message Box
        messagebox.showinfo(
            "Result",
            f"Simple Interest = {round(si,2)}\nCompound Interest = {round(ci,2)}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid input")


# Main Window
window = Tk()
window.title("Interest Calculator App")
window.geometry("400x400")

# Principal Amount
lbl = Label(window, text="Principal Amount")
lbl.pack()

entry_principal = Entry(window)
entry_principal.pack()

# Time Period
lbl2 = Label(window, text="Time Period / Years")
lbl2.pack()

entry_time = Entry(window)
entry_time.pack()

# Rate of Interest
lbl3 = Label(window, text="Rate of Interest")
lbl3.pack()

entry_rate = Entry(window)
entry_rate.pack()

# Calculate Button
btn = Button(window, text="Calculate", command=calc)
btn.pack(pady=20)

# Result Labels
label_si_result = Label(window, text="")
label_si_result.pack()

label_ci_result = Label(window, text="")
label_ci_result.pack()

# Run Window
window.mainloop()
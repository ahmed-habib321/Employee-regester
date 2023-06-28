from tkinter import *
from tkinter import messagebox

def create_employee_file():
    if code_entry.get().strip() != "" and name_entry.get().strip() != "" and address_entry.get().strip() != "":
        try:
            file = open(name_entry.get() + ".txt", "a")
            file.write("\n")
            file.write("\\\\\\Employee File////\n")
            file.write("\n")
            file.write("Employee Name: " + name_entry.get() + "\n")
            file.write("Employee Code: " + code_entry.get() + "\n")
            file.write("Employee Address: " + address_entry.get() + "\n")
            file.close()

            messagebox.showinfo("Done", "Employee File has been created")
        except Exception as ex:
            messagebox.showwarning("Warning", str(ex))
    else:
        if code_entry.get().strip() == "":
            messagebox.showwarning("Warning", "Code is empty")
            code_entry.focus()
        elif name_entry.get().strip() == "":
            messagebox.showwarning("Warning", "Name is empty")
            name_entry.focus()
        elif address_entry.get().strip() == "":
            messagebox.showwarning("Warning", "Address is empty")
            address_entry.focus()

root = Tk()
root.title("Employee File Data")
root.geometry("500x400")
root.resizable(False, False)
root.config(background="#a5f6f0")

frame = Frame(root, bg="#a5f6f0")
frame.pack(pady=10)

Label(frame, text="Employee Data", bg="navy", fg="light blue", font=("None", 30, "bold")).grid(row=0, columnspan=2)

Label(frame, text="Code:", bg="#a5f6f0", font=("None", 20, "bold")).grid(row=1, column=0, pady=10, sticky=E)
Label(frame, text="Name:", bg="#a5f6f0", font=("None", 20, "bold")).grid(row=2, column=0, pady=10, sticky=E)
Label(frame, text="Address:", bg="#a5f6f0", font=("None", 20, "bold")).grid(row=3, column=0, pady=10, sticky=E)

code_entry = Entry(frame, font=("None", 20), textvariable=StringVar())
code_entry.grid(row=1, column=1, pady=10)

name_entry = Entry(frame, font=("None", 20), textvariable=StringVar())
name_entry.grid(row=2, column=1, pady=10)

address_entry = Entry(frame, font=("None", 20), textvariable=StringVar())
address_entry.grid(row=3, column=1, pady=10)

Button(root, text="Create Employee Text File", font=("None", 20, "bold"), command=create_employee_file).pack(pady=10)
Button(root, text="Exit", fg="red", font=("None", 20, "bold"), command=root.destroy).pack(pady=10, padx=10, anchor=W)

root.mainloop()

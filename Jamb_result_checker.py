# jamb_result_checker_pro.py - CaptinBadass All-In-One
import csv
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

# Mock JAMB database
students_db = {
    "2025UTME12345": {"name": "Captin Badass", "ENG": 78, "MTH": 85, "PHY": 72, "CHEM": 80},
    "2025UTME67890": {"name": "Alfred Assistant", "ENG": 90, "MTH": 88, "PHY": 91, "CHEM": 85},
}

def check_result():
    reg = entry_reg.get().strip().upper()
    if not reg:
        messagebox.showerror("Error", "Enter Reg Number!")
        return

    if reg in students_db:
        data = students_db[reg]
        total = sum([data["ENG"], data["MTH"], data["PHY"], data["CHEM"]])

        result_text = f"""
Name: {data['name']}
Reg No: {reg}
Date: {datetime.now().strftime('%d-%m-%Y')}

English: {data['ENG']}
Maths: {data['MTH']}
Physics: {data['PHY']}
Chemistry: {data['CHEM']}

TOTAL: {total}/400
Status: {'QUALIFIED 🎉' if total >= 200 else 'BELOW CUTOFF'}
"""
        result_label.config(text=result_text)

        # Enable save button
        global current_result
        current_result = (reg, data, total)
    else:
        messagebox.showerror("Not Found", f"No result for {reg}")

def save_to_file():
    try:
        reg, data, total = current_result
        filename = f"{reg}_result.txt"
        with open(filename, "w") as f:
            f.write(result_label.cget("text"))
        messagebox.showinfo("Saved", f"Result saved as {filename}")

        # Save to CSV too
        with open("jamb_results.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([reg, data['name'], data['ENG'], data['MTH'], data['PHY'], data['CHEM'], total])

    except:
        messagebox.showerror("Error", "Check result first!")

def load_csv():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file:
        messagebox.showinfo("Loaded", f"Loaded {file} - {len(students_db)} records ready!")

# GUI Setup
root = tk.Tk()
root.title("JAMB Result Checker - CaptinBadass")
root.geometry("450x500")
root.config(bg="#0A1931")

tk.Label(root, text="JAMB RESULT CHECKER 2025", font=("Arial", 16, "bold"), bg="#0A1931", fg="white").pack(pady=15)

tk.Label(root, text="Reg Number:", bg="#0A1931", fg="white").pack()
entry_reg = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
entry_reg.pack(pady=5)

tk.Button(root, text="CHECK RESULT", command=check_result, bg="#185ADB", fg="white", font=("Arial", 11, "bold"), width=20).pack(pady=10)

result_label = tk.Label(root, text="Enter Reg Number to check...", bg="white", fg="black", font=("Courier", 10), justify="left", width=50, height=12, relief="raised")
result_label.pack(pady=10, padx=20)

frame = tk.Frame(root, bg="#0A1931")
frame.pack(pady=5)
tk.Button(frame, text="Save Result", command=save_to_file, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame, text="Load CSV", command=load_csv, bg="#FF9800", fg="white").grid(row=0, column=1, padx=5)

current_result = None
root.mainloop()

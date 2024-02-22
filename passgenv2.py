import tkinter as tk
import random


#Shuffle Password Command
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

password = ''

#Generate Password Command
def genpass():
    lbl_result.delete("1.0","end")
    password = ''
    uppercaseLetter=chr(random.randint(65,90))
    lowercaseLetter=chr(random.randint(97,122))
    number=chr(random.randint(48,57))

    length = int(ent_temperature.get())

    password = ''
 
    for i in range(length):
        choice = random.randint(0,2)
        if choice == 0:
            uppercaseLetter=chr(random.randint(65,90))
            password = password+uppercaseLetter
       
        if choice == 1:
            lowercaseLetter=chr(random.randint(97,122))
            password = password+lowercaseLetter
       
        if choice == 2:
            number=chr(random.randint(48,57))
            password = password+number

    password = shuffle(password)
    lbl_result.insert(1.0,password) 



window = tk.Tk()
window.title("Passgen v2.0")
window.resizable(width=False, height=False)
window['bg'] = "green"

#Creating elements
frm_entry = tk.Frame(master=window)
frm_entry2 = tk.Frame(master=window,width=200, height=20)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="Length:")
lbl_result = tk.Text(master=frm_entry2)

#Placing elements on screen
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

#Button to generate password
btn_convert = tk.Button(
    master=window,
    text="Generate",
    command=genpass
)




#Placing elements on screen
frm_entry.grid(row=0, column=0, padx=10)
frm_entry2.grid(row=0, column=2, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)




#Running the application
window.mainloop()
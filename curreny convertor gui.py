from tkinter import *
import requests
import json
import tkinter.messagebox
cs=ia = 0
incs = 0
url = "https://api.exchangeratesapi.io/latest"
amount = 0
end = ""

fields = ('Enter the amount','From Currency', 'To Currency')



def conversions(entries):
    end = ""
    while end !="quit":
        r = requests.get(url)
        if (r.status_code!=200):
            end = input("Sorry! REfresh or press enter")
        else:
            ans_no = 1
            data = json.loads(r.text)
            #pprint.pprint(data)
            amount = float(entries['Enter the amount'].get())
            currency = entries['From Currency'].get().upper()
            conversion = entries['To Currency'].get().upper()
            if currency == 'EUR':
                question = data['rates'][conversion]
                tkinter.messagebox.showinfo("Converted Values",'{} {} = {} {}'.format(amount, currency, amount*float(question), conversion))
            else:
                if currency != 'EUR' :
                    ia= amount
                    amount = amount / data['rates'][currency]
                    # limiting the precision to 2 decimal places
                    amount = round(amount * data['rates'][conversion], 2)
                    print('{} {} = {} {}'.format(ia, currency, amount, conversion)) 
                    tkinter.messagebox.showinfo("Converted Values",'{} {} = {} {}'.format(ia, currency, amount, conversion))
            end="quit"


def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      if field=="Enter the amount":
          ent.insert(0,"0")
      else:
          ent.insert(0,"USD")      
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    b1 = Button(root, text='Ok',
           command=(lambda e=ents: conversions(e)))
    b1.pack(side=LEFT, padx=15, pady=15)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=RIGHT, padx=15, pady=15)
    root.mainloop()

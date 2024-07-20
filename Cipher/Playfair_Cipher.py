from tkinter import * 

import string

root = Tk()
root.title("Playfair Cipher")
root.geometry("500x630")
lblMessage = Label(root,text="Message: ", font=("Arial",12))
lblMessage.place( x=30, y=30) 
txtMessage = Entry(root,width=50)
txtMessage.place(x=120, y=30)
lblKey = Label(root, text="Key: ", font=("Arial",12))
lblKey.place(x=30, y=60)
txtKey = Entry(root, width=30)
txtKey.place(x=120, y=60)

box = Text(root, width=9, height=5, font=("ROBOTO",34))
box.place(x=135, y=100)
 
def isCheck(value):
    if value == 1:
        btnClick['text'] ='Encrypy'
    elif value == 2:
         btnClick['text'] ='Decrypy'    
    return value

radio_frame=Frame(root).pack(side=BOTTOM)
var = IntVar()
var.set("1")
rdEncrypy = Radiobutton(radio_frame, text="Encrypy", variable=var, value=1, command=lambda: isCheck(var.get()))
rdEncrypy.place(x=180, y=380)
rdDecrypy = Radiobutton(radio_frame, text="Decrypy", variable=var, value=2, command=lambda: isCheck(var.get()))
rdDecrypy.place(x=260, y=380)

lblPlaintext = Label(root, text="Plaintext", font=("Arila",12))
lblPlaintext.place(x=30, y=520)
txtPlaintext = Entry(root, width=50)
txtPlaintext.place(x=120, y=520)

lblResult = Label(root, text="Result: ", font=("Arila",12))
lblResult.place(x=30, y=550)
txtResult = Entry(root, width=50)
txtResult.place(x=120, y=550)

def setKey(key):
    atoz = string.ascii_lowercase.replace("j",".")
    atoz = atoz.upper()
    key_maxtrix = ['' for i in range(5)]
    i=0
    j=0
    for c in key:
        if c in atoz:
            key_maxtrix[i] += c
            atoz = atoz.replace(c,".")
            j+=1
            if j > 4:
                i+=1
                j=0

    for c in atoz:
        if c != ".":
            key_maxtrix[i] += c
            j+=1
            if j > 4 :
                i+=1
                j=0
    return key_maxtrix

def setMessage(plaintext):
    plaintext = plaintext.replace(" ","")
    temp = []
    plaintextpairs = []
    i = 0
    if var.get() == 1:
        while i < len(plaintext):
            a = plaintext[i]
            b = ""
            if (i+1) == len(plaintext):
                b=""
            else:
                b = plaintext[i+1] 

            if a != b:
                temp.append(a)
                i+=1
            else:
                temp.append(a)
                temp.append("X")
                i+=1
        j=0
        while j < len(temp):
            s = temp[j]
            c = ""
            if (j+1) == len(temp):
                c=""
            else:
                c = temp[j+1] 
            if a != b:
                plaintextpairs.append(s+c)
                j+=2
    elif var.get() == 2:
        while i < len(plaintext):
            a = plaintext[i]
            b = ""
            if (i+1) == len(plaintext):
                b=""
            else:
                b = plaintext[i+1] 
            plaintextpairs.append(a + b)
            i+=2  
    return plaintextpairs

def encrypt(plaintext, key):   
    key_maxtrix = setKey(key)
    plaintextpairs = setMessage(plaintext)
    ciphertextpairs = []
    for pair in plaintextpairs:
        if len(pair) == 2:
            applied_rule = False
            for row in key_maxtrix:
                if pair[0] in row and pair[1] in row:
                    j0 = row.find(pair[0])
                    j1 = row.find(pair[1])

                    ciphertextpair = row[(j0+1)%5]+ row[(j1+1)%5]
                    ciphertextpairs.append(ciphertextpair)
                    applied_rule = True

            if applied_rule: 
                continue

            for j in range(5):
                col = "".join([key_maxtrix[i][j] for i in range(5)])
                if pair[0] in col and pair[1] in col:
                    i0 = col.find(pair[0])
                    i1 = col.find(pair[1])

                    ciphertextpair = col[(i0+1)%5]+ col[(i1+1)%5]
                    ciphertextpairs.append(ciphertextpair)
                    applied_rule = True

            if applied_rule: 
                continue      
            i0=0
            i1=0
            j0=0
            j1=0
            for i in range(5):
                row = key_maxtrix[i]
                if pair[0] in row:
                    i0 = i 
                    j0 = row.find(pair[0])
                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])
            ciphertextpair = key_maxtrix[i0][j1] + key_maxtrix[i1][j0]
            ciphertextpairs.append(ciphertextpair)    
        elif len(pair) < 2:
            for row in key_maxtrix:
                if pair[0] in row :
                    j0 = row.find(pair[0])

                    ciphertextpair = row[(j0+1)%5]
                    ciphertextpairs.append(ciphertextpair)
                    applied_rule = True

            if applied_rule: 
                continue

    box.delete(1.0,END)
    txtPlaintext.delete(0,END)  
    txtResult.delete(0,END)

    for k in key_maxtrix:
        for c in k:
            if c != "I":
                box.insert(END, c + " ")
            elif c == "I":
                box.insert(END, " " + c + "  ")

    for p in plaintextpairs:
        txtPlaintext.insert(END, p + " ")

    for c in ciphertextpairs:
        txtResult.insert(END, c + " ")
    return

def decrypy(plaintext, key):
    key_maxtrix = setKey(key)
    plaintextpairs = setMessage(plaintext)
    ciphertextpairs = []
    for pair in plaintextpairs:
        if len(pair) == 2:
            applied_rule = False
            for row in key_maxtrix:
                if pair[0] in row and pair[1] in row:
                    j0 = row.find(pair[0])
                    j1 = row.find(pair[1])

                    ciphertextpair = row[(j0+4)%5]+ row[(j1+4)%5]
                    ciphertextpairs.append(ciphertextpair)
                    applied_rule = True

            if applied_rule: 
                continue

            for j in range(5):
                col = "".join([key_maxtrix[i][j] for i in range(5)])
                if pair[0] in col and pair[1] in col:
                    i0 = col.find(pair[0])
                    i1 = col.find(pair[1])

                    ciphertextpair = col[(i0+4)%5]+ col[(i1+4)%5]
                    ciphertextpairs.append(ciphertextpair)
                    applied_rule = True

            if applied_rule: 
                continue      
            i0=0
            i1=0
            j0=0
            j1=0
            for i in range(5):
                row = key_maxtrix[i]
                if pair[0] in row:
                    i0 = i 
                    j0 = row.find(pair[0])
                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])
            ciphertextpair = key_maxtrix[i0][j1] + key_maxtrix[i1][j0]
            ciphertextpairs.append(ciphertextpair)    
        elif len(pair) < 2:
            for row in key_maxtrix:
                if pair[0] in row :
                    j0 = row.find(pair[0])

                    ciphertextpair = row[(j0+4)%5]
                    ciphertextpairs.append(ciphertextpair)
                    applied_rule = True

            if applied_rule: 
                continue
    temps =[]
    temp = []
    k=0  
    j =0      
    for c in ciphertextpairs:
        if len(c) ==2:
            temp.append(c[0])
            temp.append(c[1])
        elif len(c) < 2:
            temp.append(c[0])

    while k < len(temp):
        a = temp[k]
        if (k+1) == len(temp): 
            b = ""
            c = ""
        elif(k+2) == len(temp):
            b = temp[k+1]
            c = ""
        else:
            b= temp[k+1]
            c= temp[k+2]    
        if a != b and a == c:
            temps.append(a+c)
            k+=3
        else:
            temps.append(a+b)
            k+=2  

    box.delete(1.0,END)
    txtPlaintext.delete(0,END)  
    txtResult.delete(0,END)

    for k in key_maxtrix:
        for c in k:
            if c != "I":
                box.insert(END, c + " ")
            elif c == "I":
                box.insert(END, " " + c + "  ")

    for p in plaintextpairs:
        txtPlaintext.insert(END, p + " ")

    for c in temps:
        txtResult.insert(END, c + " ")
    return        


def clickBtn():
    plaintext = txtMessage.get().upper()
    key = txtKey.get().upper()
    if var.get() == 1:
        encrypt(plaintext,key)
    elif var.get() == 2:
        decrypy(plaintext,key)

if __name__ == "__main__":
    btnClick = Button(root, text="Encrypt",width=10 ,font=("Arial",12), command= clickBtn) 
    btnClick.place(x=200, y=420) 
    root.mainloop()



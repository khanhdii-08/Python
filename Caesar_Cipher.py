from tkinter import * 


root = Tk()
root.title("Caesar Cipher")
root.geometry("450x250")

lblMessage = Label(root, text="Message: ", font=("Arial",14))
lblMessage.place(x=20, y=10)

txtMessage = Entry(root, width=50)
txtMessage.place(x=130, y=10)

lblKey = Label(root, text="Key: ", font=("Arial",14))
lblKey.place(x=20, y=40)

txtKey = Spinbox(root, from_=0, to=100, width=5)
txtKey.place(x=130, y=40)

lblAction = Label(root,text="Action: ", font=("Arial",14))
lblAction.place(x=20, y=70)

def isCheck(value):
    if value == 1:
        btnClick['text'] ='Encrypy Message'
    elif value == 2:
         btnClick['text'] ='Decrypy Message'    
    return value

radio_frame=Frame(root).pack(side=BOTTOM)
var = IntVar()
var.set("1")
rdEncrypy = Radiobutton(radio_frame, text="Encrypy", variable=var, value=1, command=lambda: isCheck(var.get()))
rdEncrypy.place(x=130, y=70)
rdDecrypy = Radiobutton(radio_frame, text="Decrypy", variable=var, value=2, command=lambda: isCheck(var.get()))
rdDecrypy.place(x=210, y=70)


lblResult = Label(root, text="Result: ", font=("Arial",14))
lblResult.place(x=20, y=100)

txtResult = Entry(root, width=50)
txtResult.place(x=130, y=100)

def encrypt(plaintext, key):
    ciphertext=""
    for char in plaintext:
        if(char.isupper()):
            if char != " ":
                i = ord(char) - 65
                i = ( i + key ) % 26
                ciphertext  = ciphertext + chr(i+65)
            else :
                ciphertext  = ciphertext + char
        else:
            if char != " ":
                i = ord(char) - 97
                i = ( i + key ) % 26
                ciphertext  = ciphertext + chr(i+97)
            else :
                ciphertext  = ciphertext + char

    txtResult.delete(0,END)  
    txtResult.insert(END,ciphertext)            
    return

def decrypy(plaintext, key):
    ciphertext=""
    for char in plaintext:
        if(char.isupper()):
            if char != " ":
                i = ord(char) - 65 
                i = (i - key ) % 26
                ciphertext = ciphertext + chr(i+65)
            else:
                ciphertext = ciphertext + char
        else:
            if char != " ":
                i = ord(char) - 97
                i = (i - key) % 26
                ciphertext = ciphertext + chr(i+97)
            else:
                ciphertext = ciphertext + char

    txtResult.delete(0,END)  
    txtResult.insert(END,ciphertext)            
    return           

def check(plaintext, key):
    if var.get() == 1:
        encrypt(plaintext, key)
    elif var.get() == 2:
        decrypy(plaintext, key)


btnClick = Button(root, text="Encrypy Message" ,command=lambda: check(txtMessage.get(),int(txtKey.get())) )
btnClick.place(x=130, y=130)
root.mainloop()


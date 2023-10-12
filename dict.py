from tkinter import*
from PyDictionary import PyDictionary
from tkinter import messagebox

dict=PyDictionary()
def search():
		input=input_n1.get()
		mean=dict.meaning(input)
		if mean:
			output.delete(1.0, END)
			output.insert(END, mean['Noun'][0])
			#output.config(state= "disabled")
		else:
			messagebox.showerror("showerror", "Word not found ")
			#output.insert(END,"invalid text")
def clear():
	input_n1.delete(0, END)
	output.delete("1.0","end")
def exit():
	root.quit()
root=Tk()
root.title("dictionary")
root.geometry("900x507+200+100")  
root.resizable(False,False)

bg = PhotoImage(file = "C:/Users/hp/OneDrive/Desktop/dict/panda.png")

canvas1 = Canvas( root)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

canvas1.create_text( 320, 50, text = "My Dictionary",font=("Arial 30 bold"),fill='white')

canvas1.create_text( 245, 130, text = "Search",font=("Arial 20 bold"))
input_n1=Entry(root,font=("Arial 15"))
input_n1.place(x=200,y=150)

canvas1.create_text( 252, 230, text = "Meaning",font=("Arial 20 bold"))
output = Text(root, height = 5,width = 28,font=("Arial 16 bold"))
output.place(x=200,y=250)

button1 = Button( root, text = "Search",bd = '8',command=search)
button2 = Button( root, text = "Clear",bd = '8',command=clear)
button3 = Button( root, text = "Exit",bd = '8',command=exit)
button1_canvas = canvas1.create_window( 200, 400, anchor = "nw",window = button1)
button2_canvas = canvas1.create_window( 300, 400,anchor = "nw",window = button2)
button3_canvas = canvas1.create_window( 390, 400,anchor = "nw",window = button3)
  

root.mainloop()

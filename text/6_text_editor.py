# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkinter import Menu
import ScrolledText as st

def main():
	root = tk.Tk(className="My First Python Editor")
	textPad = st.ScrolledText(root, width=100, height=30)
	textPad.pack()

	menu = Menu(root)
	root.config(menu=menu)
	fileMenu = Menu(menu)

	menu.add_cascade(label="File", menu=fileMenu)

	root.mainloop()	

def dummy():
	print "I am just a dummy command!"

if __name__ == "__main__":
	main()
#!/usr/bin/env python

__author__ = "Saulius Bartkus"
__copyright__ = "Copyright 2017"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Saulius Bartkus"
__email__ = "saulius181@yahoo.com"
__status__ = "Production"


import tkinter as tk
from PIL import Image, ImageTk

class Game(tk.Frame):
	
	def load_images(self):
		self.rock1 = Image.open("rock1.png")
		self.rock2 = Image.open("rock2.png")
		self.tk_rock1 = ImageTk.PhotoImage(self.rock1)
		self.tk_rock2 = ImageTk.PhotoImage(self.rock2)
		
		self.scissors1 = Image.open("scissors1.png")
		self.scissors2 = Image.open("scissors2.png")
		self.tk_scissors1 = ImageTk.PhotoImage(self.scissors1)
		self.tk_scissors2 = ImageTk.PhotoImage(self.scissors2)
		
		self.paper1 = Image.open("paper1.png")
		self.paper2 = Image.open("paper2.png")
		self.tk_paper1 = ImageTk.PhotoImage(self.paper1)
		self.tk_paper2 = ImageTk.PhotoImage(self.paper2)
		
		
		self.canvas_scissors_back = self.canvas.create_rectangle(31, 171, 169, 309, fill="#000055", dash=200, width=5, stipple='gray25', state=tk.HIDDEN)
		self.canvas_scissors1 = self.canvas.create_image(100, 240, image=self.tk_scissors1, tag="Scissors")
		
		self.canvas_rock_back = self.canvas.create_rectangle(206, 171, 344, 309, fill="#000055", dash=200, width=5, stipple='gray25', state=tk.HIDDEN)
		self.canvas_rock1 = self.canvas.create_image(275, 240, image=self.tk_rock1, tag="Rock")
		
		self.canvas_paper_back = self.canvas.create_rectangle(381, 171, 519, 309, fill="#000055", dash=200, width=5, stipple='gray25', state=tk.HIDDEN)
		self.canvas_paper1 = self.canvas.create_image(450, 240, image=self.tk_paper1, tag="Paper")
		
	def bind_images(self):
		self.canvas.tag_bind(self.canvas_scissors1, "<Enter>", self.on_enter)
		self.canvas.tag_bind(self.canvas_scissors1, "<Leave>", self.on_leave)
		self.canvas.tag_bind(self.canvas_rock1, "<Enter>", self.on_enter)
		self.canvas.tag_bind(self.canvas_rock1, "<Leave>", self.on_leave)
		self.canvas.tag_bind(self.canvas_paper1, "<Enter>", self.on_enter)
		self.canvas.tag_bind(self.canvas_paper1, "<Leave>", self.on_leave)		

		self.canvas.tag_bind(self.canvas_scissors1, "<Button-1>", self.on_click)
		self.canvas.tag_bind(self.canvas_rock1, "<Button-1>", self.on_click)
		self.canvas.tag_bind(self.canvas_paper1, "<Button-1>", self.on_click)
		
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
		self.canvas = tk.Canvas(root, width=565, height=310)
		self.canvas.pack()
		
		self.load_images()
		self.bind_images()
		
		self.l1 = tk.Label(self, text="Select your hand")
		self.l2 = tk.Label(self, text="", width=40)
		self.l1.pack(side="top")
		self.l2.pack(side="top", fill="x")
	
	def on_click(self, event):
		print("sadsakdsak")
	
	def on_enter(self, event):
		self.currentID = self.canvas.find_withtag(tk.CURRENT)[0]
		self.l2.configure(text="Pick {}".format(self.canvas.gettags(self.currentID)[0]))
		self.canvas.itemconfigure(self.currentID-1, state=tk.NORMAL)
		
		
	def on_leave(self, enter):
		self.l2.configure(text="")
		self.canvas.itemconfigure(self.currentID-1, state=tk.HIDDEN)
		
if __name__ == "__main__":
	root = tk.Tk()
	Game(root).pack(side="top", fill="both", expand="true")
	root.mainloop()
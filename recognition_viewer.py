import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, VERTICAL, HORIZONTAL, N, S, E, W

class RecognitionViewer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._text = ScrolledText(self, wrap="word")
        self._text.pack(side="top", fill="both", expand=True)

# viewer = RecognitionViewer()
# viewer.mainloop()
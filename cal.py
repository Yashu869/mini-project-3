import tkinter as tkclass Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")  # Entry widget to display input and results
        self.entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)  # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
            ]  # Initialize buttons and set their callbacks
        row_val, col_val = 1, 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1  def on_button_click(self, button):
                    current_entry = self.entry.get()  if button == '=':
                        try:
                            result = eval(current_entry)
                            self.entry.delete(0, tk.END)
                            self.entry.insert(tk.END, str(result))
                            except Exception as e:
                                self.entry.delete(0, tk.END)
                                self.entry.insert(tk.END, "Error")  else:
                                    self.entry.insert(tk.END, button)  if __name__ == "__main__":
                                        root = tk.Tk()
                                        calculator = Calculator(root)
                                        root.mainloop()

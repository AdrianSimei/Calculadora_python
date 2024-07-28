import tkinter as tk
from config import constantes as cons
import utils.util_ventana as util_ventana
from tkinter import font

class FormularioCalculadora(tk.Tk):
  
    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widget()
  
    def config_window(self):
        self.title('Calculadora con tkinter')
        self.configure(bg=cons.COLOR_BOTONES_LIGHT)
        self.attributes('-alpha', 0.96)
        self.minsize(300, 400)
        util_ventana.centrar_ventana(self, 470, 570)

    def construir_widget(self):
        self.operation_label = tk.Label(self, text="", font=(
            'Arial', 16), fg=cons.COLOR_BOTONES_LIGHT, bg=cons.COLOR_DE_FONDO_LIGHT, justify='right')
        self.operation_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
    
        self.entry = tk.Entry(self, width=12, font=(
            'Arial', 40), bd=0, fg=cons.COLOR_DE_TEXTO_LIGHT, bg=cons.COLOR_CAJA_TEXTO_LIGHT, justify='right')
        self.entry.grid(row=1, column=0, columnspan=4, 
                        padx=10, pady=10, sticky="nsew")
        
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]
        roboto_font = font.Font(family="Roboto", size=16)

        for i, button in enumerate(buttons):
            row_val = i // 4 + 2
            col_val = i % 4
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.COLOR_BOTONES_ESPECIALES_LIGHT
                button_font = font.Font(size=16, weight='bold')
            else:
                color_fondo = cons.COLOR_BOTONES_LIGHT
                button_font = roboto_font
            
            btn = tk.Button(self, text=button, command=lambda b=button: self.on_button_click(b),
                            bg=color_fondo, fg=cons.COLOR_DE_TEXTO_LIGHT, relief=tk.FLAT, font=button_font)
            btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
        
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == 'C':
            self.entry.delete(0, tk.END)
        elif button == '<':
            current_text = self.entry.get()
            self.entry.delete(len(current_text) - 1)
        elif button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)


if __name__ == "__main__":
    app = FormularioCalculadora()
    app.mainloop()

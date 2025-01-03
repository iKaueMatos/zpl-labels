import tkinter as tk
from tkinter import ttk, filedialog
from models.barcode_label_generator import BarcodeLabelGenerator

class LabelFormatView:
    def __init__(self, root):
        self.root = root
        self.generator = BarcodeLabelGenerator()
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Selecione o formato da etiqueta:")
        self.label.pack(pady=10)

        self.format_combobox = ttk.Combobox(self.root, values=[
            "2-Colunas", "1-Coluna", "4-etiquetas por página", 
            "Entiqueta Envio personalizado", "QRCode", "Code128"
        ])
        self.format_combobox.pack(pady=10)
        self.format_combobox.bind("<<ComboboxSelected>>", self.on_format_selected)
        self.format_combobox['state'] = 'readonly'  # Ensure all options are displayed

        self.generate_button = ttk.Button(self.root, text="Gerar ZPL", command=self.generate_zpl)
        self.generate_button.pack(pady=10)

    def on_format_selected(self, event):
        selected_format = self.format_combobox.get()
        self.generator.set_label_format(selected_format)

    def generate_zpl(self):
        zpl_code = self.generator.generate_zpl()
        self.save_zpl_to_file(zpl_code)

    def save_zpl_to_file(self, zpl_code):
        file_path = filedialog.asksaveasfilename(defaultextension=".zpl", filetypes=[("ZPL files", "*.zpl")])
        if file_path:
            self.generator.save_zpl_to_file(zpl_code, file_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerador de Etiquetas")
    app = LabelFormatView(root)
    root.mainloop()

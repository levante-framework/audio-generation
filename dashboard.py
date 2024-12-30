import customtkinter as ctk
from tkinter import ttk
import pandas as pd
from utilities import utilities as u
from playsound import playsound
import textwrap

import math
class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Levante Translation Dashboard")
        self.geometry("1000x600")

        # Top frame with labels
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(side="top", fill="x", padx=10, pady=10)

       # Configure the grid layout
        self.top_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # First row
        self.generatedEnglish = ctk.CTkLabel(self.top_frame, text="English Audio: ###")
        self.generatedEnglish.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.generatedSpanish = ctk.CTkLabel(self.top_frame, text="Spanish Audio: ###")
        self.generatedSpanish.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.generatedGerman = ctk.CTkLabel(self.top_frame, text="German Audio: ###")
        self.generatedGerman.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Second row
        self.errorsEnglish = ctk.CTkLabel(self.top_frame, text="English Errors: ###")
        self.errorsEnglish.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.errorsSpanish = ctk.CTkLabel(self.top_frame, text="Spanish Errors: ###")
        self.errorsSpanish.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.errorsGerman = ctk.CTkLabel(self.top_frame, text="German Errors: ###")
        self.errorsGerman.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        # Third row
        self.notaskEnglish = ctk.CTkLabel(self.top_frame, text="English No Task: ###")
        self.notaskEnglish.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.notaskSpanish = ctk.CTkLabel(self.top_frame, text="Spanish No Task: ###")
        self.notaskSpanish.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.notaskGerman = ctk.CTkLabel(self.top_frame, text="German No Task: ###")
        self.notaskGerman.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        
        # Tabbed frame
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)

        # Create tabs
        self.tabSpanish = self.tabview.add("Spanish")
        self.tabGerman = self.tabview.add("German")

        # Add scrollable frame to Tab 1
        self.spanishFrame = ctk.CTkScrollableFrame(self.tabSpanish)
        self.spanishFrame.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_table(self.spanishFrame)



    def create_table(self, parent):

        def on_tree_select(event):
            # Get the ID of the selected item
            selected_items = event.widget.selection()
    
            if selected_items:  # Check if any item is selected
                item = selected_items[0]  # Get the first selected item
        
             # Get the column ID (if needed)
                column = event.widget.identify_column(event.widget.winfo_pointerx() - event.widget.winfo_rootx())
        
                # Get the values of the selected item
                item_values = event.widget.item(item, "values")
        
                # Get the text of the selected item
                item_text = event.widget.item(item, "text")
        
#                print(f"Selected item: {item}")
#                print(f"Selected column: {column}")
#                print(f"Item text: {item_text}")
#                print(f"Item values: {item_values}")

                # play audio
                # should go by column name...
                playsound(item_values[4])

        # hard-wire for now:
        lang_code_spanish = 'es-CO'
        lang_code_german = 'de'
        # Create a treeview widget for the table
        columns = ("Item", "Task", "English", "Translated", "Audio")
        style = ttk.Style()
        style.configure("Treeview", rowheight=80, \
                        font=('TkDefaultFont', 16))

        self.tree = ttk.Treeview(parent, columns=columns, show="headings", style='Treeview')
        self.tree.bind("<<TreeviewSelect>>", on_tree_select)

        # Define column headings
        for col in columns:
            self.tree.heading(col, text=col)
            if col == 'Item' or col == 'Task' or col == 'Audio':
                self.tree.column(col, width=15)
            else:
                self.tree.column(col, width=200)

        ## Hack file name!
        ourData = pd.read_csv("c:/levante/audio-generation/item_bank_translations.csv")
        # Insert DataFrame rows into the Treeview
        for index, row in ourData.iterrows():
            base = "audio_files"

            if type(row['labels']) == type('str'):
                audio_file_name = u.audio_file_path(row['labels'], row['item_id'], base, lang_code_spanish)
                values = [row['item_id'], row['labels'], row['en'], row[lang_code_spanish], audio_file_name]

                # Hack for column numbers
                values[2] = u.wrap_text(values[2])
                values[3] = u.wrap_text(values[3])

                self.tree.insert("", "end", values=values)

                self.tree.pack(expand=True, fill="both")


if __name__ == "__main__":
    app = App()
    app.mainloop()


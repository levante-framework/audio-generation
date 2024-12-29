import customtkinter as ctk
from tkinter import ttk
import pandas as pd

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Levante Translation Dashboard")
        self.geometry("800x600")

        # Top frame with buttons
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(side="top", fill="x", padx=10, pady=10)


        # Tabbed frame
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)

        # Create tabs
        self.tab1 = self.tabview.add("Spanish")
        self.tab2 = self.tabview.add("German")

        # Add scrollable frame to Tab 1
        self.scrollable_frame = ctk.CTkScrollableFrame(self.tab1)
        self.scrollable_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Create a table in the scrollable frame
        self.create_table(self.scrollable_frame)

    def create_table(self, parent):
        # Create a treeview widget for the table
        columns = ("Item", "English", "Translated", "Audio")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings")

        # Define column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        # Add sample data
#        data = [
#            ("John Doe", "30", "New York"),
#        ]

        ## Hack file name!
        ourData = pd.read_csv("c:/levante/audio-generation/item_bank_translations.csv")
        # Insert DataFrame rows into the Treeview
        for index, row in ourData.iterrows():
            self.tree.insert("", "end", values=list(row))

            self.tree.pack(expand=True, fill="both")

    def button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = App()
    app.mainloop()

# Spare stuff
"""
        self.button1 = ctk.CTkButton(self.top_frame, text="Button 1", command=self.button_click)
        self.button1.pack(side="left", padx=5)

        self.button2 = ctk.CTkButton(self.top_frame, text="Button 2", command=self.button_click)
        self.button2.pack(side="left", padx=5)

        self.button3 = ctk.CTkButton(self.top_frame, text="Button 3", command=self.button_click)
        self.button3.pack(side="left", padx=5)
"""

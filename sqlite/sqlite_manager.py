import os
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables

    def get_table_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        columns = [desc[0] for desc in self.cursor.description]
        data = [columns] + self.cursor.fetchall()
        return data
    
    def get_table_columns(self, table_name) :        
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        columns = self.cursor.fetchall()
        return columns

    def delete_data(self, table_name, row_id):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE rowid = ?;", (row_id,))
        self.conn.commit()

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Manager")

        # Select Database Frame
        self.select_db_frame = ttk.Frame(self.root, padding="10")
        self.select_db_frame.grid(row=0, column=0, sticky="nsew")

        self.db_label = ttk.Label(self.select_db_frame, text="Select Database:")
        self.db_label.grid(row=0, column=0, pady=5)

        self.db_combobox = ttk.Combobox(self.select_db_frame, state="readonly")
        self.db_combobox.grid(row=0, column=1, pady=5)
        
        self.select_db_button = ttk.Button(self.select_db_frame, text="Select", command=self.load_table_window)
        self.select_db_button.grid(row=0, column=2, padx=5)
        
        # Create Database Frame
        self.root_db_frame = ttk.Frame(self.root, padding="10")
        self.root_db_frame.grid(row=1, column=0, sticky="nsew")

        self.title_db_label = ttk.Label(self.root_db_frame, text="Database Title:")
        self.title_db_label.grid(row=0, column=0, pady=5)

        self.title_db_entry = ttk.Entry(self.root_db_frame)
        self.title_db_entry.grid(row=0, column=1, pady=5)

        # Entry and Type Buttons for Create Database
        self.entry_buttons_frame = ttk.Frame(self.root_db_frame)
        self.entry_buttons_frame.grid(row=1, column=0, columnspan=2, pady=5)

        ttk.Button(self.entry_buttons_frame, text="Add Entry", command=self.add_entry).grid(row=0, column=0, padx=5)
        ttk.Button(self.entry_buttons_frame, text="Remove Entry", command=self.remove_entry).grid(row=0, column=1, padx=5)

        # Dynamic Entry and Type Fields for Create Database
        self.entry_fields_frame = ttk.Frame(self.root_db_frame)
        self.entry_fields_frame.grid(row=2, column=0, columnspan=2, pady=5)

        self.entry_fields = []

        # Create Database Button
        self.create_db_button = ttk.Button(self.root_db_frame, text="Create Database", command=self.create_database)
        self.create_db_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.load_databases()
        
        # Table Window
        self.table_window = None
        
        self.el = ttk.Treeview()

    def add_entry(self):
        entry_frame = ttk.Frame(self.entry_fields_frame)
        entry_frame.grid(row=len(self.entry_fields), column=0, columnspan=2, pady=5)
        ttk.Entry(entry_frame).grid(row=0, column=0, padx=5, pady=5)
        ttk.Combobox(entry_frame, values=["int", "varchar", "text"]).grid(row=0, column=1, padx=5, pady=5)

        self.entry_fields.append(entry_frame)

    def remove_entry(self):
        if self.entry_fields:
            entry_frame = self.entry_fields.pop()
            entry_frame.destroy()

    def create_database(self):
        db_title = self.title_db_entry.get()

        if db_title:
            db_file = f"{db_title}.db"

            # Create or connect to the database
            db_manager = DatabaseManager(db_file)
            cursor = db_manager.cursor

            # Create table with fields
            fields = ["id integer PRIMARY KEY AUTOINCREMENT"]
            for entry_frame in self.entry_fields:
                entry_widgets = entry_frame.winfo_children()
                field_name = entry_widgets[0].get()
                field_type = entry_widgets[1].get()

                if field_name and field_type:
                    fields.append(f"{field_name} {field_type}")
                print(fields)

            create_table_query = f"CREATE TABLE IF NOT EXISTS {db_title} ({', '.join(fields)});"
            print(create_table_query)
            
            cursor.execute(create_table_query)
            db_manager.conn.commit()
            
            messagebox.showinfo("Database Created", f"The database '{db_file}' has been created successfully.")

            # Refresh the list of databases
            self.load_databases()

    def load_databases(self):
        db_files = [file for file in os.listdir() if file.endswith(".db")]
        self.db_combobox["values"] = db_files

    def load_table_window(self):
        selected_db = self.db_combobox.get()
        if selected_db:
            if self.table_window:
                self.table_window.destroy()

            self.table_window = tk.Toplevel(self.root)
            ##Centralizing Window
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_position = (screen_width - 1000) // 2
            y_position = (screen_height - 600) // 2
            self.table_window.geometry(f"{1000}x{600}+{x_position}+{y_position}")
            ####
            self.table_window.title(selected_db)

            db_manager = DatabaseManager(selected_db)
            table_names = db_manager.get_table_names()

            # Table Selection Frame
            table_select_frame = ttk.Frame(self.table_window, padding="10")
            table_select_frame.grid(row=0, column=0, sticky="nsew")

            self.table_combobox = ttk.Combobox(table_select_frame, values=table_names, state="readonly")
            self.table_combobox.grid(row=0, column=0, pady=5)
            self.table_combobox.current(0)
            self.update_table_button = ttk.Button(table_select_frame, text="Update Table", command=lambda: self.load_table_data(db_manager))
            self.update_table_button.grid(row=0, column=2, pady=5)

            self.load_table_data(db_manager)

    def load_table_data(self, db_manager):
                
        selected_table = self.table_combobox.get()
        print(selected_table)
        if selected_table:            
            data = db_manager.get_table_data(selected_table)
            
            # Display Data Frame
            display_frame = ttk.Frame(self.table_window, padding="10")
            display_frame.grid(row=1, column=0, sticky="nsew")

            # Create Treeview (Table)
            tree = ttk.Treeview(display_frame, columns=data[0], show="headings", selectmode="browse")
            for col in data[0]:
                tree.heading(col, text=col)
                tree.column(col, width=100, anchor="center")

            for row in data[1:]:
                tree.insert("", "end", values=row)

            tree.grid(row=0, column=0, padx=5, pady=5)
            
            self.el = tree
            # Delete Data Button
            delete_button = ttk.Button(display_frame, text="Delete Data", command=lambda: self.delete_data(db_manager, tree))
            delete_button.grid(row=1, column=0, pady=5)

            # Create Inputs Button
            create_inputs_button = ttk.Button(display_frame, text="Create Inputs", command=lambda: self.create_inputs(selected_table, db_manager, tree))
            create_inputs_button.grid(row=1, column=1, pady=5)
            
            ######################################## <<<<<<<<<<<<<<<<<<<<<<<<
            #Insert a Table Widget
            #insert_table = ttk.Treeview(display_frame, columns=data[0], show="headings", selectmode="browse")

    def create_inputs(self, table_name, db_manager, tree):
        # Get table columns
        columns = db_manager.cursor.execute(f"PRAGMA table_info({table_name});").fetchall()

        # Input Frame
        input_frame = ttk.Frame(self.table_window, padding="10")
        input_frame.grid(row=2, column=0, sticky="nsew")

        # Entry Widgets (excluding 'id')
        self.input_entries = []
        for col in columns:
            if col[1] != 'id':
                label = ttk.Label(input_frame, text=col[1])
                label.grid(row=0, column=col[0], padx=5, pady=5)

                entry = ttk.Entry(input_frame)
                entry.grid(row=1, column=col[0], padx=5, pady=5)
                self.input_entries.append(entry)

        # Add Data Button
        add_data_button = ttk.Button(input_frame, text="Add Data", command=lambda: self.add_data(table_name, db_manager, tree))
        add_data_button.grid(row=2, column=len(columns) - 1, padx=5, pady=5)

    def delete_data(self, db_manager, tree):
        selected_item = tree.selection()
        if selected_item:
            row_id = tree.item(selected_item, "values")[0]
            selected_table = self.table_combobox.get()
            db_manager.delete_data(selected_table, row_id)
            self.load_table_data(db_manager)          

    def add_data(self, table_name, db_manager, tree):
        
        # Get input values
        values = [entry.get() for entry in self.input_entries]
        print("values", values)
        columns = db_manager.get_table_columns(table_name)
        # Extrair os nomes das colunas (excluindo 'id')
        columns = [column[1] for column in columns if column[1] != 'id']   
        columns = ','.join(columns)    
        # Insert data into the table
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['?'] * len(values))});"
      
        db_manager.cursor.execute(query, values)
        
        db_manager.conn.commit()

        # Reload table data
        self.load_table_data(db_manager)
        
    def load_create_table_window(self):
        self.table_window = tk.Toplevel(self.root)
        ##Centralizing Window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width - 1000) // 2
        y_position = (screen_height - 600) // 2
        self.table_window.geometry(f"{1000}x{600}+{x_position}+{y_position}")
        ####
        self.table_window.title("Create Table")

        self.conn = DatabaseManager().conn
        self.cursor = self.conn.cursor()
        
        ######################################################
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - 600) // 2
    y_position = (screen_height - 400) // 2
    root.geometry(f"{600}x{400}+{x_position}+{y_position}")
    root.mainloop()





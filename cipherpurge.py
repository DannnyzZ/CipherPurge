########################################
# CipherPurge v1.0 by DannnyzZ         #
########################################

import os
import random
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, PhotoImage
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import shutil
import send2trash
import threading

# Define color scheme
BACKGROUND_COLOR = "#282634"  # Dark gray background
BUTTON_COLOR = "#c6394e"      # Red buttons
LIST_COLOR = "#FFFFFF"
TEXT_COLOR = "#dcdcdc"        # Light gray text
FONT = ("Cambria", 13)

class DataOverwriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CipherPurge v1.0")
        self.root.geometry("800x640")  # Adjusted window size
        self.root.configure(background=BACKGROUND_COLOR)

        self.selected_files = []
        self.action_history = []

        self.create_menu()
        self.create_widgets()

        # Define the log file name
        current_folder = os.getcwd()
        current_user = os.getlogin()
        log_number = random.randint(1, 1000)
        log_filename = f"{current_user}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{log_number}_log.txt"
        self.log_file = os.path.join(current_folder, log_filename)

        # Create a "Logs" folder in the current location if it doesn't exist
        log_folder = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Update the log file path to be within the "Logs" folder
        log_filename = f"{current_user}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{log_number}_log.txt"
        self.log_file = os.path.join(log_folder, log_filename)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, mode='determinate')
        self.progress_bar.pack(fill=tk.X, padx=20, pady=5)
        
        self.root.mainloop()

    def empty_trash(self):
        if not self.action_history:
            messagebox.showinfo("Empty Trash", "There aren't any elements to move")
            return

        def empty_trash_thread():
            try:
                trash_folder = os.path.join(os.path.expanduser("~"), ".Trash")
                send2trash.send2trash(trash_folder)
                action_message = "Emptied the trash."
                self.action_history.append(action_message)
                self.log_action(action_message)
            except Exception as e:
                action_message = f"Failed to empty the trash: {str(e)}"
                self.action_history.append(action_message)
                self.log_action(action_message)

            try:
                # Empty the system trash as well
                send2trash.send2trash(os.path.expanduser("~"))
                system_trash_message = "Emptied the system trash."
                self.action_history.append(system_trash_message)
                self.log_action(system_trash_message)
            except Exception as e:
                system_trash_message = f"Failed to empty the system trash: {str(e)}"
                self.action_history.append(system_trash_message)
                self.log_action(system_trash_message)

            self.update_history_listbox()

        # Launch empty trash action in a thread
        trash_thread = threading.Thread(target=empty_trash_thread)
        trash_thread.start()

    def log_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: {action}\n"
        try:
            with open(self.log_file, "a", encoding="utf-8") as log:
                log.write(log_entry)
        except Exception as e:
            print("Error writing to log file:", e)

    def generate_new_file_name(self, action_count):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_string = ''.join(random.choice('01') for _ in range(10))  # 10-digit random binary string
        new_file_name = f"{random_string}_{timestamp}_{action_count}.txt"
        return new_file_name

    def encrypt_data(self, data):
        # Create a fixed AES-256 key (256 bits = 32 bytes)
        aes_key = os.urandom(32)

        # Encrypt data using AES-256 key
        backend = default_backend()
        iv = os.urandom(16)  # Generate a random initialization vector (IV)
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=backend)
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()

        return iv, encrypted_data

    def overwrite_sanitize_and_encrypt(self):
        total_files = len(self.selected_files)
        for action_count, file_path in enumerate(self.selected_files, start=1):
            with open(file_path, 'rb') as file:
                data = file.read()

            # Randomize data before encryption
            data = os.urandom(len(data))

            # Zero out data before encryption
            data = bytes(len(data))

            iv, encrypted_data = self.encrypt_data(data)

            with open(file_path, 'wb') as file:
                file.write(encrypted_data)

            new_file_name = self.generate_new_file_name(action_count)
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
            os.rename(file_path, new_file_path)

            # Move the encrypted file to the trash using shutil.move
            try:
                trash_folder = os.path.join(os.path.expanduser("~"), ".Trash")
                if not os.path.exists(trash_folder):
                    os.makedirs(trash_folder)
                shutil.move(new_file_path, trash_folder)
                action_message = f"Sanitized, randomized, zeroed, encrypted, and moved {os.path.basename(file_path)} to trash."
            except Exception as e:
                action_message = f"Sanitized, randomized, zeroed, and encrypted {os.path.basename(file_path)}, but failed to move to trash: {e}."

            self.action_history.append(action_message)
            self.log_action(action_message)

            self.progress_var.set(action_count / total_files * 100)
            self.root.update_idletasks()

        self.progress_var.set(100)
        self.root.update_idletasks()

        messagebox.showinfo("Operation Complete", "Files have been sanitized, randomized, zeroed, encrypted, and moved to trash.")

        self.progress_var.set(0)  # Reset progress bar to 0

        self.selected_files.clear()  # Clear selected files
        self.listbox.delete(0, tk.END)  # Clear listbox

        self.log_action("All files have been sanitized, randomized, zeroed, and encrypted.")
        self.update_history_listbox()

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for action in self.action_history:
            self.history_listbox.insert(tk.END, action)

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open Files", command=self.browse_files)
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
        
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Manual", command=self.open_manual)
        self.help_menu.add_command(label="About", command=self.show_about)
        
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Clear History", command=self.clear_history)

    def clear_history(self):
        self.action_history.clear()
        self.update_history_listbox()
        self.log_action("Cleared history")

    def open_manual(self):
        manual_text = """
        Usage Guide - Quick start

        Step 1: Select Files - Click "Open Files" to choose the files you want to process.

        Step 2: Sanitize and Encrypt - Click "SANITIZE AND ENCRYPT DATA" to perform the following actions on choosen files: randomize, zeroing, encryption and moving to trash.

        Step 3: Monitor Progress - Observe the progress bar to track ongoing operations.

        Step 4: History of Actions - Review the "History of Actions" section to see a log of performed actions.

        Step 5: Empty Trash (Optional) - Click "Move to trash" to permanently delete files (irreversible).

        Note: CipherPurge actions are irreversible; use with caution.
        You're now ready to enhance data security with CipherPurge v1.0!
        For assistance, contact the developer.
        """
        messagebox.showinfo("CipherPurge Usage Guide", manual_text)
        self.log_action("User opened usage guide")

    
    def show_about(self):
        about_text = "CipherPurge\nVersion 1.0\nCopyright © DannnyzZ\nGitHub https://github.com/DannnyzZ"
        messagebox.showinfo("About", about_text)

    def delete_selected(self):
        selected_indices = self.listbox.curselection()
        selected_indices = list(selected_indices)  # Convert tuple to list

        for idx in selected_indices[::-1]:
            file_path = self.selected_files[idx]
            self.selected_files.pop(idx)
            self.listbox.delete(idx)
            self.action_history.append(f"Deleted {os.path.basename(file_path)}")

        self.update_history_listbox()
        self.log_action("Removed selected files from list")

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.frame.pack(padx=5, pady=5)

        self.label = tk.Label(self.frame, text="List of files to overwrite:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=FONT)
        self.label.pack()

        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(fill=tk.X)

        self.button_open = tk.Button(self.button_frame, text="Open Files", command=self.browse_files, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=FONT)
        self.button_open.pack(side=tk.LEFT, padx=5)

        self.button_delete = tk.Button(self.button_frame, text="Remove from list", command=self.delete_selected, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=FONT)
        self.button_delete.pack(side=tk.LEFT, padx=5)

        self.button_empty_trash = tk.Button(self.button_frame, text="Move to trash", command=self.empty_trash, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=FONT)
        self.button_empty_trash.pack(side=tk.LEFT, padx=5)

        self.listbox_frame = tk.Frame(self.frame)
        self.listbox_frame.pack()

        self.listbox_scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.listbox_frame, height=10, width=110, selectmode=tk.MULTIPLE, yscrollcommand=self.listbox_scrollbar.set, bg=LIST_COLOR, fg="black", font=FONT)
        self.listbox_scrollbar.config(command=self.listbox.yview)


        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.options_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.options_frame.pack(padx=20, pady=10)

        self.overwrite_and_move_button = tk.Button(self.options_frame, text="SANITIZE AND ENCRYPT DATA", command=self.confirm_overwrite_and_move, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=FONT)
        self.overwrite_and_move_button.pack(pady=1)

        self.history_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.history_frame.pack(padx=20, pady=10)

        self.history_label = tk.Label(self.history_frame, text="History of Actions:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=FONT)
        self.history_label.pack()

        self.history_text_frame = tk.Frame(self.history_frame)
        self.history_text_frame.pack()

        self.history_listbox_scrollbar = tk.Scrollbar(self.history_text_frame, orient=tk.VERTICAL)
        self.history_listbox = tk.Listbox(self.history_text_frame, height=10, width=110, yscrollcommand=self.history_listbox_scrollbar.set, bg=LIST_COLOR, fg=TEXT_COLOR, font=FONT)
        self.history_listbox_scrollbar.config(command=self.history_listbox.yview)

        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.history_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.root.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, event):
        # You can add any necessary functionality here.
        pass

    def confirm_overwrite_and_move(self):
        if not self.selected_files:
            messagebox.showinfo("Confirmation", "No files selected for sanitizing and encrypting.")
            return

        result = messagebox.askyesno("Confirmation", "Are you sure you want to overwrite selected files and move them to the trash?\nThis operation is irreversible!")
        if result:
            self.overwrite_sanitize_and_encrypt()

    def browse_files(self):
        try:
            file_paths = filedialog.askopenfilenames(filetypes=[("All Files", "*.*")])
            if file_paths:
                for file_path in file_paths:
                    filename = os.path.basename(file_path)
                    filesize = os.path.getsize(file_path)
                    file_extension = os.path.splitext(file_path)[1]
                    self.listbox.insert(tk.END, f"{len(self.selected_files) + 1}. {filename} | Size: {filesize} bytes | Extension: {file_extension}")
                    self.selected_files.append(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while browsing files: {e}")

if __name__ == "__main__":
    root = tk.Tk()

    # Load GIF icon as a PhotoImage object
    icon = PhotoImage(file="C:\\Users\\danie\\OneDrive\\Documents\\Desktop\\CipherPurge\\CipherPurge_logo.gif")

    # Set the application icon
    root.iconphoto(True, icon)

    app = DataOverwriterApp(root)
    root.configure(background=BACKGROUND_COLOR)
    root.mainloop()

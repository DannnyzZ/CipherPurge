########################################
#     CipherPurge v1.0 by DannnyzZ     #
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
import base64

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

        # Base64 format 
        self.icon_base64 = b"""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"""

        # Convert base64 on PhotoImage
        self.icon_image = tk.PhotoImage(data=self.icon_base64)

        # Set icon as default
        self.root.iconphoto(True, self.icon_image)
        
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

        Step 1: Select Files - Click "Open Files" to choose the files you want to process.

        Step 2: Sanitize and Encrypt - Click "SANITIZE AND ENCRYPT DATA" to perform the following actions on choosen files: randomize, zeroing, encryption and moving to trash.

        Step 3: Monitor Progress - Observe the progress bar to track ongoing operations.

        Step 4: History of Actions - Review the "History of Actions" section to see a log of performed actions.

        Step 5: Empty Trash (Optional) - Click "Move to trash" to remove files from indexing.

        Note: CipherPurge actions are irreversible; use with caution. For assistance, contact the developer.
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

    app = DataOverwriterApp(root)

    # Set the application icon using self.icon_image
    root.iconphoto(True, app.icon_image)

    root.configure(background=BACKGROUND_COLOR)
    root.mainloop()

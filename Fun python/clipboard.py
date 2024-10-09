import tkinter as tk
import pyperclip
import threading
import time

class ClipboardHistoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard History Tracker")

        self.history = []
        self.max_history_length = 10  # Limit the number of entries in history

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.listbox.pack(pady=10)

        self.paste_button = tk.Button(root, text="Paste Selected", command=self.paste_selected)
        self.paste_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear History", command=self.clear_history)
        self.clear_button.pack(pady=5)

        self.start_clipboard_monitor()

    def start_clipboard_monitor(self):
        """Start monitoring the clipboard in a separate thread."""
        threading.Thread(target=self.monitor_clipboard, daemon=True).start()

    def monitor_clipboard(self):
        """Monitor the clipboard for changes and update history."""
        previous_value = ""
        while True:
            current_value = pyperclip.paste()
            if current_value != previous_value:
                previous_value = current_value
                self.add_to_history(current_value)
            time.sleep(1)

    def add_to_history(self, item):
        """Add a new item to the clipboard history."""
        if item in self.history:
            self.history.remove(item)  # Remove duplicates
        self.history.append(item)

        # Limit the history size
        if len(self.history) > self.max_history_length:
            self.history.pop(0)

        self.update_listbox()

    def update_listbox(self):
        """Update the listbox with the current history."""
        self.listbox.delete(0, tk.END)
        for item in self.history:
            self.listbox.insert(tk.END, item)

    def paste_selected(self):
        """Paste the selected item from the history to the clipboard."""
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.history[selected_index[0]]
            pyperclip.copy(selected_item)
            print(f"Pasted: {selected_item}")

    def clear_history(self):
        """Clear the clipboard history."""
        self.history.clear()
        self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardHistoryApp(root)
    root.mainloop()
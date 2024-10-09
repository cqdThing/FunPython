import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PIL import Image

class AutomationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation Tool")

        # File Renaming Section
        self.rename_frame = tk.LabelFrame(root, text="File Renaming", padx=10, pady=10)
        self.rename_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.rename_label = tk.Label(self.rename_frame, text="Directory:")
        self.rename_label.grid(row=0, column=0, sticky="w")

        self.rename_dir_entry = tk.Entry(self.rename_frame, width=40)
        self.rename_dir_entry.grid(row=0, column=1)

        self.rename_button = tk.Button(self.rename_frame, text="Browse", command=self.browse_rename)
        self.rename_button.grid(row=0, column=2)

        self.rename_suffix_label = tk.Label(self.rename_frame, text="Suffix:")
        self.rename_suffix_label.grid(row=1, column=0, sticky="w")

        self.rename_suffix_entry = tk.Entry(self.rename_frame)
        self.rename_suffix_entry.grid(row=1, column=1)

        self.rename_apply_button = tk.Button(self.rename_frame, text="Rename Files", command=self.rename_files)
        self.rename_apply_button.grid(row=2, columnspan=3, pady=10)

        # Image Resizing Section
        self.resize_frame = tk.LabelFrame(root, text="Image Resizing", padx=10, pady=10)
        self.resize_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.resize_label = tk.Label(self.resize_frame, text="Directory:")
        self.resize_label.grid(row=0, column=0, sticky="w")

        self.resize_dir_entry = tk.Entry(self.resize_frame, width=40)
        self.resize_dir_entry.grid(row=0, column=1)

        self.resize_button = tk.Button(self.resize_frame, text="Browse", command=self.browse_resize)
        self.resize_button.grid(row=0, column=2)

        self.resize_width_label = tk.Label(self.resize_frame, text="Width:")
        self.resize_width_label.grid(row=1, column=0, sticky="w")

        self.resize_width_entry = tk.Entry(self.resize_frame)
        self.resize_width_entry.grid(row=1, column=1)

        self.resize_apply_button = tk.Button(self.resize_frame, text="Resize Images", command=self.resize_images)
        self.resize_apply_button.grid(row=2, columnspan=3, pady=10)

    def browse_rename(self):
        dir_path = filedialog.askdirectory()
        self.rename_dir_entry.delete(0, tk.END)
        self.rename_dir_entry.insert(0, dir_path)

    def rename_files(self):
        directory = self.rename_dir_entry.get()
        suffix = self.rename_suffix_entry.get()
        if not directory or not suffix:
            messagebox.showerror("Error", "Please select a directory and enter a suffix.")
            return

        try:
            for filename in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, filename)):
                    base, ext = os.path.splitext(filename)
                    new_name = f"{base}{suffix}{ext}"
                    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            messagebox.showinfo("Success", "Files renamed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def browse_resize(self):
        dir_path = filedialog.askdirectory()
        self.resize_dir_entry.delete(0, tk.END)
        self.resize_dir_entry.insert(0, dir_path)

    def resize_images(self):
        directory = self.resize_dir_entry.get()
        width = self.resize_width_entry.get()
        if not directory or not width:
            messagebox.showerror("Error", "Please select a directory and enter a width.")
            return

        try:
            width = int(width)
            for filename in os.listdir(directory):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    img_path = os.path.join(directory, filename)
                    with Image.open(img_path) as img:
                        aspect_ratio = img.height / img.width
                        new_height = int(width * aspect_ratio)
                        img = img.resize((width, new_height), Image.ANTIALIAS)
                        img.save(img_path)
            messagebox.showinfo("Success", "Images resized successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid width.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationTool(root)
    root.mainloop()
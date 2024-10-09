import tkinter as tk
import psutil

class SystemMetricsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Metrics Monitor")

        self.cpu_label = tk.Label(root, text="CPU Usage: 0%", font=("Helvetica", 16))
        self.cpu_label.pack(pady=10)

        self.memory_label = tk.Label(root, text="Memory Usage: 0%", font=("Helvetica", 16))
        self.memory_label.pack(pady=10)

        self.update_metrics()

    def update_metrics(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")

        # Call this method again after 1000 ms (1 second)
        self.root.after(1000, self.update_metrics)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMetricsApp(root)
    root.mainloop()
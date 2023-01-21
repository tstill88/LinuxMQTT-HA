import tkinter as tk
from tkinter import ttk
from agent import CpuAgent

class CpuAgentGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cpu Agent")
        self.geometry("300x200")

        self.cpu_var = tk.BooleanVar()
        self.memory_var = tk.BooleanVar()
        self.disk_var = tk.BooleanVar()
        self.network_var = tk.BooleanVar()
        self.mqtt_status = tk.StringVar()

        self.create_widgets()
    def create_widgets(self):
        self.cpu_chk = ttk.Checkbutton(self, text="CPU", variable=self.cpu_var)
        self.cpu_chk.grid(column=0, row=0)

        self.memory_chk = ttk.Checkbutton(self, text="Memory", variable=self.memory_var)
        self.memory_chk.grid(column=0, row=1)

        self.disk_chk = ttk.Checkbutton(self, text="Disk", variable=self.disk_var)
        self.disk_chk.grid(column=0, row=2)

        self.network_chk = ttk.Checkbutton(self, text="Network", variable=self.network_var)
        self.network_chk.grid(column=0, row=3)
        
        self.mqtt_status_label = ttk.Label(self, textvariable=self.mqtt_status)
        self.mqtt_status_label.grid(column=0, row=4)
        
        self.start_button = ttk.Button(self, text="Start", command=self.start)
        self.start_button.grid(column=0, row=5)

    def start(self):
        self.cpu_agent = CpuAgent(args.host, args.port)
        self.mqtt_status.set("Connected to MQTT")
        if self.cpu_var.get():
            self.cpu_agent.publish_metrics()
        if self.memory_var.get():
            self.cpu_agent.publish_memory_metrics()
        if self.disk_var.get():
            self.cpu_agent.publish_disk_metrics()
        if self.network_var.get():
            self.cpu_agent.publish_network_metrics()
if __name__ == "__main__":
    app = CpuAgentGUI()
    app.mainloop()

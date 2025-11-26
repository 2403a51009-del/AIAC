# file: c:\Users\prana\ai lab 22\task1.py
import socket
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

def scan_port(host: str, port: int, timeout: float = 1.0):
    """Try to connect to (host, port). Return port on success, None on failure."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return port if result == 0 else None
    except Exception:
        return None

def network_scan(host: str, start_port: int, end_port: int, max_threads: int,
                 timeout: float, stop_event: threading.Event,
                 progress_callback, found_callback):
    """
    Scans ports in [start_port, end_port] using a ThreadPoolExecutor.
    progress_callback(done, total) and found_callback(port) are called
    from the worker thread (the caller marshals to the main thread).
    """
    total = end_port - start_port + 1
    open_ports = []
    ports = range(start_port, end_port + 1)
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_port = {executor.submit(scan_port, host, p, timeout): p for p in ports}
        done_count = 0
        try:
            for fut in as_completed(future_to_port):
                # If the GUI requested stop, cancel remaining futures and exit loop
                if stop_event.is_set():
                    for f in future_to_port:
                        try:
                            if not f.done():
                                f.cancel()
                        except Exception:
                            pass
                    break
                try:
                    res = fut.result()
                except Exception:
                    res = None
                done_count += 1
                if res:
                    open_ports.append(res)
                    try:
                        found_callback(res)
                    except Exception:
                        pass
                try:
                    progress_callback(done_count, total)
                except Exception:
                    pass
        finally:
            stop_event.set()
    return sorted(open_ports)

class PortScannerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Port Scanner")
        self.resizable(False, False)
        self.stop_event = threading.Event()
        self.scan_thread = None
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(self, padding=10)
        frm.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frm, text="Target host:").grid(row=0, column=0, sticky="e")
        self.host_var = tk.StringVar(value="127.0.0.1")
        ttk.Entry(frm, width=25, textvariable=self.host_var).grid(row=0, column=1, sticky="w")

        ttk.Label(frm, text="Start port:").grid(row=1, column=0, sticky="e")
        self.start_var = tk.IntVar(value=1)
        ttk.Entry(frm, width=10, textvariable=self.start_var).grid(row=1, column=1, sticky="w")

        ttk.Label(frm, text="End port:").grid(row=2, column=0, sticky="e")
        self.end_var = tk.IntVar(value=1024)
        ttk.Entry(frm, width=10, textvariable=self.end_var).grid(row=2, column=1, sticky="w")

        ttk.Label(frm, text="Threads:").grid(row=3, column=0, sticky="e")
        self.threads_var = tk.IntVar(value=100)
        ttk.Entry(frm, width=10, textvariable=self.threads_var).grid(row=3, column=1, sticky="w")

        ttk.Label(frm, text="Timeout (s):").grid(row=4, column=0, sticky="e")
        self.timeout_var = tk.DoubleVar(value=1.0)
        ttk.Entry(frm, width=10, textvariable=self.timeout_var).grid(row=4, column=1, sticky="w")

        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=(8, 0))
        self.start_btn = ttk.Button(btn_frame, text="Start Scan", command=self.start_scan)
        self.start_btn.grid(row=0, column=0, padx=5)
        self.stop_btn = ttk.Button(btn_frame, text="Stop", command=self.stop_scan, state="disabled")
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.progress = ttk.Progressbar(frm, length=360, mode="determinate")
        self.progress.grid(row=6, column=0, columnspan=2, pady=(10, 0))

        ttk.Label(frm, text="Open ports:").grid(row=7, column=0, columnspan=2, sticky="w", pady=(8, 0))
        self.result_box = scrolledtext.ScrolledText(frm, width=48, height=12, state="disabled")
        self.result_box.grid(row=8, column=0, columnspan=2, pady=(4, 0))

    def start_scan(self):
        if self.scan_thread and self.scan_thread.is_alive():
            return

        host = self.host_var.get().strip()
        if not host:
            messagebox.showerror("Invalid host", "Please enter a target host or IP address.")
            return

        # Resolve hostname to IP early so we fail fast on DNS errors.
        try:
            host_ip = socket.gethostbyname(host)
        except Exception as e:
            messagebox.showerror("Host resolution failed", f"Could not resolve host '{host}': {e}")
            return

        try:
            start = int(self.start_var.get())
            end = int(self.end_var.get())
            threads = int(self.threads_var.get())
            timeout = float(self.timeout_var.get())
        except Exception:
            messagebox.showerror("Invalid input", "Please enter valid numeric values for ports/threads/timeout.")
            return

        if start < 1 or end < start or end > 65535:
            messagebox.showerror("Invalid ports", "Please provide a valid port range (1-65535).")
            return
        if threads < 1:
            messagebox.showerror("Invalid threads", "Threads must be at least 1.")
            return

        total_ports = end - start + 1
        # Cap threads to a reasonable amount and to the number of ports
        max_threads = max(1, min(threads, total_ports, 1000))

        self.stop_event.clear()
        self.progress["value"] = 0
        self.progress["maximum"] = total_ports

        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)
        self.result_box.config(state="disabled")

        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")

        def progress_cb(done, total):
            self.after(0, lambda: self.progress.config(value=done))

        def found_cb(port):
            self.after(0, lambda: self._append_result(port))

        def worker():
            try:
                open_ports = network_scan(host_ip, start, end, max_threads, timeout,
                                          self.stop_event, progress_cb, found_cb)
                self.after(0, lambda: self._scan_done_summary(open_ports))
            except Exception as e:
                self.after(0, lambda: messagebox.showerror("Error", f"Scan error: {e}"))
            finally:
                self.after(0, self.scan_finished)

        self.scan_thread = threading.Thread(target=worker, daemon=True)
        self.scan_thread.start()

    def _append_result(self, port):
        self.result_box.config(state="normal")
        self.result_box.insert(tk.END, f"{port}\n")
        self.result_box.see(tk.END)
        self.result_box.config(state="disabled")

    def _scan_done_summary(self, open_ports):
        count = len(open_ports)
        if count:
            if count <= 10:
                messagebox.showinfo("Scan Results", f"Found {count} open port(s): {', '.join(map(str, open_ports))}")
            else:
                messagebox.showinfo("Scan Results", f"Found {count} open ports. See result list for details.")
        else:
            messagebox.showinfo("Scan Results", "No open ports found in the scanned range.")

    def stop_scan(self):
        self.stop_event.set()
        self.stop_btn.config(state="disabled")

    def scan_finished(self):
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")

if __name__ == "__main__":
    app = PortScannerGUI()
    app.mainloop()

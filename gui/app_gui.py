import tkinter as tk
from tkinter import ttk, scrolledtext
from core.request_handler import send_request
from utils.json_formatter import format_json
import json

def start_app():
    root = tk.Tk()
    root.title("hogan rewish")

    # URL input
    tk.Label(root, text="URL:").grid(row=0, column=0, sticky="e")
    url_entry = tk.Entry(root, width=60)
    url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    # Method dropdown menu
    method_var = tk.StringVar(value="GET")
    tk.Label(root, text="Method:").grid(row=0, column=3)
    method_menu = ttk.Combobox(
        root,
        textvariable=method_var,
        values=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        state="readonly"
    )
    method_menu.grid(row=0, column=4, padx=10)

    # Headers input field
    tk.Label(root, text="Headers (JSON):").grid(row=1, column=0, sticky="nw", padx=10)
    headers_input = scrolledtext.ScrolledText(root, height=5, width=80)
    headers_input.grid(row=1, column=1, columnspan=4, padx=10, pady=(0, 10))

    # Body input field
    tk.Label(root, text="Body (JSON):").grid(row=2, column=0, sticky="nw", padx=10)
    body_input = scrolledtext.ScrolledText(root, height=10, width=80)
    body_input.grid(row=2, column=1, columnspan=4, padx=10, pady=(0, 10))

    # Response output
    tk.Label(root, text="Response:").grid(row=3, column=0, sticky="nw", padx=10)
    response_output = scrolledtext.ScrolledText(root, height=20, width=80)
    response_output.grid(row=3, column=1, columnspan=4, padx=10, pady=(0, 10))

    # Copy to clipboard
    def copy_to_clipboard():
        content = response_output.get("1.0", tk.END)
        root.clipboard_clear()
        root.clipboard_append(content)
        root.update()

    copy_button = tk.Button(root, text="Copy Result", command=copy_to_clipboard)
    copy_button.grid(row=4, column=1, sticky="w", padx=(0, 10), pady=(0, 10))

    # Send Button
    def handle_send():
        url = url_entry.get()
        method = method_var.get().upper() # I needed this so bad
        body = body_input.get("1.0", tk.END).strip()
        headers_raw = headers_input.get("1.0", tk.END).strip()

        try:
            headers = json.loads(headers_raw) if headers_raw else {}
        except json.JSONDecodeError:
            response_output.delete("1.0", tk.END)
            response_output.insert(tk.END, "Invalid JSON in headers")
            return

        response = send_request(url, method, body, headers)
        response_output.delete("1.0", tk.END)
        response_output.insert(tk.END, format_json(response))

    send_button = tk.Button(root, text="Send Request", command=handle_send)
    send_button.grid(row=4, column=4, padx=10, pady=(0, 10))

    root.mainloop()

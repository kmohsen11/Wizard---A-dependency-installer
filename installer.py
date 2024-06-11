import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
import subprocess
from search_handler import search_macports

def install_package(package_name):
    """
    Attempts to install a package using MacPorts. Handles cases where no package is found or installation fails.

    Args:
        package_name (str): The name of the package to install.

    Returns:
        None
    """
    macports_packages = search_macports(package_name)
    if macports_packages:
        root = tk.Tk()
        root.title("Select a package to install")
        lb = Listbox(root)
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        for package in macports_packages:
            lb.insert(tk.END, package)
        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)

        def on_select():
            selected_index = lb.curselection()
            if selected_index:
                try:
                    selected_package = macports_packages[selected_index[0]]
                    subprocess.run(["sudo", "port", "install", selected_package], check=True)
                    messagebox.showinfo("Success", f"{selected_package} installed successfully.")
                except subprocess.CalledProcessError as e:
                    error_code = e.returncode
                    error_msg = f"Failed to install {selected_package} (Error code: {error_code})."
                    # Add more specific error handling based on error_code (optional)
                    print(error_msg)
                    messagebox.showerror("Installation Error", error_msg)
            root.destroy()  # Close window after each attempt

        install_button = tk.Button(root, text="Install Selected Package", command=on_select)
        install_button.pack()
        root.mainloop()

    else:
        # No package found, offer suggestions or further actions
        messagebox.showinfo(
            "No Package Found",
            f"No installable package found for '{package_name}'. \n"
            f"- Try searching for similar packages with broader keywords.\n"
            f"- Check the official MacPorts Packages list (https://ports.macports.org/) for alternatives."
        )

def on_install_click():
    package_name = entry.get()
    install_package(package_name)

# Create the main window
root = tk.Tk()
root.title("Dependency Installer")

# Create a label and entry for the package name
tk.Label(root, text="Enter package name:").pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to install the package
install_button = tk.Button(root, text="Search for Package", command=on_install_click)
install_button.pack()

# Run the Tkinter event loop
root.mainloop()

import subprocess
import tkinter as tk
from tkinter import messagebox

def is_package_installed(package_name):
    """Check if package is installed using brew."""
    try:
        result = subprocess.run(
            ["brew", "list", "--versions", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def get_package_version(package_name):
    """Get the installed version of a package using brew."""
    if is_package_installed(package_name):
        return "installed"
    else:
        return None

def check_for_update(package_name):
    """Check if there is an update available for a package."""
    try:
        result = subprocess.run(
            ["brew", "outdated", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().split()[1:]
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def update_package(package_name):
    """Update a package using brew."""
    try:
        result = subprocess.run(
            ["brew", "upgrade", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f"{package_name} has been updated successfully.")
        else:
            print(f"Failed to update {package_name}.")
            print("Error:", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def install_package(package_name):
    """Install a package using brew."""
    try:
        result = subprocess.run(
            ["brew", "install", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f"{package_name} has been installed successfully.")
        else:
            print(f"Failed to install {package_name}.")
            print("Error:", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_package(package_name):
    """Delete a package using brew."""
    try:
        result = subprocess.run(
            ["brew", "uninstall", "--force", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f"{package_name} has been deleted successfully.")
        else:
            print(f"Failed to delete {package_name}.")
            print("Error:", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def get_user_input():
    """Get package name input from the user."""
    package_name = input("Enter the package name to check: ")
    return package_name

# GUI Part
def check_package():
    package_name = entry.get()
    version = get_package_version(package_name)
    
    if version:
        result_label.config(text=f"{package_name} is installed with version {version}.")
        updates = check_for_update(package_name)
        
        if updates:
            result_label.config(text=f"New versions available: {', '.join(updates)}")
            update_button.pack(side=tk.LEFT)
        else:
            result_label.config(text=f"{package_name} is up to date.")
        
        delete_button.pack(side=tk.LEFT)
    else:
        result_label.config(text=f"{package_name} is not installed.")
        install_button.pack(side=tk.LEFT)

def update_package_gui():
    package_name = entry.get()
    update_package(package_name)
    messagebox.showinfo("Info", f"{package_name} has been updated successfully.")

def install_package_gui():
    package_name = entry.get()
    install_package(package_name)
    messagebox.showinfo("Info", f"{package_name} has been installed successfully.")

def delete_package_gui():
    package_name = entry.get()
    delete_package(package_name)
    messagebox.showinfo("Info", f"{package_name} has been deleted successfully.")

root = tk.Tk()
root.title("Dependency Installer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="Enter the package name:")
entry_label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

check_button = tk.Button(frame, text="Check", command=check_package)
check_button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

update_button = tk.Button(root, text="Update", command=update_package_gui)
install_button = tk.Button(root, text="Install", command=install_package_gui)
delete_button = tk.Button(root, text="Delete", command=delete_package_gui)

root.mainloop()

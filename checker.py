import subprocess

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

# Example usage
if __name__ == "__main__":
    package = get_user_input()
    version = get_package_version(package)
    
    if version:
        print(f"{package} is installed with version {version}.")
        updates = check_for_update(package)
        
        if updates:
            print(f"New versions available: {', '.join(updates)}")
            user_choice = input("Do you want to update the package? (yes/no): ").strip().lower()
            
            if user_choice == "yes":
                update_package(package)
            else:
                print(f"{package} will not be updated.")
        else:
            print(f"{package} is up to date.")
        
        delete_choice = input("Do you want to delete the package? (yes/no): ").strip().lower()
        if delete_choice == "yes":
            delete_package(package)
        else:
            print(f"{package} will not be deleted.")
    else:
        print(f"{package} is not installed.")
        user_choice = input("Do you want to install the package? (yes/no): ").strip().lower()
        
        if user_choice == "yes":
            install_package(package)
        else:
            print(f"{package} will not be installed.")

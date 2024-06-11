import subprocess

def is_macports_package_installed(package_name):
    """Check if a MacPorts package is installed."""
    try:
        result = subprocess.run(["port", "installed", package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"Error checking MacPorts package: {e}")
        return False

def is_app_installed(app_name):
    """Check if an app is installed using the `mas` tool."""
    try:
        result = subprocess.run(["mas", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        installed_apps = result.stdout.decode().split('\n')
        for app in installed_apps:
            if app_name.lower() in app.lower():
                return True
        return False
    except Exception as e:
        print(f"Error checking App Store application: {e}")
        return False

def check_and_update_package(package_name):
    """Check if the package is installed and update it if necessary."""
    if is_macports_package_installed(package_name):
        print(f"{package_name} is already installed. Checking for updates...")
        try:
            subprocess.run(["sudo", "port", "upgrade", package_name], check=True)
            print(f"{package_name} updated successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to update {package_name}.")
    elif is_app_installed(package_name):
        print(f"{package_name} is already installed as an App Store application. Checking for updates...")
        try:
            subprocess.run(["mas", "upgrade"], check=True)
            print(f"{package_name} updated successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to update {package_name}.")
    else:
        print(f"{package_name} is not installed.")
        return False

    return True

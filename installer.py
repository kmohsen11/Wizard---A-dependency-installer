import subprocess
from search_handler import search_homebrew, search_app_store
def install_package(package_name):
    homebrew_packages = search_homebrew(package_name)
    if homebrew_packages:
        homebrew_package = homebrew_packages[0]  # Assuming search_homebrew() returns a list of packages
        try:
            subprocess.run(["brew", "install", homebrew_package], check=True)
            print(f"{homebrew_package} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {homebrew_package}.")
    else:
        print(f"No Homebrew package found for {package_name}.")
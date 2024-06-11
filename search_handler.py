import subprocess

def search_macports(package_name):
    """
    Searches MacPorts packages by name.

    Args:
        package_name (str): The name of the package to search.

    Returns:
        list: A list of package names found, or an empty list if none found.
    """
    try:
        result = subprocess.run(["/opt/local/bin/port", "search", package_name], capture_output=True, text=True)
        if result.stdout:
            return result.stdout.splitlines()  # Return list of package names only
        else:
            return []
    except subprocess.CalledProcessError:
        return []


from input_handler import get_user_input
from installer import install_package

def main():
    package_name = get_user_input()
    install_package(package_name)

if __name__ == "__main__":
    main()
 
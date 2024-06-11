from input_handler import get_user_input
from installer import install_package
from checker import check_and_update_package
def main():
    #get user input
    
    package_name = get_user_input()
    
    #search if packages are there, if they are there and there's a newer version, update them
    if not check_and_update_package(package_name):
        
        #if they aren't there, install them
        install_package(package_name)

if __name__ == "__main__":
    main()
 
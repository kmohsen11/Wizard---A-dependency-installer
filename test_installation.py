from installer import install_package

def test_homebrew_install():
    print("Testing Homebrew installation for a valid package:")
    install_package("tree")  # Known valid package

def test_app_store_install():
    print("\nTesting App Store installation for a valid app ID:")
    install_package("409201541")  # Known valid App ID for Pages
    print("\nTesting App Store installation for an invalid app ID:")
    install_package("000000000")  # Invalid App ID

if __name__ == "__main__":
    test_homebrew_install()
    test_app_store_install()

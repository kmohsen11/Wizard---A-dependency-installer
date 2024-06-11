import unittest
from unittest.mock import patch, MagicMock
from checker import is_macports_package_installed, is_app_installed, check_and_update_package

class TestChecker(unittest.TestCase):

    @patch('subprocess.run')
    def test_is_macports_package_installed(self, mock_run):
        # Simulate `port installed package_name` returning success
        mock_run.return_value = MagicMock(returncode=0)
        self.assertTrue(is_macports_package_installed('tree'))

        # Simulate `port installed package_name` returning failure
        mock_run.return_value = MagicMock(returncode=1)
        self.assertFalse(is_macports_package_installed('invalid-package'))

    @patch('subprocess.run')
    def test_is_app_installed(self, mock_run):
        # Simulate `mas list` containing the app name
        mock_run.return_value = MagicMock(stdout=b"409201541 Pages\n")
        self.assertTrue(is_app_installed('Pages'))

        # Simulate `mas list` not containing the app name
        mock_run.return_value = MagicMock(stdout=b"")
        self.assertFalse(is_app_installed('InvalidApp'))

    @patch('subprocess.run')
    def test_check_and_update_package_macports(self, mock_run):
        # Simulate package already installed
        mock_run.side_effect = [
            MagicMock(returncode=0),  # port installed
            MagicMock()               # port upgrade
        ]
        self.assertTrue(check_and_update_package('tree'))

        # Simulate package not installed
        mock_run.side_effect = [
            MagicMock(returncode=1),  # port installed
            MagicMock(returncode=1)   # mas list
        ]
        self.assertFalse(check_and_update_package('invalid-package'))

    @patch('subprocess.run')
    def test_check_and_update_package_app_store(self, mock_run):
        # Simulate app already installed
        mock_run.side_effect = [
            MagicMock(returncode=1),           # port installed
            MagicMock(stdout=b"409201541 Pages\n"),  # mas list
            MagicMock()                          # mas upgrade
        ]
        self.assertTrue(check_and_update_package('Pages'))

        # Simulate app not installed
        mock_run.side_effect = [
            MagicMock(returncode=1),  # port installed
            MagicMock(stdout=b""),    # mas list
        ]
        self.assertFalse(check_and_update_package('InvalidApp'))

if __name__ == '__main__':
    unittest.main()

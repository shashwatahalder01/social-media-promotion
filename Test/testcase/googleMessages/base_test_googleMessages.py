import unittest
from appium import webdriver
from data.data import Data


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.data = Data
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  # 'platformVersion': '11',
                                  # 'deviceName': 'c9c5976',
                                  'automationName': 'UiAutomator2',
                                  'newCommandTimeout': '240',
                                  'appPackage': self.data.gmessages_app_package,
                                  'appActivity': self.data.gmessages_app_activity,
                                  # 'app-package': self.data.skype_app_package,
                                  # 'app-activity': self.data.skype_app_activity,
                                  # 'app': self.data.gmessages,
                                  'appWaitPackage': self.data.gmessages_app_package,
                                  'appWaitActivity': self.data.gmessages_app_activity,
                                  'appWaitDuration': '30000',
                                  'noReset': True,
                                  'fullReset': False,
                                  # 'autoGrantPermissions': True,
                                  })

    def tearDown(self):
        self.driver.quit()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)

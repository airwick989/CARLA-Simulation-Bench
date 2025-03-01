import sys
import subprocess
import unittest
import time

packageName = "com.example.jultrautomaintenance"
activityName = "LoginActivity"

sys.path.insert(1,'/home/rtemsoft/Desktop/CARLA-Simulation-Bench/Working-Directory-v2/testcases')

cmd = f"adb shell am start -n {packageName}/{packageName}.{activityName}"
cmd2 = f"adb shell pidof {packageName}"

#launch app with packageName and intent for the activityName
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

time.sleep(2)

#check if pid exists for app with packageName
proc = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
o, e = proc.communicate()
output = o.decode('ascii')

class TestAppRunning(unittest.TestCase):
    def setUp(self):
        self.longMessage=False
    def test_running(self):
        isRunning = False
        if output != "":
            isRunning = True
            print("App has been launched successfully and is running")
        self.assertTrue(isRunning,msg="FAILURE! App is NOT running!")
if __name__ == '__main__':
    unittest.main()
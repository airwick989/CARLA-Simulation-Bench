import sys
import unittest

sys.path.insert(1,'/home/rtemsoft/Desktop/CARLA-Simulation-Bench/Working-Directory')

import testbed_modified as client
class TestSteeringWheelKit(unittest.TestCase):
    def setUp(self):
        self.longMessage=False
    def test_acceleration_input(self):
        client.main(21)
        self.assertTrue(client.get_speed(client.global_world, 1))
    def test_destroy(self):
        if (client.global_world and client.global_world.recording_enabled):
            client.global_client.stop_recorder()
        if client.global_world is not None:
            client.global_world.destroy()

if __name__ == '__main__':
    unittest.main()
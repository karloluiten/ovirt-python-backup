import unittest
from backupvm import Backup
from ovirtsdk4.types import DiskAttachment, Disk


class TestBackup(unittest.TestCase):
    def test_find_data_device(self):
        expected = '/dev/vdb'
        attachment = DiskAttachment(disk=Disk(id='5986a832-d1e6-40e9-8410-7817f1020a3e'))
        dev = Backup._find_data_disk(attachment)
        self.assertEqual(dev, expected)

    def test_sdk_connection(self):
        self.assertIsNotNone(Backup._get_system_service())


if __name__ == '__main__':
    unittest.main()

import socket

from common import platform_skip, unittest2
import pyuv


class UtilTest(unittest2.TestCase):

    def test_hrtime(self):
        r = pyuv.util.hrtime()
        self.assertTrue(r)

    def test_freemem(self):
        r = pyuv.util.get_free_memory()
        self.assertTrue(r)

    def test_totalmem(self):
        r = pyuv.util.get_total_memory()
        self.assertTrue(r)

    def test_loadavg(self):
        r = pyuv.util.loadavg()
        self.assertTrue(r)

    def test_uptime(self):
        r = pyuv.util.uptime()
        self.assertTrue(r)

    def test_resident_set_memory(self):
        r = pyuv.util.resident_set_memory()
        self.assertTrue(r)

    def test_interface_addresses(self):
        r = pyuv.util.interface_addresses()
        self.assertTrue(r)

    def test_cpu_info(self):
        r = pyuv.util.cpu_info()
        self.assertTrue(r)

    @platform_skip(['darwin'])
    def test_process_title(self):
        title = 'my process'
        pyuv.util.set_process_title(title)
        r = pyuv.util.get_process_title()
        self.assertEqual(r, title)

    def test_getaddrinfo(self):
        def getaddrinfo_cb(result, errorno):
            print result
            self.assertEqual(errorno, None)
        loop = pyuv.Loop.default_loop()
        pyuv.util.getaddrinfo(loop, 'localhost', getaddrinfo_cb, 80, socket.AF_INET)
        loop.run()


if __name__ == '__main__':
    unittest2.main(verbosity=2)


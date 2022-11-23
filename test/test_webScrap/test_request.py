import unittest

from krx_v2.webScrap import request

class Test_request(unittest.TestCase):

    def test_request(self):
        rq = request.Request_price()

        data = rq.request(work={'trdDd':'19950614'})
        print(data)

if __name__ == '__main__':
    unittest.main()
import unittest

from krx_v2.webScrap import request, workingList

class TestWork(unittest.TestCase):

    def test_get_working_list(self):
        work_ = workingList.WorkingList().get_working_list()
        print(work_)
        work_ = work_[4]
        data=work_.get_request_key()
        print(data)

        rq = request.Request_price()
        data = rq.request(work=work_.get_request_key())
        print(data)

if __name__ == '__main__':
    unittest.main()
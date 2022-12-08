from webScrap_v2 import work, util
import datetime


class WorkingList:

    def get_day_list(self, start, end=None):
        start = datetime.datetime.strptime(start, "%Y%m%d")
        if end:
            end = datetime.datetime.strptime(end, "%Y%m%d")
        else:
            end = datetime.datetime.today()
        day_list = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]
        dayList = []
        for date in day_list:
            dayList.append(date.strftime("%Y%m%d"))
        return dayList

    def get_working_list(self):
        dayList = self.get_day_list(start = '19950501')
        return [work.Work(work={'trdDd':day}) for day in dayList]
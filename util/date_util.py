# coding:utf-8
import time, datetime
import math

LOVE_TIME = "2016-01-01"
ONE_DAY_SEC = 24 * 60 * 60


def today_to_loveday_days():
    love_date = datetime.datetime.strptime(LOVE_TIME, "%Y-%m-%d")
    love_sec_float = time.mktime(love_date.timetuple())

    now_sec = time.time()
    days = int(math.floor((now_sec - love_sec_float) / ONE_DAY_SEC) + 1)
    return days


if __name__ == '__main__':
    print today_to_loveday_days()

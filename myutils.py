import datetime
from pytz import timezone, utc


def kst_datetime():
    kst = timezone('Asia/Seoul')
    now = datetime.datetime.utcnow()
    date_time = utc.localize(now).astimezone(kst)
    return date_time


if __name__ == '__main__':
    print(kst_datetime())

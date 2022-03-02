import time
from datetime import datetime


def get_this_time(UTC_TIME=True):
    """
    获取当前的UTC_TIME
    :param UTC_TIME:
    :return:
    """
    # this_time = datetime.now().strftime("%Y%m%d %H:%M:%S")
    if UTC_TIME:
        # 获取当前的 UTC时间 -- datetime类型值
        this_time = datetime.utcnow()
    else:
        # 获取当前时区的时间 -- datetime类型值
        this_time = datetime.now()
    return datetime.fromtimestamp(time.mktime(this_time.timetuple()))

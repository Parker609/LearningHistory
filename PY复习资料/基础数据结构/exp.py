import datetime # datetime是处理日期的api；


def get_delta_event_day(basetime, delta):
    """ 
        将输入的日期 "2023-04-10 23:43:01" 格式转换为这个格式 "20230410"
    """
    date = datetime.datetime.strptime(basetime[0:10], "%Y-%m-%d")
    print(date)
    new_date = date + datetime.timedelta(delta)
    print(new_date)
    event_day = new_date.strftime("%Y%m%d")
    print(event_day)
    return event_day

"""
    将输入的日期 "2023-04-10 23:43:01" 这个格式转化成"2023-04-10"这样的格式
"""
def get_delta_hyphen_event_day(basetime, delta):
    date = datetime.datetime.strptime(basetime[0:10], "%Y-%m-%d")
    new_date = date + datetime.timedelta(days=delta)
    event_day = new_date.strftime("%Y-%m-%d")
    return event_day


base_time = "2023-04-10 23:43:01"
event_day = get_delta_event_day(base_time, 0)
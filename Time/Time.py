时间戳与时间字符串互相转化:
strptime("string format")字符串如“20130512000000”格式的 输入处理函数

localtime(float a)时间戳的输入处理函数

二者返回struct_time结构数据，

由strftime(format, float/time_struct) 和mktime(struct_time)处理后输出，返回日期格式字符串和秒数。

import time

a= "2011-09-28 10:00:00"

对时间处理一般都先转化为struct_time结构，在进行处理，举例如下：

#1中间过程，一般都需要将字符串转化为时间数组

time.strptime(a,'%Y-%m-%d %H:%M:%S')

>>time.struct_time(tm_year=2011, tm_mon=9, tm_mday=27, tm_hour=10, tm_min=50, tm_sec=0, tm_wday=1, tm_yday=270, tm_isdst=-1)

#2将"2011-09-28 10:00:00"转化为时间戳

time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))

>>1317091800.0

#3将时间戳转化为localtime

x = time.localtime(1317091800.0)#localtime参数为float类型

time.strftime('%Y-%m-%d %H:%M:%S',x)

>>2011-09-27 10:50:00

  1，时间戳转化为struct_time
    start_t=time.localtime(start)
    end_t=time.localtime(end)

    2，struct_time转化为指定格式日期字符串
    print time.strftime(ISFORMAT,start_t)
    print time.strftime(ISFORMAT,end_t)
   

    日期字符串的读取：

    tt="201307291008"

    print time.strptime(tt,TIMESTAMP)#读入为struct_time
    print time.mktime(time.strptime(tt,TIMESTAMP))#变为时间戳

today = datetime.datetime.now()
# curr_day = datetime.datetime(year_int, month_int, day_int, hour_int)
curr_day = datetime.datetime(2016, 11, 25, 14)

last_hour = today - datetime.timedelta(hours=1)
yesterday = today - datetime.timedelta(days=1)
last_week = today - datetime.timedelta(weeks=1)
settlementDate = time.strftime('%04d-%02d-%02d' % (yesterday.year, yesterday.month, yesterday.day))

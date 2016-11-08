"""
Corporation A checks every employee's come and go out time.
    emploey    in      out
       A    09:12:23 11:14:45
       B    10:34:01 13:23:40
       C    08:02:02

    if this worker holic didn't go home that day, out time would not exist.

Count the employee present in given time. If given time is 11:00:00, answer is  1
"""

def count_employee_present(employee_log, time_string):

    from datetime import datetime
    import re

    _result_count = 0

    if re.match(r'^\d{1,2}:\d{1,2}:\d{1,2}$', time_string,):
        h, m, s = (int(_) for _ in time_string.split(':'))
    else:
        raise TypeError('hh:mm:ss 형식으로 시간을 입력해야 합니다.')

    if not (0 <= h <= 23):
        raise ValueError('시간은 0~23 사이의 자연수여야 합니다.')
    elif not 0 <= m <= 59:
        raise ValueError('분은 0부터 59 사이의 자연수여야 합니다.')
    elif not 0 <= s <= 59:
        raise ValueError('초는 0부터 59 사이의 자연수여야 합니다.')

    else:
        the_time = datetime.strptime(time_string, '%H:%M:%S')

        for time_tuple in employee_log:
            if len(time_tuple) == 2:
                come_time, out_time = time_tuple
                come_time = datetime.strptime(come_time, '%H:%M:%S')
                out_time = datetime.strptime(out_time, '%H:%M:%S')
                if come_time <= the_time < out_time:
                    _result_count += 1

            elif len(time_tuple) == 1:
                come_time = datetime.strptime(come_time, '%H:%M:%S')
                if come_time <= the_time:
                    _result_count += 1


    print(_result_count)
    return _result_count


employee_log = ([('13:03:2'),
                 ('08:02:1', '21:03:02'),
                 ('10:03:2', '23:21:12')])

count_employee_present(employee_log, '20:30:29')
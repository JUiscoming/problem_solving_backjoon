h, m = map(int, input().split())

minutes = h * 60 + m

minutes_alarm = minutes - 45
if minutes_alarm < 0:
    minutes_alarm += (24 * 60)

h_alarm, m_alarm = divmod(minutes_alarm, 60)
print(h_alarm, m_alarm)
h, m = map(int, input().split())
elapsed_time = int(input())

minutes = h * 60 + m
minutes_baked = (minutes + elapsed_time) % (24 * 60)
h_baked, m_baked = divmod(minutes_baked, 60)
print(h_baked, m_baked)

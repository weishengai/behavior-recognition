import numpy as np

# clip length
# L = 15
L = 8
winWidth = 1280
# winWidth = 640
winHeight = 720
# winHeight = 480
# move_status = ['', 'stand', 'sit', 'walk', 'walk close', 'walk away', 'sit down', 'stand up', 'fall down']
move_status = ['', '站立', '坐', '行走', '走进', '走远', '坐下', '站起来', '摔倒']
fontpath = "./utils/font/simsun.ttc"  # <== 这里是宋体路径
fontsize = 64

c = np.random.rand(32, 3) * 255
sort_max_age = 20
sort_min_hit = 3


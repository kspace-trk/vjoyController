import pyvjoy
import time

j = pyvjoy.VJoyDevice(1)

# ジョイスティックの軸を元に戻す（中央に配置する）
j.data.wAxisX = 0x4000
j.data.wAxisY = 0x4000



# for i in range(0,10000,1):
# ジョイスティックのX軸を前に倒す（前進する）
j.data.wAxisX = 0x8000

# vJoyデバイスにデータを送信
j.update()
print('updated')

# 3秒間待つ
time.sleep(3)

# ジョイスティックの軸を元に戻す（中央に配置する）
j.data.wAxisX = 0x4000
j.data.wAxisY = 0x4000

# vJoyデバイスにデータを送信
j.update()


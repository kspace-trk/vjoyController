import pyvjoy
import time

j = pyvjoy.VJoyDevice(1)

# ジョイスティックの軸を元に戻す（中央に配置する）
j.data.wAxisX = 0x4000
j.data.wAxisY = 0x4000
j.data.wAxisZ = 0x4000


# ジョイスティックのX軸を前に倒す
j.data.wAxisX = 0x8000
j.data.wAxisY = 0x4000

# vJoyデバイスにデータを送信
j.update()
print('updated')
print(dir(j.data))

# 3秒間待つ
time.sleep(3)

# ジョイスティックの軸を元に戻す（中央に配置する）
j.data.wAxisX = 0x4000
j.data.wAxisY = 0x4000
j.data.wAxisZ = 0x4000

# vJoyデバイスにデータを送信
j.update()

# 念のためリセット
j.reset_povs()
j.reset()

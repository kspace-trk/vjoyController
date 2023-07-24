import pyvjoy

j = pyvjoy.VJoyDevice(1)

j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)

j.reset_povs()
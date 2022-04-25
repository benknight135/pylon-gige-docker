from pypylon import pylon

# Create TlFactory
tl_factory = pylon.TlFactory.GetInstance()

# Get connected devices
devices = tl_factory.EnumerateDevices()
# List connected GigE devices
for device in devices:
    # Only print info on GigE devices
    if device.GetDeviceClass() == 'BaslerGigE':
        print(
            "Device %s @ %s (%s)" % (
                device.GetModelName(),
                device.GetIpAddress(),
                device.GetMacAddress()))
else:
    raise EnvironmentError("no GigE devices found")

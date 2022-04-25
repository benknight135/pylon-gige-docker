from pypylon import pylon

# Create TlFactory
tl_factory = pylon.TlFactory.GetInstance()

# Get connected devices
devices = tl_factory.EnumerateDevices()
if (len(devices) <= 0):
    raise EnvironmentError("no devices found")
# List connected devices
gige_devices = []
for device in devices:
    # Add GigE camera to list
    if device.GetDeviceClass() == 'BaslerGigE':
        gige_devices.append(device)
# Check a GigE device was found
if (len(gige_devices) <= 0):
    raise EnvironmentError("no GigE devices found")
# Print connected GigE devices
for device in gige_devices:
    print(
        "Device %s @ %s (%s)" % (
            device.GetModelName(),
            device.GetIpAddress(),
            device.GetMacAddress()))

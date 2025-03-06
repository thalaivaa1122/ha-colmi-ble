# What?
This is a VERY early attempt to integrate the Colmi line of smart rings with Home Assistant. It is an incomplete work in progress.
Colmi rings (like the R02, R06, R10 etc) can be found for udner $20 on AliExpress.

# How?
This is built on top of tahnok's Python API (https://github.com/tahnok/colmi_r02_client) and ludeeus's Home Assistant Integration blueprint (https://github.com/ludeeus/integration_blueprint)

# Requirements
Your home assistant device must have the ability to make active Bluetooth Low Energy (BLE) connections. The bluetooth adapter in a raspberry pi or intel motherboard will satisfy this. It should also work with ESPHome blue repeaters if they are configured something like this:

esp32_ble_tracker:
  scan_parameters:
    active: true

bluetooth_proxy:
  active: true
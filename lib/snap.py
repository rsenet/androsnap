#!/usr/bin/env python3
import adbutils
import json
import csv


def get_connected_devices():
    """Return all connected devices
    """
    adb = adbutils.AdbClient(host="127.0.0.1", port=5037)

    return adb


def display_connected_device():
    """Display all connected devices
    """
    adb = get_connected_devices()

    for device in adb.devices():
        print(" - %s" % device.serial)


def check_device_exists(device):
    """Check if the specified device truly exists

    :param device: Device to audit
    """
    checked = False

    for element in get_connected_devices().device_list():
        if device in str(element):
            checked = True

    return checked


def show_device_info(device):
    """Display information regarding the device

    :param device: Device to audit
    """
    adb = get_connected_devices()
    d = adb.device(serial=device)

    print("[x] Getting information on %s - %s (%s)" % (device, d.prop.device, d.prop.model))


def exec_command(device, cmd):
    """Execute a specific command on the specified device

    :param device: Device to audit
    :param cmd: Commande to execute
    """
    adb = get_connected_devices()
    d = adb.device(serial=device)

    return d.shell(cmd)


def get_conf(device, category):
    """Execute a specific command on the specified device

    :param device: Device to audit
    :param category: Specific category (secure or global)
    """

    parser = open("settings.json", "r").read()
    conf_dict = json.loads(parser)

    # Open CSV file
    filename = "AndroSNAP-%s.csv" % device
    with open(filename, "a", newline="") as csvfile:
        for conf_info in conf_dict[category]:
            # Execute command
            result = exec_command(device, "settings get %s %s" % (category, conf_info["name"]))

            # Integrate result in CSV file
            androsnap_file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            androsnap_file.writerow([conf_info["description"],
                                     category,
                                     conf_info["name"],
                                     result,
                                     conf_info["expected"]
                                     ])

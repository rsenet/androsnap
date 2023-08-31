#!/usr/bin/env python3
from lib import snap
import argparse
import sys
import csv

__author__  = 'Regis SENET'
__email__   = 'regis.senet@orhus.fr'
__git__     = 'https://github.com/rsenet/androsnap'
__version__ = '0.1'
__license__ = 'GPLv3'
__pyver__   = '%d.%d.%d' % sys.version_info[0:3]
short_desc  = "Android Configuration Checker"

arg_parser = argparse.ArgumentParser(description=short_desc)
arg_parser.add_argument('--device', help="Specify the device to audit ")
u_args = arg_parser.parse_args()
device = u_args.device

if not u_args.device:
    print("[x] Please specify the device to audit (--device)")
    snap.display_connected_device()

else:
    if snap.check_device_exists(device):
        # Create CSV file
        filename = "AndroSNAP-%s.csv" % device

        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Description", "Category", "Command" ,"Current Configuration", "Secure Configuration"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        # Get device info
        snap.show_device_info(device)

        # Get information on the secure settings
        print("[-] Grabbing Secure Settings")
        snap.get_conf(device, "secure")

        # Get information on the global settings
        print("[-] Grabbing Global Settings")
        snap.get_conf(device, "global")

    else:
        print("[x] Device does not exists - Leaving")

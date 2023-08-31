# About AndroSNAP

**androSNAP** was written in order to help any security auditor to perform a configuration audit on an Android Phone

## Usage

Print the help to get all necessary information

```bash
$ python3 androSNAP.py -h
usage: androSNAP.py [-h] [--device DEVICE]

Android Configuration Checker

options:
  -h, --help       show this help message and exit
  --device DEVICE  Specify the device to audit
```

You just have to specify the device to connect:

```bash
$ python3 androSNAP.py --device 192.168.57.114:5555
[x] Getting information on 192.168.57.114:5555 - vbox86p (Samsung Galaxy S7)
[-] Grabbing Secure Settings
[-] Grabbing Global Settings
```


## Enable USB-Debugging

### Via GUI:

Go to **Settings** > **About phone** and press on **build number** 7 times to enable developper mode.

Once enabled, go to **Settings** > **Developer options** and enable **USB debugging**


### Via ADB:

```bash
adb shell settings put global development_settings_enabled 1
adb shell setprop persist.service.adb.enable 1
```


## Author

Régis SENET ([rsenet](https://github.com/rsenet))


## Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/rsenet/androsnap).


## License

The project is available as open source under the terms of the [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

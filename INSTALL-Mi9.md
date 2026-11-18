# Install BlueOS 0.9.0 on Xiaomi Mi 9 Transparent Edition

**English** | [Русский](https://github.com/GDmio/BlueOS/blob/main/INSTALL-Mi9.ru.md)

This test build targets the Xiaomi Mi 9 Transparent Edition (`cepheus`). The signed OTA and recovery passed package checks. First boot and hardware still need testing on the phone. Google Play is included.

## Before you start

- Back up your files, chats and two-factor codes. Unlocking the bootloader and formatting in Recovery erase your data. Keep the bootloader unlocked while using BlueOS.
- For the Chinese Transparent Edition, prepare an unlocked bootloader and stock MIUI 12.5 Android 11 firmware `V12.5.6.0.RFACNXM`. Skip the stock firmware step if that base is already installed. [Mi 9 firmware reference](https://www.crdroid.net/cepheus/12/install)
- Install [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools). Download `BlueOS-0.9.0-cepheus-20261117.zip`, `recovery.img`, `dtbo.img`, `vbmeta.img` and `SHA256SUMS` from the [same release](https://github.com/GDmio/BlueOS/releases/tag/v0.9.0-cepheus). Check each file against `SHA256SUMS` with `sha256sum -c SHA256SUMS` on Linux or `Get-FileHash -Algorithm SHA256` in PowerShell.

## Clean installation

1. Enter Fastboot with Power + Volume Down from a powered-off phone. Connect it and run `fastboot getvar product`. Proceed only if the product is `cepheus`.
2. Run `fastboot flash recovery recovery.img`. If it succeeds, boot straight into Recovery with Power + Volume Up. Release Power at the logo and keep holding Volume Up until Recovery opens.
3. Select **Factory reset → Format data / factory reset** and confirm.
4. Choose **Apply update → Apply from ADB** and run `adb -d sideload BlueOS-0.9.0-cepheus-20261117.zip`. Wait for Recovery to report success, then choose **Reboot system now**.

The OTA initializes the dynamic partition layout and writes its own `dtbo` and `vbmeta`. For this clean install, the only image flashed through Fastboot is `recovery.img`.

If ADB stops near 47%, use the status on the phone to confirm whether the installation succeeded. If you hit an error, save the message from Recovery and [report it](https://github.com/GDmio/BlueOS/issues).

[BlueOS by GDmio](https://github.com/GDmio/BlueOS)

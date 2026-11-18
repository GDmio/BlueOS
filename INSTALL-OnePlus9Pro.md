# Install BlueOS 0.9.0 on OnePlus 9 Pro

**English** | [Русский](https://github.com/GDmio/BlueOS/blob/main/INSTALL-OnePlus9Pro.ru.md)

This test build targets the OnePlus 9 Pro (`lemonadep`). The signed A/B OTA and matching images passed package checks. First boot and hardware still need testing on the phone. Google Play is included.

## Before you start

- Back up your files, chats and two-factor codes. Unlocking the bootloader and formatting in Recovery erase your data. Keep the bootloader unlocked while using BlueOS.
- Check the model number. Use stock Android 13 or 14 firmware for your model and region. The Chinese model uses ColorOS. Follow the appropriate LineageOS guide for the stock firmware and bootloader requirements. [LE2120, LE2121, LE2123, LE2125](https://wiki.lineageos.org/devices/lemonadep/install/variant1/) · [LE2127 (T-Mobile)](https://wiki.lineageos.org/devices/lemonadep/install/variant2/)
- Install [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools). Download `BlueOS-0.9.0-lemonadep-20261118.zip`, `boot.img`, `dtbo.img`, `vbmeta.img`, `vendor_boot.img` and `SHA256SUMS` from the [same release](https://github.com/GDmio/BlueOS/releases/tag/v0.9.0-lemonadep). Check each file against `SHA256SUMS` with `sha256sum -c SHA256SUMS` on Linux or `Get-FileHash -Algorithm SHA256` in PowerShell.

## Clean installation

1. If the bootloader is locked, enable **OEM unlocking** on LE2120, LE2121, LE2123 and LE2125 if available. Power off and hold both volume buttons and Power to enter Fastboot. Run `fastboot devices`, then `fastboot oem unlock` and confirm on the phone. For LE2127, use the [T-Mobile unlock procedure](https://wiki.lineageos.org/devices/lemonadep/install/variant2/#unlocking-the-bootloader).
2. Return to Fastboot and open the terminal in the download folder. Run these commands in order and stop if any command fails.

   ```sh
   fastboot flash dtbo dtbo.img
   fastboot flash vbmeta vbmeta.img
   fastboot flash vendor_boot vendor_boot.img
   fastboot reboot bootloader
   ```

3. Wait for Fastboot to return, then run `fastboot flash boot boot.img`. Select **Recovery mode** on the phone.
4. Select **Factory reset → Format data / factory reset** in Recovery and confirm. Choose **Apply update → Apply from ADB** and run `adb -d sideload BlueOS-0.9.0-lemonadep-20261118.zip`. Wait for Recovery to report success, then choose **Reboot system now**.

If ADB stops near 47%, use the status on the phone to confirm whether the installation succeeded. If you hit an error, save the message from Recovery and [report it](https://github.com/GDmio/BlueOS/issues).

[BlueOS by GDmio](https://github.com/GDmio/BlueOS)

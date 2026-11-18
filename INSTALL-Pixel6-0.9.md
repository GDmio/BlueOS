# Install BlueOS 0.9.0 on Google Pixel 6

**English** | [Русский](https://github.com/GDmio/BlueOS/blob/main/INSTALL-Pixel6-0.9.ru.md)

Use these files on the Google Pixel 6 (`oriole`). The signed OTA and its recovery images passed package checks. First boot and the upgrade path from 0.8.1 still need testing on a Pixel 6. Google Play is included.

## Before you start

- Back up your files, chats and two-factor codes. Unlocking the bootloader and formatting in Recovery erase your data. Keep the bootloader unlocked while using BlueOS.
- Before a clean install, use the latest stock Android 17 firmware available for Pixel 6 and verify that calls and SMS work. [Pixel 6 firmware requirements](https://wiki.lineageos.org/devices/oriole/install/#checking-the-correct-firmware)
- Install [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools). Download `BlueOS-0.9.0-oriole-20261117.zip`, `boot.img`, `dtbo.img`, `vendor_boot.img` and `SHA256SUMS` from the [same release](https://github.com/GDmio/BlueOS/releases/tag/v0.9.0-oriole). Check each file against `SHA256SUMS` with `sha256sum -c SHA256SUMS` on Linux or `Get-FileHash -Algorithm SHA256` in PowerShell.

## Clean installation

1. If the bootloader is locked, enable **OEM unlocking** and **USB debugging**. Enter Fastboot with Volume Down + Power from a powered-off phone. Run `fastboot devices`, then `fastboot flashing unlock` and confirm on the phone. Return to Fastboot after the reset.
2. With the phone in Fastboot and the terminal open in the download folder, run the following commands in order. Wait for Fastboot to return after the reboot. Stop if a command fails.

   ```sh
   fastboot flash boot boot.img
   fastboot flash dtbo dtbo.img
   fastboot reboot bootloader
   fastboot flash vendor_boot vendor_boot.img
   ```

3. Select **Recovery mode** on the phone. In BlueOS Recovery, select **Factory reset → Format data / factory reset** and confirm.
4. Choose **Apply update → Apply from ADB** and run `adb -d sideload BlueOS-0.9.0-oriole-20261117.zip`. Check that Recovery reports a successful installation. If prompted to install add-ons, choose **No**. Select **Reboot system now**.

If ADB stops near 47%, use the status on the phone to confirm whether the installation succeeded. If you hit an error, save the message from Recovery and [report it](https://github.com/GDmio/BlueOS/issues).

Earlier device-tested build: [BlueOS 0.8.1 for Pixel 6](https://github.com/GDmio/BlueOS/releases/tag/v0.8.1-oriole).

[BlueOS by GDmio](https://github.com/GDmio/BlueOS)

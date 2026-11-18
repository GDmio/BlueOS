# Тестовая BlueOS для OnePlus 9 Pro

[English](https://github.com/GDmio/BlueOS/blob/main/INSTALL-OnePlus9Pro.md) | **Русский**

Это инструкция по чистой установке BlueOS на OnePlus 9 Pro (`lemonadep`). Загрузку этой сборки на телефоне ещё предстоит проверить.

## Подготовка

1. Сделайте резервную копию на ПК или в облаке. Разблокировка загрузчика и форматирование в Recovery стирают приложения и файлы в памяти телефона.
2. Сверьте заводскую модель. Для LE2120, LE2121, LE2123 и LE2125 действует обычная инструкция LineageOS. Для LE2127 (T-Mobile) предусмотрена отдельная процедура разблокировки. [LE2120, LE2121, LE2123, LE2125](https://wiki.lineageos.org/devices/lemonadep/install/variant1/) · [LE2127 (T-Mobile)](https://wiki.lineageos.org/devices/lemonadep/install/variant2/)
3. Для первой установки нужна прошивка от штатной системы на Android 13 или 14 для вашей модели и региона. На китайской версии штатная система называется ColorOS. Если у вас уже стоит подходящая заводская версия, переходите к следующему шагу. Если версия прошивки неизвестна, сверьтесь с инструкцией LineageOS для своей модели. [OnePlus 9 Pro для Китая](https://www.oneplus.com/cn/9-pro/specs)
4. Установите Android Platform-Tools на ПК и добавьте папку `platform-tools` в `PATH`, чтобы команды `adb` и `fastboot` были доступны из папки с комплектом. [Загрузка Platform-Tools](https://developer.android.com/tools/releases/platform-tools)

## Разблокировка загрузчика

Если загрузчик уже разблокирован, переходите к установке. Для LE2120, LE2121, LE2123 и LE2125 включите «Заводскую разблокировку» в параметрах разработчика, если переключатель доступен. Выключите телефон и зажмите обе кнопки громкости и питание, чтобы войти в Fastboot. Подключите телефон по USB. Когда `fastboot devices` покажет устройство, выполните `fastboot oem unlock` и подтвердите разблокировку на экране телефона.

Для **LE2127 (T-Mobile)** выполните процедуру разблокировки для операторской версии. [Инструкция LineageOS для LE2127](https://wiki.lineageos.org/devices/lemonadep/install/variant2/#unlocking-the-bootloader)

## Установка

1. Войдите в Fastboot, подключите телефон по USB и откройте терминал в папке с комплектом. Убедитесь, что `fastboot devices` показывает телефон. Запишите образы из этого комплекта. Если команда вернула ошибку, остановитесь на этом шаге.

   ```sh
   fastboot flash dtbo dtbo.img
   fastboot flash vbmeta vbmeta.img
   fastboot flash vendor_boot vendor_boot.img
   fastboot reboot bootloader
   ```

2. Дождитесь возвращения телефона в Fastboot, затем запишите `boot.img`, необходимый для запуска Recovery.

   ```sh
   fastboot flash boot boot.img
   ```

3. Кнопками громкости выберите **Recovery mode** в меню загрузчика и подтвердите кнопкой питания. В Recovery выберите **Factory reset → Format data / factory reset** и подтвердите удаление данных.
4. В главном меню Recovery выберите **Apply update → Apply from ADB** и выполните на ПК `adb -d sideload BlueOS-0.9.0-lemonadep-20261118.zip`. Проверяйте результат на экране телефона. Индикатор ADB на ПК иногда останавливается на 47% даже при успешной установке. Когда Recovery подтвердит успех, выберите **Reboot system now**.
5. После первой загрузки проверьте звонки, мобильный интернет, Wi-Fi, Bluetooth, камеры, звук и отпечаток пальца. Google Play уже входит в сборку.

Контрольные суммы ZIP и образов перечислены в `SHA256SUMS`. Комплект основан на [BlueOS by GDmio](https://github.com/GDmio/BlueOS).

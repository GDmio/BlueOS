# BlueOS 0.9.0 для Xiaomi Mi 9 Transparent Edition

[English](https://github.com/GDmio/BlueOS/blob/main/INSTALL-Mi9.md) | **Русский**

Это тестовая сборка на Android 17 для Xiaomi Mi 9 с кодовым именем `cepheus`. Google Play уже включён. ZIP и образы проверены на компьютере. Первую загрузку и работу оборудования нужно проверить на телефоне.

## Перед установкой

- Сохраните файлы, переписки и коды двухфакторной защиты. Разблокировка загрузчика и форматирование удаляют пользовательские данные.
- Подготовьте разблокированный загрузчик и актуальную базовую прошивку MIUI 12.5 на Android 11 для исходного региона устройства. Для китайской Transparent Edition используйте базу `V12.5.6.0.RFACNXM`. Если эта версия уже установлена, повторно ставить её не нужно. [Справка по прошивке Mi 9](https://www.crdroid.net/cepheus/12/install)
- Установите [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools). Скачайте ZIP и `recovery.img` из одного комплекта и сравните их SHA-256 с файлом `SHA256SUMS`. В Windows используйте `Get-FileHash -Algorithm SHA256`.

## Чистая установка

1. Загрузитесь в Fastboot, удерживая питание и уменьшение громкости. Подключите USB и выполните `fastboot getvar product`. Продолжайте, если команда вернула `cepheus`.
2. Выполните `fastboot flash recovery recovery.img`. Сразу загрузитесь в Recovery, удерживая питание и увеличение громкости. После появления логотипа отпустите питание и держите увеличение громкости до меню Recovery.
3. В Recovery выберите **Factory reset → Format data / factory reset**. Этот шаг удаляет приложения и пользовательские файлы.
4. Выберите **Apply update → Apply from ADB**. На компьютере выполните:

   ```sh
   adb sideload BlueOS-0.9.0-cepheus-20261117.zip
   ```

5. Дождитесь сообщения об успешной установке в Recovery. Выберите **Reboot system now**.

ZIP создаёт разметку динамических разделов и записывает `dtbo` и `vbmeta`. Через Fastboot для этой установки прошивается только `recovery.img`.

Для первого теста проверьте звонки и мобильные данные, Wi-Fi, Bluetooth, все камеры, экранный отпечаток, NFC, звук и беспроводную зарядку. Если установка прервалась, сохраните текст ошибки из Recovery.

BlueOS by GDmio. [Репозиторий проекта](https://github.com/GDmio/BlueOS)

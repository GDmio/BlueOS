# Установка готовой BlueOS на Google Pixel 6

[English](https://github.com/GDmio/BlueOS/blob/main/INSTALL-Pixel6-0.9.md) | **Русский**

Эта инструкция и этот zip — только для **Pixel 6** (кодовое имя `oriole`), сборка BlueOS 0.9.0 из этого комплекта. Для каждой модели скачивайте её собственную сборку. Для Pixel 6 Pro —
[INSTALL-Pixel6Pro.ru.md](https://github.com/GDmio/BlueOS/blob/main/INSTALL-Pixel6Pro.ru.md), для Pixel 6a — [INSTALL.ru.md](https://github.com/GDmio/BlueOS/blob/main/INSTALL.ru.md).

Сборка 0.9.0 прошла проверки на компьютере. Загрузку и работу на Pixel 6 ещё предстоит проверить.

## ⚠️ Прочитайте до начала
- **Неофициальная фанатская прошивка, без каких-либо гарантий.** Всё, что вы делаете с телефоном, — на ваш страх и
  риск. Это не сборка LineageOS: об ошибках BlueOS не пишите в LineageOS, пишите сюда (Issues).
- **Все данные на телефоне сотрутся** — при разблокировке загрузчика и ещё раз при установке. Сохраните фото,
  переписки, **коды двухфакторной защиты** (Google Authenticator и т. п.) заранее. Удалите с телефона аккаунт Google,
  чтобы после сброса он не спрашивал старый.
- **Загрузчик останется разблокированным.** При каждом включении телефон покажет предупреждение об этом — так и
  должно быть. **Не блокируйте загрузчик, пока стоит BlueOS**: телефон перестанет загружаться.
- **Некоторые приложения могут не работать:** оплата телефоном (Google Wallet), часть банковских приложений и игр.
- **Персонажа и звуков из Blue Archive в этой сборке нет.** Файлы игры можно добавить
  прямо на телефоне: «Обои и стиль» → «Персонаж» → «Добавить файлы персонажа» ([ASSETS.ru.md](https://github.com/GDmio/BlueOS/blob/main/ASSETS.ru.md)). Где их взять: в постах Telegram-канала BlueOS —
  [t.me/BlueOSfirmware](https://t.me/BlueOSfirmware), или собрать самому из файлов игры.
- **Google Play внутри** (MindTheGapps).
- Телефон, купленный у оператора с блокировкой, загрузчик не разблокирует — тогда установить нельзя.

## Что скачать
| Файл | Зачем |
|---|---|
| `BlueOS-0.9.0-oriole-20261117.zip` | прошивка для установки через ADB sideload |
| `boot.img`, `dtbo.img`, `vendor_boot.img` | для первой установки: загрузочный раздел и recovery BlueOS |
| `SHA256SUMS` | контрольные суммы — проверить, что файлы скачались целиком |

Проверка: Windows (PowerShell) — `Get-FileHash .\BlueOS-0.9.0-oriole-20261117.zip`, Linux/macOS — `sha256sum -c SHA256SUMS`.
Суммы должны совпасть. Не совпали — скачайте заново, не прошивайте.

## Перед началом
- Обновите стоковую прошивку до **последней заводской версии Android 17 для Pixel 6**. [Требования к заводской прошивке](https://wiki.lineageos.org/devices/oriole/install/#checking-the-correct-firmware)
- Проверьте, что на стоковой прошивке работают звонки и SMS.
- Компьютер, кабель USB и [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools)
  (`adb` и `fastboot`). На Windows ещё [Google USB Driver](https://developer.android.com/studio/run/win-usb).
- Зарядите телефон хотя бы до 50 %.

## 1. Разблокировать загрузчик (один раз)
1. «Настройки» → «О телефоне» → 7 раз нажать «Номер сборки» — включится режим разработчика.
2. «Настройки» → «Система» → «Для разработчиков»: включить **«Заводская разблокировка»** и **«Отладка по USB»**.
3. Подключить к компьютеру, разрешить отладку на телефоне. В папке platform-tools:
```
adb reboot bootloader
fastboot flashing unlock
```
4. На телефоне кнопками громкости выбрать «Unlock the bootloader», подтвердить кнопкой питания. Телефон сотрётся.
   После загрузки снова включите «Отладку по USB».

## 2. Поставить recovery BlueOS
```
adb reboot bootloader
fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot reboot bootloader
fastboot flash vendor_boot vendor_boot.img
```
Затем кнопками громкости выбрать **Recovery mode** и нажать питание — откроется recovery BlueOS (логотип с нимбом).
Если логотипа BlueOS нет, дальше не идите.

## 3. Установить BlueOS
1. В recovery: **Factory reset → Format data / factory reset** → подтвердить.
2. Назад → **Apply update → Apply from ADB**.
3. На компьютере:
```
adb sideload BlueOS-0.9.0-oriole-20261117.zip
```
   ADB может остановиться на 47 %. Продолжайте, если Recovery подтвердил успешную установку.
4. Если recovery спросит про перезагрузку для дополнений — «No», Google Play уже внутри.
5. **Reboot system now.** Первая загрузка — несколько минут.

## Обновления
Для обновления BlueOS на Pixel 6 используется recovery → Apply update → Apply from ADB →
`adb sideload BlueOS-0.9.0-oriole-20261117.zip`. Переход с 0.8.1 без сброса ещё не проверен на телефоне. Перед тестом сохраните данные.

## Если что-то пошло не так
- Не загружается дальше логотипа больше 10 минут — зайдите в recovery (питание + громкость вниз, затем Recovery mode),
  сделайте Format data и поставьте zip ещё раз.
- **Вернуть стоковую прошивку:** [flash.android.com](https://flash.android.com) (Chrome или Edge). Данные сотрутся.
  Загрузчик блокируйте только после возврата на стоковую прошивку.
- Нашли ошибку — откройте Issue: что делали, что увидели, лучше со скриншотом.

# INT-16 test task 2
**Второе** тестовое задание в отдел INT-16
"Группа конкурентного анализа. Application Security" в рамках 2-го этапа стажировки
2023.2 PT-START Intensive.

Задание выполнено на основе данного [технического задания](https://sadykov.notion.site/INT-16-cb90ea1eaf8c41bcab92e6258a2d8499).

## Requirements
Скрипт тестировался на версии Python 3.10. Также необходимо установить [Docker](https://www.docker.com/) и
[OWASP ZAP](https://www.zaproxy.org/).

## Getting Started
Для начала нужно запустить [OWASP Juice Shop](https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html)
в docker контейнере при помощи команды:
```bash
make shop
```
Затем нужно запустить сканирование уязвимостей запущенного выше веб-приложения с помощью [OWASP ZAP](https://www.zaproxy.org/)
командой:
```bash
make zap
```
Финально необходимо запустить скрипт `main.py` для конвертации репорта об уязвимостях, сгенерированного командой выше, в
формат согласно техническому заданию при помощи команды:
```bash
make convert
```
Вышеперечисленные шаги можно выполнить все вместе данной командой:
```bash
make
```

## Additional Information
В `Makefile` можно регулировать следующие параметры при помощи переменных окружения:
- `CONT_NAME` - имя контейнера, в котором запускается [OWASP Juice Shop](https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html)
- `ZAP_REPORT_PATH` - путь до `json` файла с отчетом об уязвимостях от [OWASP ZAP](https://www.zaproxy.org/)
- `RESULT_REPORT_PATH` - путь до `json` файла финального репорта в требуемом формате
# Fuzzy Matcher

## Requirements

- python3
- pandas
- openpyxl
- ensure that python3 is in your **PATH variable**
- xclip / xcel if your os is GNU Linux

## How to

1. edit [voc.xlsx](./voc.xlsx), first column is search column, second column is return column
2. copy cour list to clipboard
3. run [run.bat](./run.bat) if you are windows user or just [match.py](./match.py) in other cases
4. script will update your clipboard with closest matches

Using my example [voc.xlsx](./voc.xlsx) on following input:

```
москва
Питер
казань
```

you'll get the following output:

```
Москва
Санкт-Петербург
Республика Татарстан
```
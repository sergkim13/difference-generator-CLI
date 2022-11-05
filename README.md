# Difference generator CLI

### Hexlet tests and linter status:
[![Actions Status](https://github.com/sergkim13/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/sergkim13/python-project-50/actions)
[![Actions Status](https://github.com/sergkim13/python-project-50/actions/workflows/project_ci.yml/badge.svg)](https://github.com/sergkim13/python-project-50/actions/workflows/project_ci.yml)[![Maintainability](https://api.codeclimate.com/v1/badges/4b548ad9dd2986338109/maintainability)](https://codeclimate.com/github/sergkim13/python-project-50/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/4b548ad9dd2986338109/test_coverage)](https://codeclimate.com/github/sergkim13/python-project-50/test_coverage)


### Installation
1. Make sure you have Poetry installed on your computer.
If you have not, type:
```curl -sSL https://install.python-poetry.org | python3 -``` (works for Linux, macOS, Windows (WSL))
See https://python-poetry.org/docs/ for more info about Poetry.
2. Clone repository:
``$ git clone https://github.com/sergkim13/python-project-50.git``
2. Type: 
```make install-gendiff```


### Description:
This CLI-utility compares two ```JSON``` or ```YAML``` files and shows a difference. You can set a format of output: 'stylish' mode (set by default) , 'plain' mode or 'json' mode.
Input "gendiff -h" for more information.
______________
### Описание:
Данная консольная утилита сравнивает между собой два файла формата ```JSON``` или ```YAML``` и показывает разницу между ними. Вы можете настроить формат вывода результата: 'stylish' (выбран по умолчанию), 'plain' или 'json'.
Наберите "gendiff -h", чтобы узнать больше.

### Manual:
**To compare files in the terminal, type:**  
>```$ gendiff <path1>  <path2>```

1. -**h, --help** - ```$ gendif -h``` - shows a guide;
2. **-f, --format** - ```$ gendif -f``` - allows you to select the format of the 
difference output. **Available formats:**
  
   1. `-f stylish`- default form. Example output:
  
   >{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }
    2. `-f plain`. Example output:  
  
    > Property 'common.follow' was added with value: false  
    Property 'common.setting2' was removed  
    Property 'common.setting3' was updated. From true to [complex value]  
    Property 'common.setting4' was added with value: 'blah blah'
    3. `-f json`. Returns the difference in json format.
  
    >{"-follow": false, "=host": "hexlet.io", "-proxy": "123.234.53.22", "-timeout": 50, "+timeout": 20, "+verbose": true}
______________
### Инструкция

**Чтобы сравнить два файла, наберите в консоли:**  
>```$ gendiff <путь_к_файлу_1>  <путь_к_файлу_2>```

1. -**h, --help** - ```$ gendif -h``` - вывод справочной информации;
2. **-f, --format** - ```$ gendif -f``` - позволяет выбрать формат формат вывода. **Available formats:**
  
   1. `-f stylish`- по умолчанию. Пример:
  
   >{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }
    2. `-f plain`. Пример:  
  
    > Property 'common.follow' was added with value: false  
    Property 'common.setting2' was removed  
    Property 'common.setting3' was updated. From true to [complex value]  
    Property 'common.setting4' was added with value: 'blah blah'
    3. `-f json`. Возвращает результат в формате '''json'''.
  
    >{"-follow": false, "=host": "hexlet.io", "-proxy": "123.234.53.22", "-timeout": 50, "+timeout": 20, "+verbose": true}

#### Demo in 'stylish' mode.
[![asciicast](https://asciinema.org/a/Q6PH9m3bcVfdljH6yPOqRNnq7.svg)](https://asciinema.org/a/Q6PH9m3bcVfdljH6yPOqRNnq7)

#### Demo in 'plain' mode.
[![asciicast](https://asciinema.org/a/TZc0azdhkC8ruBZH5mKyuP4IC.svg)](https://asciinema.org/a/TZc0azdhkC8ruBZH5mKyuP4IC)

#### Demo in 'json' mode.
[![asciicast](https://asciinema.org/a/a6u4PCgb7ZzavIvc1natUaHwE.svg)](https://asciinema.org/a/a6u4PCgb7ZzavIvc1natUaHwE)
# What does it do
The script should take the input path to a text file and output to the console ten most popular words in this file in descending order of frequency.

# How to use 
User in function `load_data_from_file(file_path)` enter path to file, these is function reads data from file and `return data_of_file`

then `data_of_file`  pass in function `get_most_frequent_words()`, and after work function, she return ten most popular word  and  their quantity from your text

```python 

get_most_frequent_words(data_of_file)
return ten_elements_of_array_sorted

```
Then `ten_elements_of_array_sorted` pass in function `deduce_frequent_word_and_count(ten_elements_of_array_sorted)`  which deduce words and their quantity in the console 

# For example
User for start need to pass path to directory in which to be script and text for frequency analisys.
In my case this directory is `firstTask`

```bash

>cd C:/Users/User/PycharmProjects/firstTask

```

After user will need to enter in console first parameter it is interpreter `python`, then name of script, then name of file with text 

In my case: name of script `coolprogram.py`, name of file with text `test.txt`

Data is in `test.txt`:

```
А вы знаете самые частые слова в русском языке? Это "и", "в" и "не". Остальных можно посмотреть на википедии.

В этой задаче нужно написать скрипт, который составит такой список для любого текста, поданного на вход.

Скрипт должен принимать на вход путь до текстового файла и выводить в консоль десять самых популярных слов в этом файле в порядке убывания частоты.

Потом можно попробовать скормить ему разные тексты. "Война и мир". Всю Википедию. Кстати, такой скрипт должен нормально работать не только с русским, но и с другими языками.

```
Start your script

```bash

>cd C:/Users/User/PycharmProjects/firstTask
>python coolprogram.py test.txt
в 5
и 5
на 3
не 2
можно 2
скрипт 2
такой 2
вход 2
должен 2
с 2

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

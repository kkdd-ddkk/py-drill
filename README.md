# Small handy language drilling tool inspired by org-drill

## Usage

First make a csv-style with combinations, for example:
```csv
I live in Granada.;Yo vivo en Granada
I live in Granada, {a city}.;Yo vivo en Granada, {una ciudad}
I live in Granada, a city {that has monuments}.;Yo vivo en Granada, una ciudad {que tiene monumentos}
I live in Granada, a city that has {very important} monuments.;Yo vivo en Granada, una ciudad que tiene monumentos {muy importantes}
```

Combinations may have an increasing complexity, to softly walk you through a difficult grammar structure.

Then call the `py-drill`:
```batch
py-drill.py   mi-casa.csv
```

It will walk you sequentially though the CSV lines, higlighting the words inside braces with color, showing the first csv column element first, and then if you hit `enter` - the second one.

## Example
![image](https://github.com/kkdd-ddkk/py-drill/assets/58269091/482f19e9-42ac-474e-a735-71db3ef42e3c)

*press enter*

![image](https://github.com/kkdd-ddkk/py-drill/assets/58269091/855acd55-6963-463b-8731-e623f6a9032f)


# Features

- No statistics is collected
- Input - a csv format
- Сan highlight words by using curly braces like this `{highlight me}`.




## Controls:
- Arrow keys - go to the next/previous phrase
- `j` - jump to a random phrase
- `enter` - show translation, move to the next phrase
- `backspace` - hide the translation





# To register a new extension handler in Windows

As administrator:
```batch
assoc .pydrill=Python.Drill

ftype Python.Drill="C:\Windows\py.exe" -3  path\to\py-drill.py  %1 %2
```

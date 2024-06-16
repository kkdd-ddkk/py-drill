# Small handy language drilling tool inspired by org-drill
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

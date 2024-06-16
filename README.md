- No statistics is collected
- Input - a csv format
- Сan highlight words by using /.../.

# To register a new extension handler in Windows

As administrator:
```batch
assoc .pydrill=Python.Drill

ftype Python.Drill="C:\Windows\py.exe" -3  path\to\py-drill.py  %1 %2
```

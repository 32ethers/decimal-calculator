# README

An high-precision command-line calculator. 

## install 

```bash
uv venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

uv pip install . 
```

or

```bash
pip install -r requirements.txt
```

## usage

```bash
uv run main.py

# or

python main.py
```

Then enter a mathematical expression calculate, 

```
An unsafe high-precision command-line calculator. Please enter a mathematical expression.
$ > 1+3
4
$ > 6*4
24
$ > (64**2 + 3)/2
2049.5
$ > 
```

If you want to use the last result, use _

```
$ > 3+4
7
$ > _ + 3
10
$ >  
```

Various is also supported

```
$ > a = 6, b = 2
a = 6
b = 2

$ > a + b
8
$ > b**3
8
$ > 
```
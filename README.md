# README

An high-precision command-line calculator. 

It will replace all input number to decimal to calculate more precisely than float, which is very helpful in calculate uint256 and decimals on ethereum.

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

If you want to change precision, use parameter -p

```bash
python main.py -p 50
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
```

If you want to use the last result, use _

```
$ > 3+4
7
$ > _ + 3
10
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
```

Since number is converted to Decimal, so functions of Decimal class can be called

```
$ > 5 + 4.sqrt()
7
```



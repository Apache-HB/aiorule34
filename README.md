# aiorule34

## Installation

pip install aiorule34

## Usage
```
from aiorule34 import rule34get as r34get

ret = await r34get('1girl')

for post in ret:
	print(post.url)
```
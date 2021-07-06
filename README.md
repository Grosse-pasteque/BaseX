# BaseX - EnD [0.5.0]

## By Grosse pastèque#6705


-------------


### Confifuration:

```py
config = {
	loop: base,
	loop: base
}
```

-> `Base` that is equivalent to the base type that you want to use.
-> `Loop` that is equivalent to the number of loop that you want the encode or decode to.
-> `Base` can be: 16, 32, 64, 85


-------------


### Full Code:

```py
import BaseX

config = {
	2: 64,
	3: 32
}

encrypted = BaseX.encrypt(b"hello", config)
decrypted = BaseX.decrypt(encrypted, config)

print(encrypted)
#	b'JJJEIRKXKYZEUS2ZLJKUSURSJNEVUQ2WINLEEU2JKZCFKQ2OKNJEQVJWKQZFASJ5'

print(decrypted)
#	b'hello'
```

**IMPORTANT NOTE: *This encryption method is not very powerfull if your turn number is low, you should have at list __40 turns minimum !__***
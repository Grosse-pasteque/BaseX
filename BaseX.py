import base64


def encrypt(value: bytes, config: dict) -> bytes:	

	for loop, base in config.items():
		if base not in [16, 32, 64, 85]:
			raise ValueError(
				f"base {base} not in [16, 32, 64, 85]")

		for i in range(loop):

			value = eval(f"base64.b{base}encode({value!r})")
	
	return value


def decrypt(value: bytes, config: dict) -> bytes:
	
	keys = list(config.keys())
	keys.reverse()

	values = list(config.values())
	values.reverse()

	_config = {keys[i]: values[i] for i in range(len(config))}

	for loop, base in _config.items():
	
		if base not in [16, 32, 64, 85]:
			raise ValueError(
				f"base {base} not in [16, 32, 64, 85]")

		for i in range(loop):

			value = eval(f"base64.b{base}decode({value!r})")

	return value

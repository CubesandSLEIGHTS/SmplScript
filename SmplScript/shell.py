import SmplScript.SmplScript as smpl
from termcolor import cprint as c

while True:
	text = input('Smpl > ')
	result, error = smpl.run('<stdin>', text)

	if error: c(error.as_string(), 'red')
	else: print(repr(result))
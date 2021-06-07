from SmplScript.Run.Run import run
from termcolor import cprint as c

while True:
	text = input('Smpl > ')
	if text.strip() == "": continue
	result, error = run('<stdin>', text)

	if error:
		c(error.as_string(), 'red')
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
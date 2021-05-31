import SmplScript as smpl

while True:
    text = input('Smpl > ')
    result, error = smpl.run(text)

    if error: print(error.as_string())
    else: print(result)
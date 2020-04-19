def read(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def write(path, contents):
	with open(path, 'w') as f:
		f.write(contents)
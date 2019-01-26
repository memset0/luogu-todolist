import spider

def read(path):
	f = open(path, 'r+')
	t = f.read()
	f.close()
	return t

def index():
	text = read('web/index.html')
	info = spider.update()
	info['table main'] = read('web/table.html')
	for key, val in info.items():
		text = text.replace('{{ %s }}' % key, str(val))
	return text
import spider

def readFile(path):
	file = open(path, 'r+', encoding='utf8')
	text = file.read()
	file.close()
	return text

def index():
	text = readFile('web/index.html')
	info = spider.update()
	info['table main'] = readFile('web/table.html')
	for key, val in info.items():
		text = text.replace('{{ %s }}' % key, str(val))
	return text
import yaml, re, requests

cookies = headers = {}

def readFile(path):
	file = open(path, 'r+', encoding='utf8')
	text = file.read()
	file.close()
	return text

def getTitle(prob):
	global titleList
	try:
		return titleList[prob]
	except:
		if titleList == None:
			titleList = {}
		url = 'https://www.luogu.org/problemnew/show/{prob}'.format(prob=prob)
		text = requests.get(url, cookies=cookies, headers=headers).text
		title = text.split('<title> {prob} '.format(prob=prob))[1].split(' - 洛谷</title>')[0]
		titleList[prob] = title
		with open('cache/title.yml', 'a+', encoding='utf8') as file:
			file.write('{prob}: "{title}"\n'.format(prob=prob, title=title))
			file.close()
		return title

def getStatus(status):
	if status:
		return '<span style="color: green">Y</span>'
	else:
		return '<span style="color: red">N</span>'

class Todo:
	def toStr(self):
		return '[{prob}] {status}'.format(prob=self.prob, status=self.status)
	def toTable(self):
		answer = '''
<tr>
	<td><a href="https://www.luogu.org/recordnew/lists?uid={uid}&pid={prob}" class="table-status">{status}</a></td>
	<td><a href="https://www.luogu.org/problemnew/show/{prob}" class="table-link">{prob}</a></td>
	<td><a href="https://www.luogu.org/problemnew/show/{prob}" class="table-link">{title}</a></td>
</tr>
		'''.format(prob=self.prob, status=getStatus(self.status), title=self.title, uid=uid).replace('\n', '').replace('	', '')
		if self.status or 'pass' in self.tags:
			answer = answer.replace('<tr>', '<tr style="background: #cfc;">')
		elif 'warn' in self.tags:
			answer = answer.replace('<tr>', '<tr style="background: #fcc;">')
		return answer
	def addTag(self, tag):
		self.tags.append(tag)
	def __init__(self, prob):
		self.tags    = []
		self.prob   = prob
		self.title  = getTitle(prob)
		self.status = False

def init():
	global uid, config
	config = yaml.load(readFile('config.yml'))
	uid = config['userid']
	headers['referer']     = 'https://www.luogu.org/'
	headers['User-agent']  = 'wxw_ak_ioi'
	cookies['_uid']        = str(config['userid'])
	cookies['__client_id'] = config['clientid']

def getACList():
	text = requests.get('https://www.luogu.org/space/show?uid=%d' % uid, cookies=cookies, headers=headers).text
	text = re.sub(r'<span style="display:none">[\s\S]*?</span>', '', text)
	text = re.sub(r'<h2>尝试过的题目</h2>[\s\S]*?</div>', '', text)
	find = re.findall(r'<a data-pjax href="/problem/show\?pid[\s\S]*?</a>', text)
	prob = []
	for it in find:
		prob.append(it.split('>')[1].split('<')[0])
	return prob

def getTodoList():
	text = readFile('todo.list')
	text = re.sub(r'#[\s\S]*?\n', '', text)
	find = re.split(r'[\s]', text)
	prob = []
	added = []
	for it in find:
		if it == '':
			continue
		if it[0] == '[':
			prob[-1].addTag(it[1:-1])
		elif not it in added:
			prob.append(Todo(it))
			added.append(it)
	return prob

def update():
	global titleList
	titleList = yaml.load(readFile('cache/title.yml'))
	ac_counter    = 0
	total_counter = 0
	ac   = getACList()
	todo = getTodoList()
	tableFile = open('web/table.html', 'w+', encoding='utf8')
	for it in todo:
		total_counter += 1
		it.status = it.prob in ac
		if it.status or 'pass' in it.tags:
			ac_counter += 1
		# print(it.toStr())
		tableFile.write(it.toTable())
	tableFile.close()
	return {
		'ac counter': ac_counter,
		'total counter': total_counter,
	}

init()
update()

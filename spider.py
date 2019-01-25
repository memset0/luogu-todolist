import yaml, re, requests

cookies = headers = {}

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
		with open('cache/title.yml', 'a+') as file:
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
		if self.status:
			answer = answer.replace('<tr>', '<tr style="background: #cfc;">')
		return answer
	def __init__(self, prob):
		self.prob = prob
		self.title = getTitle(prob)
		self.status = False

def init():
	global uid, config
	config = yaml.load(open('config.yml', 'r+').read())
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
	text = open('todo.list', 'r+').read()
	text = re.sub(r'#[\s\S]*?\n', '', text)
	find = re.split(r'[\s]', text)
	prob = []
	for it in find:
		if it != '':
			prob.append(Todo(it))
	return prob

def update():
	global titleList
	titleList = yaml.load(open('cache/title.yml', 'r+').read())
	ac   = getACList()
	todo = getTodoList()
	tableFile = open('web/table.html', 'w+')
	for it in todo:
		it.status = it.prob in ac
		# print(it.toStr())
		tableFile.write(it.toTable())
	tableFile.close()

init()
update()
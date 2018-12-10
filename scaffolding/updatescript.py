import git
	
inputFile = open('queue.txt', 'r+')
repos = inputFile.read().strip().text.split('\n')
inputFile.truncate(0)
inputFile.close()


if len(text) == 0:
	return

github = GITPATH = '/home/logan/projects/%s'
GITURL = 'git@github.com:tuffing/%s.git'


for repo in repos: 
	#update local repo from it's source
	g = git.cmd.Git('/home/logan/projects/%s' % repo)
	g.pull()

	g.push('git@github.com:tuffing/%s.git' % repo)
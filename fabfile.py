import os
from fabric.api import *

root_dir = os.path.dirname(os.path.realpath(__file__))
pj = os.path.join
def publish():
	tgt = os.path.abspath(pj(root_dir, '../leo-editor.github.io/'))
	if not os.path.isdir(tgt):
		print("You need to check out https://github.com/leo-editor/leo-editor.github.io to " + tgt)
		return
	gen_dir = pj(root_dir, 'output')
	with lcd(tgt):
		local("git pull")

	local("cp -rv %s/* %s" % (gen_dir, tgt))
	with lcd(tgt):
		local("git add -A")
		local("git push origin master")










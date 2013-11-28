Elevating user privileges with Leo and Python
---------------------------------------------

:date: 2013-12-01
:tags: Windows, scripts, permissions
:category: scripts
:slug: windows_elevate
:author: Matt Wilkie
:summary: Initiating Windows User Account Control (UAC) from a normal account

#### elevate.py #### 
Open a new python interpreter after asking for elevated UAC permissions, and feed it the python script specified on the command line.
    
    python elevate.py d:\full\path\to\some-script.py {args for some-script}

Registering Leo with Windows
-----------------------------------

:date: 2013-12-01
:tags: Windows, install, scripts
:category: scripts
:slug: register_leo
:author: Matt Wilkie
:summary: Enable 2x-click .leo files in Windows using bazaar, snapshot or portable Leo


_this is documentation work in progress_

Installing Leo using the standard setup program from Sourceforge does nice things like create Start Menu & Desktop shortcuts and enable open Leo files with a simple doubleclick. For those that like to run from source code or a portable drive there are manual instructions for doing the same, but it's fiddly and rapidly gets old. Why repeat when you can automate?

Introducing **register-leo.leox** (and unregister-leo): Creates the necessary Windows registry keys for integration with Explorer and friends. After running this script .leo and .leox files are shown with the Leo icon, and 2x-clicking on them will open them in Leo.

This has the added benefit of removing the need for most to create a batch file and then figure out where in PATH to store it in order to use Leo. As a matter of fact, any .leo file becomes the equivalent of launchLeo.py, just try this:

   %homedrive%\homepath%\workbook.leo x:\path\to\some\other\leofile.leo

To use: open a command shell with administrative rights, and run:

    d:\path\to\python.exe d:\path\to\leo\launchLeo.py e:\path\to\register-leo.leox


All in one step: you can try the `elevate.py` script which will ask for Admin priviliges from a regular command shell:

    d:\path\to\python.exe d:\path\to\leo\leo\scripts\elevate.py e:\path\to\register-leo.leox



Eventually I'd like to see this activated from a Settings/Options/Preferences menu. Then we can distribute daily and portable builds of Leo and still have easy (dis)integration with the host (on Windows) and not rely so heavily on stable builds and installers, which are few and long between 'cause of the pain in building them.

feedback/testing/patches welcome


-----
Resources used:

    @url http://superuser.com/questions/88491/force-cmd-exe-to-run-as-admin/
    @url  http://stackoverflow.com/questions/2331690/how-to-set-a-icon-file-while-creating-file
    @url http://stackoverflow.com/questions/771689/how-can-i-set-an-icon-for-my-own-file-extension
    

elevate.py: 
    Open a new python intepreter after asking for elevated UAC permissions, and feed it the python script specified on the command line.
    
        python elevate.py d:\full\path\to\some-script.py {args for some-script}

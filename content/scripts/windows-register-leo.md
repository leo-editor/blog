Title: Registering Leo with Windows
Date: 2013-11-28
Tags: Windows, install, scripts
Category: scripts
Slug: register_leo
Author: Matt Wilkie
Summary: Enable 2x-click .leo files in Windows when using bazaar, snapshot or portable Leo

_a post in progress_

Installing Leo using the standard setup program from Sourceforge does nice things like create Start Menu & Desktop shortcuts and enable open Leo files with a simple double-click. For those that like to run from source code or a portable drive there are [manual instructions](http://leoeditor.com/installing.html#installing-from-sources-windows) for doing the same, but it's fiddly and rapidly gets old. Why repeat when automation is possible?

Introducing **[register-leo.leox](http://bazaar.launchpad.net/~leo-editor-team/leo-editor/trunk3/view/head:/leo/scripts/register-leo.leox)** (and [unregister-leo](http://bazaar.launchpad.net/~leo-editor-team/leo-editor/trunk3/view/head:/leo/scripts/unregister-leo.leox)): which creates the necessary Windows registry keys for integration with Explorer and friends. After running this script .leo and .leox files are shown with the Leo icon, and double-clicking on them will open them in Leo.

To use: open a command shell with administrative rights, and run:

```text
    d:\path\to\python.exe d:\path\to\leo\launchLeo.py e:\path\to\register-leo.leox
```

All in one step: you can try the [`elevate.py`](http://bazaar.launchpad.net/~leo-editor-team/leo-editor/trunk3/view/head:/leo/scripts/elevate.py) script which will ask for Admin privileges from a regular command shell:

```text
    d:\path\to\python.exe d:\path\to\leo\leo\scripts\elevate.py e:\path\to\register-leo.leox
```

Eventually I'd like to see this activated from a Settings/Options/Preferences menu. Then we can distribute daily and portable builds of Leo and still have easy (dis)integration with the host (on Windows) and not rely so heavily on stable builds and installers, which are few and long between 'cause of the pain in building them.

Developed and tested with Python 2.7, Leo 4.10 and Win7 x64. Py3 needs work.

Feedback/testing/patches welcome (see mailing list).

-Matt Wilkie

-----
    
Notes
----------- 

#### What's this `.leox`? ####

I created this convention so I could easily distinguish regular Leo files, which can be about anything, and Leo files which are runnable Leo scripts. The intention is to allow for things like:

```text
    leo --script d:\path\to\scripts\register-leo.leox
```

At present double-clicking a .leox opens in edit mode. It occurs to me as I write this it could be changed so it runs automatically by adding, `--script` (quotes might need fiddling with):

    ftype LeoFile="C:\Python27\python.exe" "B:\apps\leo\launchLeo.py" "--script ""%1"" %*


#### Any .leo is a launcher ####

Association has the added benefit of removing the need for most to create a batch file and then figure out where in PATH to store it in order to use Leo. As a matter of fact, any .leo file becomes the equivalent of launchLeo.py, just try this:

    %homedrive%\homepath%\workbook.leo x:\path\to\some\other\leofile.leo

or to build on the previous note:

    %homedrive%\homepath%\workbook.leo --script ..\scripts\unregister-leo.leox



### Resources used ###

http://superuser.com/questions/88491/force-cmd-exe-to-run-as-admin/  
http://stackoverflow.com/questions/2331690/how-to-set-a-icon-file-while-creating-file
http://stackoverflow.com/questions/771689/how-can-i-set-an-icon-for-my-own-file-extension

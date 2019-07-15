@echo.
@echo. --- Windows batchfile to generate and preview html pages
@echo.
@setlocal
@set _p=%prompt%
@set "prompt=$G$_"
rmdir /s/q docs
mkdir docs

pelican content -o docs -s pelicanconf.py

@echo.
@echo. --- Starting local server
@echo. --- Press Ctrl-C to stop server
@echo.
cd doc
start /b "" python -m http.server
start http://localhost:8000/
cd ..
@set prompt=%_p%
@endlocal

pushd "%~dp0"

cd ..

rmdir .venv /q /s
virtualenv .venv --python=C:\Python39x64\python.exe
call .venv\Scripts\activate.bat
poetry install

popd
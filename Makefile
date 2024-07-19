upgrade:
	python.exe -m pip install --upgrade pip

dev:
	fastapi dev app.py

PHONY:
	upgrade dev
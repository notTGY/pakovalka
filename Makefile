all: data/babylm-10M.csv
	gcc -O2 pakovalka.c -o a.out
	python3 -c 'import subprocess; subprocess.run(["./a.out"], timeout=300, check=True)'
	python3 grade.py

data/babylm-10M.csv:
	uv run prepare.py

all: data/lengths.csv
	gcc -O2 pakovalka.c -o a.out
	python3 -c 'import subprocess; subprocess.run(["./a.out"], timeout=300, check=True)'
	python3 grade.py

data/lengths.csv: prepare.py
	uv run prepare.py

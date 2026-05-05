# Makefile for ROT Cipher Toolkit

.PHONY: install test run analyze clean

install:
	pip install -e .

test:
	pytest

run:
	python3 -m rot_toolkit.cli

analyze:
	python3 -m rot_toolkit.cli analyze $(FILE)

encrypt:
	python3 -m rot_toolkit.cli encrypt $(FILE) --shift $(SHIFT)

decrypt:
	python3 -m rot_toolkit.cli decrypt $(FILE) --shift $(SHIFT)

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
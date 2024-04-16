#Makefile ITS Project
#Marek Gergel (xgerge01)

LOGIN := xgerge01

.PHONY: all test pdf clean zip tar

all: test

test:
	behave

pdf: README.md
	pandoc -V geometry:margin=2cm --variable urlcolor=blue $< -o $@

clean:
	rm -f README.pdf $(LOGIN).zip $(LOGIN).tar

zip:
	zip -rq $(LOGIN).zip features/ environment.py requirements.txt report.pdf

tar:
	tar -cf $(LOGIN).tar features/ environment.py requirements.txt report.pdf
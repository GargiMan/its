#Makefile ITS Project
#Marek Gergel (xgerge01)

LOGIN := xgerge01

.PHONY: all test clean zip tar

all: test

test:
	behave

report.pdf: report.md
	pandoc -V geometry:margin=2cm --variable urlcolor=blue $< -o $@

clean:
	rm -f README.pdf $(LOGIN).zip $(LOGIN).tar

zip: report.pdf
	zip -rq $(LOGIN).zip features/ requirements.txt report.pdf

tar: report.pdf
	tar -cf $(LOGIN).tar features/ requirements.txt report.pdf
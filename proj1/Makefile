#Makefile ITS Project
#Marek Gergel (xgerge01)

LOGIN := xgerge01

.PHONY: all pdf clean zip tar

all: zip

pdf: README.md
	pandoc -V geometry:margin=2cm --variable urlcolor=blue $< -o $@

clean:
	rm -f README.pdf $(LOGIN).zip $(LOGIN).tar

zip:
	zip -rq $(LOGIN).zip features/ README.md

tar:
	tar -cf $(LOGIN).tar features/ README.md
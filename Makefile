SRC = cover
BIBL = bibl.bib
TEXS = segments.tex

cover.pdf: $(SRC).tex $(BIBL) pracamgr.cls segments.tex
	pdflatex $(SRC)
	bibtex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

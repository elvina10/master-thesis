SRC = cover
BIBL = bibl.bib

cover.pdf: $(SRC).tex $(BIBL) pracamgr.cls
	pdflatex $(SRC)
	bibtex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

SRC = cover
BIBL = bibl.bib
TEXS = segments.tex cover.tex apxcomplete.tex weighted_segments.tex

cover.pdf: $(SRC).tex $(BIBL) pracamgr.cls $(TEXS)
	pdflatex $(SRC)
	bibtex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

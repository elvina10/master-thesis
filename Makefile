SRC = cover
BIBL = bibl.bib
TEXS = segments.tex definitions.tex cover.tex apxcomplete.tex fpt_weighted_segments.tex w1_completeness.tex apx_choose_variable.pdf_tex apx_or_gadget.pdf_tex apx_clause.pdf_tex fpt_v_t_def.pdf_tex

cover.pdf: $(SRC).tex $(BIBL) pracamgr.cls $(TEXS)
	pdflatex $(SRC)
	bibtex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

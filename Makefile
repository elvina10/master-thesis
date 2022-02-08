SRC = thesis
BIBL = bibl.bib
SVGS = fpt_v_t_def fpt_tricky_case
TEXS = segments.tex definitions.tex apxcomplete.tex fpt_weighted_segments.tex w1_hardness.tex fig_apx_segment_whole.tex fig_apx_choose_variable.tex fig_apx_or_gadget.tex fig_apx_clause.tex introduction.tex

thesis.pdf: $(SRC).tex $(BIBL) pracamgr.cls $(TEXS) $(foreach x,$(SVGS), $x.svg)
	$(foreach x,$(SVGS), inkscape -D --export-latex --export-pdf=$x.pdf $x.svg;)
	pdflatex $(SRC)
	bibtex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

%.pdf_tex: $@.svg
	inkscape -D --export-latex --export-pdf=$@.pdf $@.svg

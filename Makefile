SRC = cover
BIBL = bibl.bib
SVGS = fpt_v_t_def fpt_tricky_case
TEXS = segments.tex definitions.tex cover.tex apxcomplete.tex fpt_weighted_segments.tex w1_completeness.tex apx_choose_variable.pdf_tex apx_or_gadget.pdf_tex apx_clause.pdf_tex fig_apx_segment_whole.tex

cover.pdf: $(SRC).tex $(BIBL) pracamgr.cls $(TEXS) $(foreach x,$(SVGS), $x.svg)
	$(foreach x,$(SVGS), inkscape -D --export-latex --export-pdf=$x.pdf $x.svg;)
	pdflatex $(SRC)
	bibtex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

%.pdf_tex: $@.svg
	inkscape -D --export-latex --export-pdf=$@.pdf $@.svg

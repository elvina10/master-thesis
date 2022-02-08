SRC = thesis
BIBL = bibl.bib
SVGS = fpt_v_t_def fpt_tricky_case
FIGURES = figures/fig_apx_segment_whole.tex figures/fig_apx_choose_variable.tex figures/fig_apx_or_gadget.tex figures/fig_apx_clause.tex figures/grid_tiling_example.tex figures/diag_definition.tex figures/w1_hard_segments.tex
TEXS = segments.tex definitions.tex apxcomplete.tex fpt_weighted_segments.tex w1_hardness.tex introduction.tex

thesis.pdf: $(SRC).tex $(BIBL) pracamgr.cls $(TEXS) $(FIGURES) $(foreach x,$(SVGS), $x.svg)
	$(foreach x,$(SVGS), inkscape -D --export-latex --export-pdf=$x.pdf $x.svg;)
	pdflatex $(SRC)
	bibtex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

%.pdf_tex: $@.svg
	inkscape -D --export-latex --export-pdf=$@.pdf $@.svg

clean:
	rm *.aux
	rm *.bbl
	rm *.blg
	rm *.log
	rm *.toc

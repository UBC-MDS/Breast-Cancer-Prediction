all	:	doc/report.md

results/breast_cancer_new.csv	:	scripts/read_clean.py	data/breast_cancer.csv
	python	scripts/read_clean.py	data/breast_cancer.csv	results/breast_cancer_new.csv

img/plot	:	scripts/eda.py results/breast_cancer_new.csv
	python	scripts/eda.py	results/breast_cancer_new.csv img/plot

results/detailed_importance	:	scripts/analysis.py results/breast_cancer_new.csv
	python scripts/analysis.py results/breast_cancer_new.csv results/importance.csv results/detailed.csv

results/results.png	:	scripts/plot.py results/importance.csv
	python scripts/plot.py results/importance.csv results/results.png

doc/report.md : doc/report.Rmd img/plot results/detailed_importance results/results.png
	Rscript -e "rmarkdown::render('doc/report.Rmd')"

clean :
	rm -f results/*
	rm -f doc/Report.md
	rm -f doc/Report.html
	rm -f	doc/report_files/figure-markdown_github/*

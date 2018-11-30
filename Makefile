# Driver script
# Akansha Vashisth and Talha A. Siddiqui, Nov 2018
# The goal of this project is to discover the strongest predictors of breast cancer
#
# Usage: make all

# Run all analysis
all	:	doc/report.md

# Get the data
results/breast_cancer_new.csv	:	scripts/read_clean.py	data/breast_cancer.csv
	python	scripts/read_clean.py	data/breast_cancer.csv	results/breast_cancer_new.csv

# Generate EDA plots
img/plot	:	scripts/eda.py results/breast_cancer_new.csv
	python	scripts/eda.py	results/breast_cancer_new.csv img/plot

# Generate detailed prediction results and features importance
results/detailed_importance	:	scripts/analysis.py results/breast_cancer_new.csv
	python scripts/analysis.py results/breast_cancer_new.csv results/importance.csv results/detailed.csv

# Plot features importance
results/results.png	:	scripts/plot.py results/importance.csv
	python scripts/plot.py results/importance.csv results/results.png

# Generate final report
doc/report.md : doc/report.Rmd results/breast_cancer_new.csv img/plot results/detailed_importance results/results.png
	Rscript -e "rmarkdown::render('doc/report.Rmd')"

# Clean up intermediate files
clean :
	rm -f results/*
	rm -f doc/Report.md
	rm -f doc/Report.html
	rm -f	doc/report_files/figure-markdown_github/*

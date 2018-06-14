start_year=2016
end_year=2017

.PHONY: all
all: gdd_map_plot gdd_accumulated bokehplot gen_gdd min_max_plot
	@echo "Starting workflow"

linearReg: min_max_plot
	@echo "Plotting Linear Regression"
	python3 linearReg.py $(start_year) $(end_year)

min_max_plot: download_data gen_gdd gdd_accumulated
	@echo "Plotting min-max values"
	python3 min_max_plot.py

gen_gdd: download_data
	@echo "Computing GDD with base 10"
	@for file in Data/*.csv; do python3 gdd.py $$file 10 30; done
	@echo "Computing GDD with base 5"
	@for file in Data/*$(start_year).csv; do python3 gdd.py $$file 5 30; done
	@echo "Computing GDD with base 0"
	@for file in Data/*$(start_year).csv; do python3 gdd.py $$file 0 30; done

download_data: input.csv init
	@echo "Downloading data"
	python3 download_data.py $< $(start_year) $(end_year)

gdd_accumulated: download_data gen_gdd
	@echo "Generating Accumulated GDD plots for all years"
	python3 gddplot.py

bokehplot: gen_gdd
	python3 bokehplot.py


gdd_map_plot: init
	@echo "Ploting GDD map"
	python3 gdd_map_plot_NL.py
	python3 gdd_map_plot_CAN.py

#gen_latex: docs/project_report.tex gdd_acccumulated bokehplot gdd_map_plot min_max_plot
#	latexmk -pdf $<

clean:
	rm -rf Data/*.csv Plots/* GDDFiles* docs/plots/*

init:
	mkdir -p Data Plots docs/data docs/plots

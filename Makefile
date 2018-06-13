.PHONY: get_all_results
get_all_results: min_max_plot gdd_plot gdd_map_plot gen_latex 
 
min_max_plot: download_data
	@echo "Plotting min-max values"
	python3 min_max_plot.py

download_data: input.csv init 	
	@echo "Downloading data"
	python3 download_data.py $< 2016 2017

gdd_map_plot: 
	@echo "Ploting GDD map"
	python3 gdd_map_plot_NL.py
	python3 gdd_map_plot_CAN.py

gen_latex: Plots/* docs/plots/*
	latexmk report.tex

clean:
	rm -f Data/*.csv Plots/* docs/plots/*

init:
	mkdir -p Data Plots docs/data docs/plots

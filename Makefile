start_year=2016
end_year=2017

.PHONY: min_max_plot
min_max_plot: download_data gen_gdd
	@echo "Plotting min-max values"
	python3 min_max_plot.py

gen_gdd: download_data 
	@echo "Computing GDD with base 10"
	@for file in Data/*$(start_year).csv; do python3 gdd.py $$file 10 30; done
	@echo "Computing GDD with base 5"
	@for file in Data/*$(start_year).csv; do python3 gdd.py $$file 5 30; done
	@echo "Computing GDD with base 0"
	@for file in Data/*$(start_year).csv; do python3 gdd.py $$file 0 30; done

download_data: input.csv init 	
	@echo "Downloading data"
	python3 download_data.py $< $(start_year) $(end_year) 


gdd_map_plot: 
	@echo "Ploting GDD map"
	python3 gdd_map_plot_NL.py
	python3 gdd_map_plot_CAN.py

#gen_latex: report.tex Plots/* docs/plots/*
#	latexmk $< 

clean:
	rm -f Data/*.csv Plots/* docs/plots/*

init:
	mkdir -p Data Plots docs/data docs/plots

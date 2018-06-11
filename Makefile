.PHONY: min_max_plot
min_max_plot: download_data
	@echo "Plotting min-max values"
	python3 min_max_plot.py

download_data: input.csv init 	
	@echo "Downloading data"
	python3 download_data.py $< 2016 2017

clean:
	rm -f Data/*.csv Plots/*

init:
	mkdir -p Data
	mkdir -p Plots

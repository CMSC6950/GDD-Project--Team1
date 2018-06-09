datafile = ./Data
plot = ./Plots
root = ./

min_max_plot: download_data
	@echo "Plotting Mix and Max Values"
	python3 $(root)min_max_plot.py

download_data: init
	@echo "Downloading files"
	python3 $(root)download_data.py input.csv 2014 2017

clean:
	rm -rf $(plot)
	rm -rf $(datafile)

init:
	mkdir -p $(datafile)
	mkdir -p $(plot)

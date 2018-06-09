datafile = ./Data
plot = ./Plots
root = ./

<<<<<<< HEAD
.PHONY: download_data
download_dat: init $(CITY_FILE_PATHS) $(CITY_NAME_PATHS)
=======
min_max_plot: download_data
	@echo "Plotting Mix and Max Values"
	python3 $(root)min_max_plot.py
>>>>>>> parent of 83ebeef... A trial update of downloading data

download_data: init
	@echo "Downloading files"
	python3 $(root)download_data.py input.csv 2014 2017

clean:
	rm -rf $(plot)
	rm -rf $(datafile)

init:
	mkdir -p $(datafile)
	mkdir -p $(plot)

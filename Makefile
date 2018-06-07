datafile = ./Data
plot = ./Plots
root = ./

download_data: init
	@echo "Downloading files"
	python3 $(root)download_data.py input.csv 2014 2017

clean:
	rm -rf $(plot)
	rm -rf $(datafile)

init: clean
	mkdir -p $(datafile)
	mkdir -p $(plot)

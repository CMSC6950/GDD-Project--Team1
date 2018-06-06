datafile = ./Data
plot = ./Plots
root = ./

download_data: init
	python $(root)download_data.py input.csv 2013 2017

clean:
	rm -rf $(plot)
	rm -rf $(datafile)

init: clean
	mkdir -p $(datafile)
	mkdir -p $(plot)

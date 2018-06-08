-include cities.mak
CITY_FILES := $(addsuffix .csv, $(CITIES))
CITY_NAMES := $(addsuffix .name, $(CITIES))
CITY_FILE_PATHS := $(addprefix Data/, $(CITY_FILES))
CITY_NAME_PATHS := $(addprefix Data/, $(CITY_NAMES))

.PHONY: min_max_plot
min_max_plot: download_data
	@echo "Plotting min-max values"
	python3 min_max_plot.py

download_data: init $(CITY_FILE_PATHS) $(CITY_NAME_PATHS)
	@echo "Downloading data"

Data/%.name: input.csv 
	python3 gen_station_name_files.py $< 2012 2013

Data/cities_list.txt: input.csv 
	python3 gen_station_name_files.py $< 2012 2013

Data/%.csv: Data/%.name download_data.py 
	python3 download_data.py $<

cities.mak: Data/cities_list.txt 
	@sed -e ':a' -e 'N' -e '$$!ba' -e 's/\n/ /g' -e 's/^/CITIES := /' $< > $@

clean:
	rm -f cities.mak Data/*.name Data/*.csv Data/cities_list.txt

init:
	mkdir -p Data
	mkdir -p Plots

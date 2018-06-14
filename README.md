# Growing degree days project for CMSC6950

Team members:
Dawei Wang
Ajay vijayakumar
Demarey Baker
Haqqani Gulam

*Growing degree day(s) (GDD)*, also called growing degree units (GDUs), are a heuristic tool in phenology. GDD are a measure of heat accumulation used by horticulturistics, gardeners and farmers to predict plant and animal development rates such as the date that a flower will bloom, or a crop will reach maturity (From wikipedia).

This project will walk through the whole computational workflow for this GDD analysis problem. In this project, we will show the annual cycle of min/max dailly temperatures, accumulated GDD vs time at year 2016 and 2017 for Halifax, Calgary and Ottawa. More specifically, we will use their station IDs 50620, 50430 and 49568. In addition, we plotted the accumulated GDD distribution for both Canada and Newfoundland area to show that central Newfoundland tends to have a higher GDD values than other Newfoundland areas. We also analysed the relationship of GDD calculation with the choice of base temperature and show that a higher base will lead to a lower GDD value. As the final task report, we use the accumulated GDD values to predict expected date for a specific flower to emerge.

The whole process of this workflow is automatically implemented using the building functioinality of a Makefile. And we tested the performance and reliability of the codes. Tried to exploit possiblity of parallel implementation.

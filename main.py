## Imporant : The Cleaner needs a manual modification (removing of some columns for the moment)

#from parser.cleaner import clean_dynon_csv

#raw_file = "data/raw/FlightDEK-D180_sn1878_20250731_datalog.csv"
#cleaned_file = "data/cleaned/FlightDEK-D180_sn1878_20250731_datalog.cleaned.csv"

#clean_dynon_csv(raw_file, cleaned_file)

from parser.segmenter import parse_and_split_sessions

parse_and_split_sessions(
    input_path="data/cleaned/FlightDEK-D180_sn1878_20250731_datalog.cleaned.csv",
    output_dir="data/sessions/"
)

from visualization.plotter import plot_oil_temperature

plot_oil_temperature("data/sessions/session_2.csv")

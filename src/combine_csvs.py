import os

# * Get the CSVs
csvs_list = os.listdir("../Movie CSVs/")

# * Create the new CSV file
mcu_csv_file = open("../MCU CSV/MCU_interactions.csv", "w")

for csv in csvs_list:
    curr_csv = open("../Movie CSVs/" + csv)
    print("opening ", csv)
    curr_csv_lines = curr_csv.readlines()

    for line in curr_csv_lines:
        mcu_csv_file.write(line)
    
    mcu_csv_file.write("\n")

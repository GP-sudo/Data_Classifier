import pandas as pd

def generate_report(file_name, classified_data):
    df = pd.DataFrame(classified_data, columns=["Entity/Field", "Sensitivity"])
    df["File"] = file_name
    return df
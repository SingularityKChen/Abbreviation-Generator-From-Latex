class backend:
    """
    Backend generate the latex table for abbreviations from the csv file.\n
    This file can be either generated and/or modified from frontend or created manually.\n
    Format of the csv file:\n
    first column: abbr \n
    second column: long words.
    """
    def __init__(self, f_gen_abbr_latex_dir: str = "", f_csv_dir: str = ""):
        self.csv_file_dir = f_csv_dir

#!/usr/bin/python3
from pathlib import Path


class backend:
    """
    Backend generate the latex table for abbreviations from the csv file.\n
    This file can be either generated and/or modified from frontend or created manually.\n
    Format of the csv file:\n
    first column: abbr \n
    second column: long words.
    """
    def __init__(self, f_gen_abbr_latex_dir: str = "", f_csv_dir: str = ""):
        self._abbr_tex_filename = "abbr.tex"
        self._abbr_csv_filename = "abbr.csv"
        if f_csv_dir:
            self._csv_dir = f_csv_dir
        else:
            self._csv_dir = "."
        if f_gen_abbr_latex_dir:
            self._abbr_tex_dir_filename = f_gen_abbr_latex_dir + "/" + self._abbr_tex_filename
        else:
            self._abbr_tex_dir_filename = self._csv_dir + "/" + self._abbr_tex_filename
        self._abbr_csv_dir_filename = self._csv_dir + "/" + self._abbr_csv_filename
        # Generate the abbr latex file
        self._gen_abbr_tex()

    def _gen_abbr_tex(self):
        abbr_csv = Path(self._abbr_csv_dir_filename)
        if not abbr_csv.exists():
            exit("\033[91m[ERROR] The csv file %s does not exists!\033[0m" % self._abbr_csv_dir_filename)
        abbr_tex = Path(self._abbr_tex_dir_filename)
        with open(abbr_tex, "w+") as tex:
            tex.write("\\begin{longtable}{ll}\n")
            for line in abbr_csv.open():
                abbr_read_line = line.strip().split(",")
                abbr_write_line = "\t%s & %s \\\\\n" % (abbr_read_line[0], abbr_read_line[1])
                tex.write(abbr_write_line)
            tex.write("\\end{longtable}")
            tex.close()

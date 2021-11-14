#!/usr/bin/python3
import argparse
from backend import backend
from frontend import frontend


class abbr_latex_generator:
    def __init__(self):
        self._target_csv_dir = ""
        self._target_latex_dir = ""
        self._source_latex_file_list = []
        self._whether_frontend = False
        self._whether_backend = False
        self._get_opt()
        if self._whether_frontend:
            if self._source_latex_file_list:
                self._ft = frontend(f_source_file_dir_name_list=self._source_latex_file_list,
                                    f_target_csv_dir=self._target_csv_dir)
            else:
                exit("\033[91m[ERROR] The source latex file list is empty!\033[0m")
        if self._whether_backend:
            self._bk = backend(f_csv_dir=self._target_csv_dir, f_gen_abbr_latex_dir=self._target_latex_dir)

    def _get_opt(self):
        parser = argparse.ArgumentParser(description="To retrieval abbreviations from the files into a latex table.")
        parser.add_argument("-f", "--frontend", dest="frontend", action="store_true", help="Execute frontend flow.")
        parser.add_argument("-b", "--backend", dest="backend", action="store_true", help="Execute backend flow.")
        parser.add_argument("-s", "--texsourcefile", dest="tex_source_file", nargs="+",
                            help="The source latex files that will be retrieved. This argument is required in frontend")
        parser.add_argument("-c", "--csvdir", dest="csv_dir", nargs=1,
                            help="The generated abbr csv directory.")
        parser.add_argument("-l", "--latexdir", dest="tex_dir", nargs=1,
                            help="The generated abbr latex table directory.")
        args = parser.parse_args()
        self._whether_frontend = args.frontend
        self._whether_backend = args.backend
        self._target_csv_dir = args.csv_dir
        self._target_latex_dir = args.tex_dir
        self._source_latex_file_list = args.tex_source_file


if __name__ == '__main__':
    gen = abbr_latex_generator()

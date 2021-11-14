#!/usr/bin/python3
from abbreviations import schwartz_hearst


class frontend:
    """
    Frontend retrieval abbreviations from the files into a csv file.\n
    Users are supposed to check the generated csv file before executing the backend,
    where the csv file will be read and write into the required latex abbreviation table.
    """

    def __init__(self, f_source_file_dir_name_list: list, f_target_csv_dir: str = ""):
        self._csv_name = "abbr.csv"
        self._abbr_dict = {}  # empty abbr dictionary
        self._file_list = f_source_file_dir_name_list
        if f_target_csv_dir:
            self._target_csv_dir = f_target_csv_dir
        else:
            self._target_csv_dir = "."
        self._csv_dir_filename = self._target_csv_dir + "/" + self._csv_name
        self._retrieval_files()
        self._abbr_dict_to_csv()
        print("[INFO] Abbreviations in", self._file_list, "are writen into", self._csv_dir_filename)

    def _retrieval_files(self):
        for file in self._file_list:
            self._retrieval_single_file(file)
        self._abbr_dict = dict(sorted(self._abbr_dict.items()))

    def _retrieval_single_file(self, f_file_dir_name: str):
        self._abbr_dict.update(schwartz_hearst.extract_abbreviation_definition_pairs(file_path=f_file_dir_name,
                                                                                     most_common_definition=False,
                                                                                     first_definition=False))

    def _abbr_dict_to_csv(self):
        csv_file = open(self._csv_dir_filename, "w")
        for abbr, words in self._abbr_dict.items():
            csv_file.write("%s,%s\n" % (abbr, words))
        csv_file.close()

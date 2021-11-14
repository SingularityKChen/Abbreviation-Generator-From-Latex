# Abbreviation-Generator-From-Latex

## 3 Steps
Generate Abbreviations from Latex files using this Python3 script:
```bash
python3 abbr_latex_generator.py -f -s <source latex files>
```

Then you can find a middle file `abbr.cvs` for you to check and modify.

After you modify the csv file, 
then you can execute the backend flow to generate latex format table from this csv file.
You can find the final latex file `abbr.tex`.
```bash
python3 abbr_latex_generator.py -b
```

## Full Usages

```
usage: abbr_latex_generator.py [-h] [-f] [-b] [-s TEX_SOURCE_FILE [TEX_SOURCE_FILE ...]] [-c CSV_DIR] [-l TEX_DIR]

To retrieval abbreviations from the files into a latex table.

optional arguments:
  -h, --help            show this help message and exit
  -f, --frontend        Execute frontend flow.
  -b, --backend         Execute backend flow.
  -s TEX_SOURCE_FILE [TEX_SOURCE_FILE ...], --texsourcefile TEX_SOURCE_FILE [TEX_SOURCE_FILE ...]
                        The source latex files that will be retrieved. This argument is required in frontend
  -c CSV_DIR, --csvdir CSV_DIR
                        The generated abbr csv directory.
  -l TEX_DIR, --latexdir TEX_DIR
                        The generated abbr latex table directory.

```

### Frontend Example

Retrieval abbreviations from a single Latex file:
```bash
python3 abbr_latex_generator.py -f -s my_latex.tex
```


Retrieval abbreviations from multiple Latex files:
```bash
python3 abbr_latex_generator.py -f -s *.tex
```

## Reference

This Python script employs the Python library 
[abbreviation-extraction](https://github.com/philgooch/abbreviation-extraction)
to extrate abbreviations into the middle csv file.

So you're supposed to install this package:
```bash
pip3 install abbreviations
```

Or:
```bash
pip3 install -r requirements.txt
```
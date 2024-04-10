# GML Generator
The `gml_generator.py` script generates GML files using Apache SIS, from a set of WKTs listed in a file (`result.wkts`).

## Requirements
In order to run `gml_generator.py`, there are a few requirements.

### JPype
JPype is used to make a bridge between the Python code and Java code. It is necessary to call Apache SIS's functions.

To install it, run the following:
```python
pip install JPype1
```

### TQDM
TQDM is used to show the progression of the GML file generation.

To install it, run the following:
```python
pip install tqdm
```

### WKT file
Make sure that the file `result.wkts` is in the same directory as `gml_generator.py`, and that each WKT is separated by a double line break (`\n\n`).

## Running the script
To run the script, go in the same directory as `gml_generator.py` and run the following:
```python
python gml_generator.py
```

When running the script, you will be prompted a few parameters:
* **Apache SIS**
  * If you have local installation of Apache SIS in the same directory as the script, with the format `apache-sis-1.4`, this Apache SIS will be used for GML generation.
  * Otherwise, you will be prompted the directory to a local installation of Apache SIS.
  * If you don't have local installation, Apache SIS will automatically be downloaded (~12 MB). Note: Apache SIS directory will be deleted once the script is completed.
* **Remove all existing GML files:** Whether you want to remove all GML files in the output directory. This can be useful to make sure you do not keep previously-generated GML files.
* **Override existing GML files:** Whether you want to override existing GML files if they already exist.

*Note: The last two prompts are not displayed if the output directory is empty.*

There will be a warning: `AVERTISSEMENT: La variable environnementale « SIS_DATA » n'est pas définie.` This references a variable used by the EPSG extension (for Apache SIS), which is not needed for IAU CRS. You can safely ignore that warning.

GML files are generated in the `gml` directory.

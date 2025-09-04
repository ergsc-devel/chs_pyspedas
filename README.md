# chs_pyspedas


# User's guide of CHS plug-ins for PySPEDAS

The routines in this module can be used to load time series data from the SUSANOO-SW.

## Instllation
To avoid potential dependency issues with other Python packages, we suggest creating a virtual environment for miopyspedas plug-in; you can create a virtual environment in your terminal with:

### Virtual Environment

```
python -m venv chs_pyspedas_test
```

To enter your virtual environment, run the 'activate' script:

**Windows**
```bash
.\chs_pyspedas_test\Scripts\activate
```

**macOS and Linux**
```bash
source ~/chs_pyspedas_test/bin/activate
```

#### Using Jupyter notebooks with your virtual environment
To get virtual environments working with Jupyter, in the virtual environment, type:

```bash
pip install ipykernel
python -m ipykernel install --user --name chs_pyspedas_test --display-name "(CHSpySPEDAS plug-in)"
```
> [!NOTE]
>"chs_pyspedas_test" is the name of your virtual environment

Then once you open the notebook, go to "Kernel" then "Change kernel" and select the one named "(CHSpySPEDAS plug-in)"

### Install
PySPEDAS supports Windows, macOS and Linux. To get started, install the pyspedas package using PyPI:
```bash
pip install pyspedas
```

### Install chs_pyspedas plug-in
After installing pyspedas, you need to add miopyspedas plug-in to your virtual environment.

```bash
pip install git+https://github.com/ergsc-devel/chs_pyspedas.git
```


## Examples
An example code for Jupyter notebooks 

```python
import chs_pyspedas
from pytplot import tplot, store_data, options, get_data
import pyspedas
```

Choose timespan by trange


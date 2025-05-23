# midasmlpy

Python implementation of the midasml approach - providing **estimation** and **prediction** methods for high-dimensional mixed-frequency time-series data

## Authors

* Jonas Striaukas - [jstriaukas](https://github.com/jstriaukas)
* Kris Stern - [krisstern](https://github.com/krisstern)
* Marcus Egelund-Müller - [Mem03](https://github.com/Mem03)

## About

The *midasmlpy* package implements *estimation* and *prediction* methods for high-dimensional mixed-frequency (MIDAS) time-series and panel data in regression models.
The regularized MIDAS models are estimated using orthogonal (e.g. Legendre) polynomials and the sparse-group LASSO estimator.
For more information on the *midasmlpy* approach there are references in the footnotes[^2][^3].

The package is equipped with the fast implementation of the sparse-group LASSO estimator by means of proximal block coordinate descent.
High-dimensional mixed frequency time-series data can also be easily manipulated with functions provided in the package.

## The `.f90` source files

These can be found at the [midasmlpy/src](./midasmlpy/src/sparseglf90/) directory.
Compiled `.so` files can be found at [midasmlpy/compiled](./midasmlpy/compiled) directory.
Please note that we have taken the `.f90` source code for sparse-group LASSO from the repo of the R package `sparsegl` on hosted GitHub at https://github.com/dajmcdon/sparsegl.
We have taken their source code in accordance with their GPL-2.0 license as is without any modification as of November 2nd, 2023 UTC.

## Compiling the `.f90` source files with `f2py` on a Mac

### The `gfortran` command to compile `.mod` files from `.f90`

Run:

```bash
gfortran -c fortran_file.f90
```

### The `f2py` command to compile `.so` files from `.f90`

Run:

```bash
python -m numpy.f2py -c fortran_file.f90 -m fortran_file
```

_**Note**_: Be sure the `python` executable above matches the one in your environment.

## Software in other languages

- A Julia implementation of the midasml method is available [here](https://github.com/ababii/Pythia.jl).
- A MATLAB implementation of the midasml method is available [here](https://github.com/jstriaukas/midasml_mat).
- An R implementation of the midasml method is available [here](https://github.com/jstriaukas/midasml).

## Installation

To install the `midasmlpy` package, download the files and at the directory of files run:

```shell
pip install .
```

To install the `midasmlpy` package in development or “editable” mode, do the following:

```shell
pip install -e .
```

## Development

We recommend using the VS Code IDE for local development. After cloning this repo, before you install the `midasmlpy` package, you should run the following commands in the Terminal one-by-one:

1. Go to the source file directory

   ```shell
   cd midasmlpy/src/sparseglf90
   ```
2. Delete the original "sparsegllog_module_1.pyf" file in that directory.
3. Compile the f90 code with `f2py`

   ```shell
   python -m numpy.f2py spmatmul.f90 log_sgl_subfuns.f90 sgl_subfuns.f90 sparsegl.f90 sparsegllog.f90 -m sparsegllog_module -h sparsegllog_module_1.pyf

   python -m numpy.f2py --fcompiler=gnu95 -c sparsegllog_module_1.pyf spmatmul.f90 log_sgl_subfuns.f90 sgl_subfuns.f90 sparsegl.f90 sparsegllog.f90
   ```

   Please note that the above instructions are exactly the same as the ones at [midasmlpy/src/sparseglf90/README.md](midasmlpy/src/sparseglf90/README.md)
4. Return to the root directory

   ```shell
   cd ../../..
   ```
5. To install the `midasmlpy` package for development, first ensure that you have [gfortran](https://gcc.gnu.org/wiki/GFortran) installed. Then do the following instead in “editable” mode:

   ```shell
   pip install -e .
   ```

## Testing

We are using `unittest` as the testing framework for our package. Please set up testing for this framework as per the instructions in the [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing) document. If successful, VS Code should be able to autodetect the tests should be showing up at the Test Explorer view accessible via the beaker icon displayed on the VS Code Activity bar. Note we have assumed that you have the Python extension installed and a Python file open within the editor.

To run the tests, please click on the run icon next to the tests in the Test Explorer, like in the screenshot below:

<img title="Test Explorer sample image" alt="Test Explorer sample image" src="./media/test-explorer-sample-image.png" width="300px;">

> [!NOTE]
> The run icon only shows up if you hover your cursor over the relevant test(s) in the Test Explorer.

## Remarks

In case you are running the code on a different platform, you can compile the Fortran code `sglfitF.f90` by using `f2py` which is part of `numpy`. There is a guide in midasmlpy/src/sparseglf90/README.md

[^1]: Babii, A., Ghysels, E., & Striaukas, J. Machine learning time series regressions with an application to nowcasting, (2022) *Journal of Business & Economic Statistics*, Volume 40, Issue 3, 1094-1106. https://doi.org/10.1080/07350015.2021.1899933.
    
[^2]: Babii, A., Ghysels, E., & Striaukas, J. High-dimensional Granger causality tests with an application to VIX and news, (2022) *Journal of Financial Econometrics*, nbac023. https://doi.org/10.1093/jjfinec/nbac023.
    
[^3]: Babii, A., R. Ball, Ghysels, E., & Striaukas, J. Machine learning panel data regressions with heavy-tailed dependent data: Theory and application, (2022) *Journal of Econometrics*. https://doi.org/10.1016/j.jeconom.2022.07.001.

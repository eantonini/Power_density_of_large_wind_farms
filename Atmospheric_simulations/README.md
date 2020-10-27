This folder contains setup files and instructions to reproduce the numerical results of the paper using WRF 4.2.1.


## Downloading WRF

WRF 4.2.1 can be downloaded from https://github.com/wrf-model/WRF/releases/tag/v4.2.1


## Setting up WRF cases

Copy `module_initialize_ideal.F` into `$WRF_ROOT_DIRECTORY/dyn_em/`

Copy  `input_sounding`, `namelist.input`, `wind-turbine-1.tbl`, `windturbines-ij-9,0Wm2.txt` (or `windturbines-ij-4,5Wm2.txt`)  into `$WRF_ROOT_DIRECTORY/test/em_convrad/`

Then change `windturbines-ij-9,0Wm2.txt` (or `windturbines-ij-4,5Wm2.txt`) to `windturbines-ij.txt`


## Changing WRF setup files

In the paper, we performed simulations with different combinations of geostrophic winds, Coriolis parameters, and installed capacity density.

The setup files included in this repository are for a geostrophic wind of 16 m/s, Coriolis parameter of 1.05 x 10^(-4) rad/s, and installed capacity density of 9 W/m^2.

To change the geostrophic wind, insert the desired value in the fourth column of `input_sounding`.

To change the Coriolis parameter, insert the desired value at line 419 of `module_initialize_ideal.F`. Every time `module_initialize_ideal.F` is changed, you must re-compile WRF.

To change the installed capacity density, use either `windturbines-ij-9,0Wm2.txt` or `windturbines-ij-4,5Wm2.txt` for an installed capacity density of 9 or 4.5 W/m^2, respectively.


## Compiling WRF

Please follow the instructions at https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php to install the required libraries.

The following commands should then be run from the WRF root directory:

* `>> ./clean  &> log.clean1`
* `>> ./clean -a &> log.clean2`
* `>> ./configure &> log.configure` with options 34 and 1
* `>> ./compile em_convrad >& log.compile`


## Running WRF

Run from the WRF root directory:

* `>> cd test/em_convrad/`
* `>> ./run_me_first.csh`
* `>> rm ozone*`
* `>> rm RRTMG_*`
* `>> ./ideal.exe`
* `>> ./wrf.exe`

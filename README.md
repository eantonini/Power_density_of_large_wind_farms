# Power_density_of_large_wind_farms

This repository contains setup files for WRF 4.2.1 to reproduce results of the following paper:

Enrico G.A. Antonini, Ken Caldeira, "Atmospheric pressure gradients and Coriolis forces provide geophysical limits to power density of large wind farms", under review.

## WRF installation instructions

WRF 4.2.1 can be downloaded from https://github.com/wrfmodel/WRF/releases/tag/v4.2.1

Once downloaded, the following commands should be run from the WRF root directory:

* `>> ./clean  &> log.clean1`
* `>> ./clean -a &> log.clean2`
* `>> ./configure &> log.configure` with options 34 and 1
* `>> ./compile em_convrad >& log.compile`


## Setting up WRF cases

Copy `module_initialize_ideal.F` into `./dyn_em/`

Copy  `input_sounding`, `namelist.input`, `wind-turbine-1.tbl`, `windturbines-ij-9,0Wm2.txt` (or `windturbines-ij-4,5Wm2.txt`)  into `./test/em_convrad/`

Run from the WRF root directory:

* `>> cd test/em_convrad/`
* `>> ./run_me_first.csh`
* `>> rm ozone*`
* `>> rm RRTMG_*`
* `>> mv windturbines-ij-9,0Wm2.txt windturbines-ij.txt`


## Changing WRF set-up files

In the paper, we performed simulations with different combinations of geostrophic winds, Coriolis parameters, and installed power density.

The set-up files included in this repository are for a geostrophic wind of 16 m/s, Coriolis parameter of 1.05 x 10^(-4) rad/s, and installed power density of 9 W/m^2.



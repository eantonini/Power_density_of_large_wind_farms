# Power_density_of_large_wind_farms

This repository contains setup files for WRF 4.2.1 to reproduce results of the following paper:

Enrico G.A. Antonini, Ken Caldeira, "Atmospheric pressure gradients and Coriolis forces provide geophysical limits to power density of large wind farms", under review.

## WRF installation instructions

WRF 4.2.1 can be downloaded from https://github.com/wrfmodel/WRF/releases/tag/v4.2.1

Once downloaded, the following commands should be run from the WRF root directory:

* `>> ./clean  &> log.clean1`
* `>> ./clean -a &> log.clean2`
* `>> ./configure &> log.configure` options 34 and 1
* `>> ./compile em_convrad >& log.compile`


## Setting up WRF cases

Copy `module_initialize_ideal.F` into `./dyn_em/`

Copy 





* `>> cd test/em_convrad/`
* `>> ./run_me_first.csh`
* `>> rm ozone*`
* `>> rm RRTMG_*;`

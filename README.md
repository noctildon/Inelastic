# Inelastic nuclear scattering from neutrinos and dark matter

This repo contains the code to produce the figures and calculations in [the paper](https://arxiv.org/abs/2206.08590) (Bhaskar Dutta, Wei-Chih Huang, Jayden L. Newstead, Vishvas Pandey). Here we take argon for an example.

|Filename   |Description   |
|---|---|
|DMfiles/  | density matrices for each transitions (including BIGSTICK raw output and the converted)  |
|res2den.py  | Convert BIGSTICK outputs to the compatible inputs for 7operator|
|ar40_s.res  | BIGSTICK output for ar40 strength function of Gamow-Teller  |
|neutrino multipole.nb   | Mathematica code to calculate neutrino scattering in multipole formalism|
|neutrino GT.nb   | Mathematica code to calculate neutrino scattering in GT formalism |
|dark matter multipole.nb   | Mathematica code to calculate DM scattering in multipole formalism |
|dark matter GT.nb   | Mathematica code to calculate DM scattering in GT formalism  |


For the source of 7operator, refer to https://elsevier.digitalcommonsdata.com/datasets/hwzx6vfjmv/1
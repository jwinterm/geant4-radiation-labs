# Geant4 Radiation Labs

A four-lab series taking you from a fresh Linux install to a working PET-scanner simulation, using [Geant4](https://geant4.web.cern.ch/) for the physics and Python (pandas, matplotlib) for analysis.

**Read the labs at:** <https://jwinterm.github.io/geant4-radiation-labs/>

## Labs

| | Title | Topic |
|---|---|---|
| 1 | Setting Up Linux and Building Geant4 | Ubuntu VM + Geant4 build with Qt visualization |
| 2 | First Simulation: Building and Running B1 | Compile B1, run interactively + via macros, vary particle/energy |
| 3 | Acquiring and Analyzing Simulation Data | Patch B1 to write CSV via `G4AnalysisManager`; analyze in Python |
| 4 | Medical Physics Application: A PET Scanner | Use B3a PET example; identify 511 keV photopeak; reconstruct lines of response |

## Building locally

This site is built with [Quarto](https://quarto.org/). To preview locally:

```bash
quarto preview
```

To regenerate a single lab as PDF:

```bash
quarto render lab1_setup/lab1.qmd --to pdf
```

## Authors

John Murphy and Steven Carlson

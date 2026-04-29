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

## License

This repository uses a dual license:

- **Code** (Python, C++ snippets, Quarto/YAML config, diagram-generation scripts) is licensed under the [MIT License](LICENSE).
- **Lab content** (prose, diagrams, screenshots, generated figures) is licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](LICENSE-CONTENT).

## Inquiries

Want on-site delivery or customization built on top of these openly-licensed materials? [such.software](https://such.software) — an independent provider co-founded by one of the authors — offers commercial services. Email [john@such.software](mailto:john@such.software).

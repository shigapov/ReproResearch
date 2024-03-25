## GitHub for FAIR reproducible research (data) projects

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/shigapov/ReproResearch/code)
[![Open Data](https://badgen.net/static/open/data/cyan)](https://github.com/shigapov/ReproResearch/data)

**Title**: A ready-to-use repository for FAIR reproducible research (data) projects

**Research question**: Can be GitHub used for creating a FAIR reproducible research (data) project? 

**Research objectives**:
* To examine GitHub's role in the lifecycle of research data management and collaboration
* To explore how GitHub facilitates data sharing, version tracking, and reproducibility of results in research
* To describe best practices for organizing data repositories and leveraging GitHub Actions for automating workflows

## Table of contents

* [Repo structure](#repo-structure)
  * [Plan](#plan)
  * [Docs](#docs)
  * [Data](#data)
  * [Code](#code)
* [Replication package](#replication-package)
* [License](#license)

## Repo structure

Let's keep a project structure simple and use only four folders: code, data, docs, and plan. It is sufficient for the majority of research projects.

Every sub-folder can additionally contain README and LICENSE files, because content of every sub-folder might have a separate license and separate "read me first"-files.

You can get a similar structure using `tree -L 2 -F -r`-command in shell:

```
ReproResearch/
├── plan/
│   ├── software_management_plan/
│   ├── project_proposal/
│   ├── preregistration/
│   ├── data_management_plan/
│   └── README_plan.md
├── docs/
│   ├── talks/
│   ├── report/
│   ├── papers/
│   ├── blogs/
│   └── README_docs.md
├── data/
│   ├── visualized_data/
│   ├── supplemented_materials/
│   ├── raw_data/
│   ├── processed_data/
│   ├── models/
│   ├── appendix/
│   └── README_data.md
├── code/
│   ├── tests/
│   ├── notebooks/
│   ├── experiments/
│   └── README_code.md
├── README.md
├── LICENSE.md
├── CODE_OF_CONDUCT.md
└── CITATION.cff
```

### Plan

The folder `plan` contains documents related to planning your research project. It includes:
* project proposal (project proposals are often not published, but they can be published in [Research Ideas and Outcomes](https://riojournal.com))
* pre-registration (you can create and publish your pre-registration in [Open Science Framework](https://help.osf.io/article/158-create-a-preregistration))
* data management plan (to create a data management plan you can use a template or a DMP-tool listed at [Awesome RDM repo](https://help.osf.io/article/158-create-a-preregistration). If you study or work at the University of Mannheim, you can use [MADataPlan](https://fdz.bib.uni-mannheim.de/madataplan). Consider to archive your DMP in a data repository (e.g., in [MADATA](https://madata.bib.uni-mannheim.de)))
* software management plan (to create a software management plan you can use information provided at [forschungsdaten.info](https://forschungsdaten.info/praxis-kompakt/english-pages/software-management-plans/). If you study or work at the University of Mannheim, you can use [MADataPlan](https://fdz.bib.uni-mannheim.de/madataplan). Consider to archive your SMP in a data repository (e.g., in [MADATA](https://madata.bib.uni-mannheim.de)))

### Docs

The folder `docs` contains a documentation for your research project including
* papers
   * paper (your main paper)
   * data paper (if you collected or created a reusable data)
   * software paper (if you created a reusable software)
* talks
   * abstract (extended abstract(s) for a conference)
   * presentation (slides for your presentation)
   * poster (files for your poster)
* report (project report)
* blogs (posts in social media (LinkedIn, X, Mastodon, etc.) about your research project)

### Data

The folder `data` contains all data used in this research including:
* raw data (input data in your research)
* processed data (processed data in your research)
* visualized data (e.g., figures for papers, presentations and posters)
* supplemented materials (from papers)
* appendix (from papers)
* models (e.g., models for machine and deep learning)

Include data availability statement at the end of your paper. For example, "All data used in this research are freely available at URL under the CC BY license." As a URL provide a DOI-URL of your archived data in a data repository (e.g., in [MADATA](https://madata.bib.uni-mannheim.de)). Archive the whole data folder with README-file, including secondary data like visualized data, supplemented materials, appendix to your papers, and models.

The machine and deep learning models can be additionally uploaded to [Hugging Face Models](https://huggingface.co/models) and you can [generate a DOI](https://huggingface.co/docs/hub/doi) for them.

Cite your archived data, including models, in your papers.

### Code

The folder `code` contains all scripts and codes used in your research including
* notebooks (executable notebooks)
* experiments (scripts for experiments in your research)
* tests (testing scripts for your research)

Include "Code availability statement" at the end of your paper. For example, "All codes used in this research are openly available at URL under MIT license." As a URL provide a DOI-URL of your archived codes in a data repository (e.g., in [MADATA](https://madata.bib.uni-mannheim.de)). Archive the whole `code` folder with README-file, including all kinds of codes.

## Replication Package

Creating a replication package for a research project on GitHub involves packaging all the necessary materials, including code, data, documentation, and any other relevant resources, and organizing them in a clear and accessible manner. Here's a step-by-step guide to creating a replication package:

1. Organize Your Materials:
   * Gather all the materials related to your research project, including source code, data, configuration files, documentation, and planning documents (proposal, DMP, SMP, etc.).
   * Organize these materials into a structured directory hierarchy for easy navigation: code, data, docs, and plan.
2. Edit this README.md File:
   * It should provide an overview of the project, its objectives, and instructions for replication.
   * Include details on dependencies, software requirements, and any special instructions for setting up the environment.
3. Licensing:
   * Choose an appropriate open-source license for your project to specify how others can use, modify, and distribute your work.
   * Include the license file (e.g., LICENSE) in your repository or even in sub-folders as well in case you use multiple licenses.
4. Code Documentation:
   * Ensure that your code is well-documented with comments and docstrings.
   * Provide clear instructions on how to run the code and reproduce the experiments or analyses conducted in your research. Add this info to README files in `code` folder.
5. Data Preparation:
   * If your research involves datasets, ensure that you provide access to the data or instructions on how to obtain it.
   * Include any preprocessing scripts or instructions necessary to prepare the data for use with your code.
6. Scripts and Notebooks:
   * Include any scripts, Jupyter notebooks, or other executable files used in your research. 
   * Make sure these files are well-documented and annotated to explain their purpose and usage.
7. Dependencies and Environment Setup:
   * Provide a list of dependencies required to run your code, including programming languages, libraries, and their versions.
   * Consider using a package manager like Pip (for Python), Maven (for Java), or npm (for JavaScript) to manage dependencies.
8. Testing and Validation:
   * Include any test scripts or validation procedures to ensure the correctness of your code.
   * Provide sample outputs or expected results for users to compare with their own results.
9. Release on GitHub:
   * Create a repository on GitHub (or clone this repository or fork this repository) and push your code and materials to the repository. 
   * Ensure that your repository is set to public or accessible to the intended audience.
   * Optionally, create a release version for your replication package to provide a stable snapshot of your project.
10. Documentation and Support:
    * Maintain documentation on how to use your replication package, and be responsive to inquiries or issues from users who attempt to replicate your research.
11. Arhive in a Data Repository:
    * To ensure long-term preservation, accessibility, and citability of your replication package, archive it in a data repository ([MADATA](https://madata.bib.uni-mannheim.de) or [ZENODO](https://zenodo.org)). Add the obtained DOI to CITATION.cff.
12. Citation and Attribution:
    * Include information on how users should cite your work if they use your replication package for their research.
    * Provide appropriate attribution to any third-party resources or libraries used in your project.

By following these steps, you can create a comprehensive replication package for your research project on GitHub, allowing others to easily replicate your work and build upon it.

## License

This work is licensed under the MIT license (code) and Creative Commons Attribution 4.0 International license (for everything else). You are free to share and adapt the material for any purpose, even commercially, as long as you provide attribution (see CITATION.cff).

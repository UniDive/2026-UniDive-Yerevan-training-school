# Diversity quantification in natural language processing: The why, what, where and how 
This folder contains the material for course 3 of the [2nd UniDive Training School in Yerevan](https://unidive.lisn.upsaclay.fr/doku.php?id=meetings:other-events:2nd_unidive_training_school).

## Trainers
- [Louis Estève](https://www.lisn.upsaclay.fr/membres/esteve-louis/) (Université Paris-Saclay, CNRS, France)
- [Marie-Catherine de Marneffe](https://cental.uclouvain.be/team/mcdm/) (Université Catholique Louvain, Belgium)
- [Nurit Melnik](https://www.openu.ac.il/en/personalsites/nuritmelnik.aspx) (The Open University, Israel)
- [Agata Savary](https://perso.limsi.fr/savary/) (Université Paris-Saclay, CNRS, France)
- [Olha Kanishcheva](https://scholar.google.com/citations?user=C_TrxQoAAAAJ&hl=en) (Heidelberg University, Germany, SET University, Ukraine)

## Sessions
1. [Tuesday] Diversity quantification taxonomy (lecture)
2. [Tuesday] Taxonomy in practice (practical session, group work)
3. [Wednesday] Measuring in-text diversity (practical session, lab)
4. [Thursday] Measuring metalinguistic diversity (practical session, lab)
5. [Friday] Trainees' presentations of the outcomes from sessions 2 and 4 (group work)

See also the [schedule](https://unidive.lisn.upsaclay.fr/doku.php?id=meetings:other-events:2nd_unidive_training_school#schedule) and the [course proposal](https://unidive.lisn.upsaclay.fr/lib/exe/fetch.php?media=meetings:other-events:2nd-training-school:esteve-et-al-diversity-quantification.pdf).

## Prerequisites for the trainees
Before coming to Yerevan, make sure that you have met the following pre-requistites.

### Technical pre-requisites
- Laptop
- Python environment - 2 alternatives:
   - Google account to work with Google Colab (recommended if not/weakly familiar with Python; requires no installations)
   - Local Python 3 installation
      - Reasonably recent Python version (we tested with Python 3.13)
      - Development compilation headers: `python.h` 
      - C compiler (added to your PATH environment variable)
- Understand the [CoNLL-U file format](https://universaldependencies.org/format.html)

### Pre-requisites for the group assignment
- Check the list of [groups](https://github.com/UniDive/2026-UniDive-Yerevan-training-school#trainee-groups) and find the group to which you belong
- Make sure that you have received an email (sent after 6 Jan 2026) by the organizers which
   - puts you in contact with the **members of your group**,
   - links you to a **paper** on diversity quantification in NLP assigned to your group.
- **Read the paper before coming** to Yerevan. Try to understand *why* diversity is important there, what *objects* are quantified for diversity, in which *processing stage* diversity is quantified and which diversity *measures* are used.
- If possible, arrange an **online group meeting** prior to coming to Yerevan to discuss your understanding of the paper.

## Group work in Yerevan
- In session 2 (Tuesday), the trainees will:
   - work in **groups** to analyse their pre-requisite papers following a taxonomy introduced in session 1
   - create a joint **presentation** (based on Google slides template that the trainers will prepare), with up to **5 slides** per group, using this [shared document](https://docs.google.com/presentation/d/1CUBlTrpue8A_GkOJJ7oU7bIopkg_aRVwv7aUzX9Gyu4/edit?usp=sharing)
   - select a **reporter** of the group (preferably a young researcher)
- Session 5 (Friday) will host the group presentations by the repoters: **5 minutes** per group + **2-minute** discussion

## Lab sessions
In sessions 3 (Wednesday) and 4 (Thursday) the trainees will work individually to set up a pipeline for quantifying diversity of various datasets. 
**Python** code will be used. It is provided in 3 alternative formats: 
- Google Colab
- Jupyter notebook file (`*.ipynb`)
- standard Python file (`*.py`)

The data used in labs include:
- a [subset](GUM-subcorpus) of the [GUM corpus](https://gucorpling.org/gum/) (included in this repository) in English with 15 different genres of similar sizes, in the [CoNLL-U format](https://universaldependencies.org/format.html)

### Instructions for starting a lab session in Google colab
- go to the folder of [session 3](https://github.com/UniDive/2026-UniDive-Yerevan-training-school/tree/main/Diversity-quantification-course/session-3-measuring-in-text-diversity-in-nlp) or [session 4](https://github.com/UniDive/2026-UniDive-Yerevan-training-school/tree/main/Diversity-quantification-course/session-4-measuring-meta-linguistic-diversity-in-nlp)
- click on the file with the `.ipynb` extension, programmers' or non-programmers' version, depending on your profile; - if you are autonomous in Python programming, select the programmers' version, otherwise, select the non-programmers' version
- when the file opens, download it (with the download icon in the upper right-hand corner)
- open [Google Colab](https://colab.google/), click on `Open Colab`, then `Upload`, select the file from your computer
- read through the instructions; when you come to a cell containing code (in Python), hower over it; a "play" icon appears in the upper left-hand corner; click on it to execute the code
- the cells of code need to be run sequentially; don't miss any of them, otherwise errors (in red) might occur


 



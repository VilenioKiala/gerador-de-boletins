# Book Report Generator From Angola

[English](README.en.md) | [Português](README.md)

**Book Report Generator From Angola** is a project focused on creating an school book report for schools in Angola (where i'm from). It uses the data provided by the user on terminal like the **student name**, **grade**, **school year**, **the subjects with the corresponding grades**.

The app is fully on terminal and it generates an excel file in the end with the corresponding Book Report.

## Requirements

In order to run this project you need to have the following apps installed:

- Windows;
- Python;
- Git (optional);
- Winrar (optional, if you don't have Git)

## How to install

Here I teach you step-by-step how to install this project:

### Step 1: Download this repository

Download this repository by clicking on **<> Code** and **Download Zip** and then extract it on any folder. Or, if you have Git installed on your computer, just open you terminal (CMD on Windows), and insert this command on the folder you want to save:
`git clone https://github.com/VilenioKiala/gerador-de-boletins.git`

### Step 2: Install All the required packages

With the **Python** installed, open your terminal on the project folder and then run this command:
`pip install -r requirements.txt`

### Everything fine

Now that you have all set up, let's take a look on how to use it.

## How to use it

On the project folder, open the file **launcher.bat** or just **launcher** to initialize the app, respond all the question and it will generate an excel file containing the Book Report ready to be printed.

### The questions translated

- Digite o Nome do aluno (ou digite q para sair do programa) - Insert the student name (or insert q to quit)
- Digite a classe do aluno(em número inteiro) (ou digite q para sair do programa) - Insert the student grade(integer number) (or insert q to quit)
- Digite o trimestre (em numero inteiro) (ou digite q para sair do programa) - Insert the trimester(integer number) (or insert q to quit)
- Digite o Ano_lectivo (ou digite q para sair do programa) - Insert the school year (or insert q to quit)
- Ok, agora forneça as disciplinas e as respectivas notas - Ok, now insert the subjects with the grades.
- Digite a disciplina (ou digite q para sair do programa) - Insert the subject (or insert q to quit)
- Digite a nota para a disciplina de "disciplina inserida" - Insert the grade in subject "subject inserted"

It will be a loop of subjects and grades until you press q to quit.

When you quit, it will generate an excel file with the book report all organized like the book reports in Angola.

Thank you so much for seeing my project.

Vilénio Kiala

# My First Snakemake Workflow

## Description
A simple Snakemake workflow for homework that runs a Python script and saves the output to a file.

## Requirements
- Git
- Python 3 + pip
- Snakemake (pip install snakemake)

## How to Run
1. Clone the repository and switch to the branch:
   ```
   git clone https://github.com/sherifimari-bit/sherifimari-homework.git
   cd sherifimari-homework
   git checkout add-workflow
   ```
2. Install Snakemake (if not installed):
   ```
   pip install snakemake
   ```
3. Run the workflow:
   ```
   snakemake --cores 1
   ```
4. Check the result:
   ```
   cat results/hello_output.txt
   ```

## Expected Output
After running the workflow, the file `results/hello_output.txt` will contain:
```
Hello world from Snakemake workflow!
========================================
Скрипт запущен: scripts/hello.py
Текущая дата: [current date and time]
```

## Author
Maria Sherifi
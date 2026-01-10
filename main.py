# Simple Snakemake workflow for homework
# This workflow creates a summary of a CSV file

rule all:
    input:
        "results/summary.txt",
        "results/plot.png"

rule clean_data:
    input:
        "data/input.csv"
    output:
        "results/cleaned.csv"
    shell:
        """
        echo "Cleaning data..."
        # Simple cleaning - remove empty lines
        grep -v '^$' {input} > {output}
        echo "Rows in cleaned file:" >> results/log.txt
        wc -l {output} >> results/log.txt
        """  

rule analyze_data:
    input:
        "results/cleaned.csv"
    output:
        "results/summary.txt"
    shell:
        """
        echo "=== Data Analysis Summary ===" > {output}
        echo "Generated on: $(date)" >> {output}
        echo "" >> {output}
        echo "File statistics:" >> {output}
        echo "----------------" >> {output}
        wc -l {input} >> {output}
        echo "" >> {output}
        echo "First 5 lines:" >> {output}
        echo "-------------" >> {output}
        head -n 5 {input} >> {output}
        """

rule create_plot:
    input:
        "results/cleaned.csv"
    output:
        "results/plot.png"
    script:
        "scripts/create_plot.py"

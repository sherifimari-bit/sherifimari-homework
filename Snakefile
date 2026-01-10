rule all:
    input:
        "hello_output.txt"

rule print_hello:
    output:
        "hello_output.txt"
    shell:
        "python scripts/hello.py > {output}"
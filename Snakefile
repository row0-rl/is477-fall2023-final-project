rule prepare:
    output:
        "data"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

rule analyze:
    output:
        "results/odor.png"
    shell:
        "python scripts/analyze.py"
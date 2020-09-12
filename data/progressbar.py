def printProgressBar(iteration: int, total: int, prefix: str = "", suffix: str = '', decimals: int = 0, length: int = 100, fill: str = "█", printEnd: str = ""):
    """
    Call in a loop to create terminal progress bar https://stackoverflow.com/a/34325723
        iteration   - Required  : current iteration
        total       - Required  : total iterations
        prefix      - Optional  : prefix string
        suffix      - Optional  : suffix string
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\\r", "\\r\\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total))).rjust(4 + decimals if decimals > 0 else 3)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

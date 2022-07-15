import os
import shutil

from pathlib import Path

downloadsFolder = Path("/home/luismeza/Downloads/")
documentsFolder = Path("/home/luismeza/Documents/")


def sort():
    for file in os.listdir(downloadsFolder):
        if file[:3].lower() == "cal":
            shutil.move(downloadsFolder/file, documentsFolder/"Calculo/")

        elif file[:2].lower() == "mc":
            shutil.move(downloadsFolder/file, documentsFolder /
                        "MatesComputacionales/")


sort()

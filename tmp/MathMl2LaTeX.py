import os

def mml2latex(file):
    """
    (str) -> str
    :param file: path to file containing MathMl code
    :return: string of LaTeX code
    """
    prompt = "xsltproc mathml_2_latex/mmltex.xsl " + file
    return os.popen(prompt).read()

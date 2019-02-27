import os

def mml2latex(mml):
    """
    (str) -> str
    :param mml: mml code in str representation
    :return: string of LaTeX code
    """
    file = open("tmp.mml", "w")
    print(mml, file=file)
    file.close()
    prompt = "xsltproc mathml_2_latex/mmltex.xsl " + "tmp.mml"
    return os.popen(prompt).read()

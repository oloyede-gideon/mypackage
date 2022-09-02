def dna_complementary(dna):
    """Return th e top n items in abn array in descending order

    Args:
    items(array):

    Return:
    array
    """
    # your code here
    compl = []
    anser = ""
    dna_ch = { "A":"T",
                "T": "A",
                "C": "G",
                "G": "C" }
    for k in dna:
        compl.append(dna_ch[k])
        
    return anser.join(compl)

from modulefinder import Module
from mypackage import myModule

def test_dna_complementary():
    """ Making sure bcode runs correctly"""


    assert myModule.dna_complementary('ATCGGACTACGA') == 'TAGCCTGATGCT', 'incorrect'
    assert myModule.dna_complementary('TCCCGGATCGCATACGAT') == 'AGGGCCTAGCGTATGCTA', 'incorrect'
    assert myModule.dna_complementary('ATCTTATAATTACCGAGTCGATCGG') == 'TAGAATATTAATGGCTCAGCTAGCC', 'incorrect'

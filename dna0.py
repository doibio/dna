def ascii_to_dna(text):
    text = text.upper()
    ascii_start = 32
    ascii_end = 126
    dna_triplets = [
        'AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT',
        'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT',
        'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT',
        'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT',
        'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT',
        'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT',
        'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT',
        'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT'
    ]

    ascii_values = [ord(char) for char in text]

    for value in ascii_values:
        if ascii_start <= value <= ascii_end:
            index = value - ascii_start
            dna_sequence += dna_triplets[index]
        else:
            raise ValueError(f"Character '{chr(value)}' at ASCII {value} out of mappable range 32-126")

    return dna_sequence

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    try:
        dna_result = ascii_to_dna(text)
        print("DNA Sequence:", dna_result)
    except ValueError as e:
        print(e)

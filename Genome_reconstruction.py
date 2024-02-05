# Import necessary modules
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import vcf
 
# Open VCF file
vcf_file_path = "path/Variant_file.vcf"
vcf_reader = vcf.Reader(filename=vcf_file_path)
 
# Filter variants based on quality (QUAL) threshold
filtered_variants = [record for record in vcf_reader if record.QUAL is not None and record.QUAL >= 20]
 
# Print details of the first 5 variants
for variant in filtered_variants[:5]:
    print("Chromosome: {}, Position: {}, ID: {}, Ref: {}, Alt: {}, Quality: {}".format(
        variant.CHROM, variant.POS, variant.ID, variant.REF, variant.ALT, variant.QUAL))
 
# Reference fasta file path
ref_fasta_path = "path/reference_sequence.fasta"
genome = SeqIO.read(ref_fasta_path, "fasta")
ref_sequence = str(genome.seq)
 
# Open and read the first few lines of the reference fasta file
with open(ref_sequence, "r") as ref_file:
    for _ in range(5):  # Print the first 5 lines
        print(ref_file.readline().strip())
 
 
# Define function to extract sequence based on variant
def extract_sequence(ref_sequence, variant_position, variant_sequence):
    """
    Extracts the individualized sequence based on a genetic variant.
 
    Parameters:
    - ref_sequence: Original reference DNA sequence.
    - variant_position: Position of the genetic variant.
    - variant_sequence: Alternative sequence introduced by the genetic variant.
 
    Returns:
    - Individualized DNA sequence.
    """
    return ref_sequence[:variant_position - 1] + variant_sequence + ref_sequence[variant_position + len(variant_sequence):]
# ref_sequence[:variant_position - 1]: This part extracts the portion of the reference sequence from the beginning up to (but not including) the position of the genetic variant.
# variant_sequence: This part adds the alternative sequence introduced by the genetic variant.
# ref_sequence[variant_position + len(variant_sequence):]: This part extracts the portion of the reference sequence from the position after the genetic variant to the end.
 
# Initialize list to store individualized sequences
individualized_sequences = []
 
# Process each variant and create individualized sequences
for variant in filtered_variants:
    variant_position = variant.POS
    if variant.ALT:
        variant_sequence = str(variant.ALT[0])
        ind_sequence = extract_sequence(ref_sequence, variant_position, variant_sequence)
        individualized_sequences.append(ind_sequence)
        print("Variant: {}, Variant Position: {}, Variant Sequence: {}, Individualized Sequence: {}".format(
            variant, variant_position, variant_sequence, ind_sequence))
    else:
        print("Skipping variant {} due to missing ALT information.".format(variant))
 
 
# Initialize individualized sequence with the original reference sequence
individualized_sequence = ref_sequence
 
# Iterate over filtered variants and modify the individualized sequence
for variant in filtered_variants:
    variant_position = variant.POS
    if variant.ALT:
        variant_sequence = str(variant.ALT[0])
        individualized_sequence = extract_sequence(individualized_sequence, variant_position, variant_sequence)
    else:
        print("Skipping variant {} due to missing ALT information.".format(variant))
 
# Print the final individualized sequence
print("Final Individualized Sequence:", individualized_sequence)

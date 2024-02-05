
# Download VCF file
wget -O Chr17_sites.vcf "https://storage.googleapis.com/gcp-public-data--gnomad/release/4.0/vcf/genomes/gnomad.genomes.v4.0.sites.chr17.vcf.bgz"
# Download TBI file
wget -O Chr17_sites.vcf.tbi "https://storage.googleapis.com/gcp-public-data--gnomad/release/4.0/vcf/genomes/gnomad.genomes.v4.0.sites.chr17.vcf.bgz.tbi"
# Check MD5 for VCF file
md5sum chr17_sites.vcf

# Check MD5 for TBI file
md5sum chr17_sites.vcf.tbi

# Download Chromosome 17
wget -O chr17.fasta "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=NC_000017.11&db=nuccore&report=fasta&extrafeat=976&fmt_mask=0&maxplex=1&toolbar=0&extrafeatfeats=976&log%24=seqview&tracklabel=Chr17&search=&filenum=1"


import vcf

def extract_variants_in_interval(vcf_file, genome_fasta, genomic_interval, output_file):
    """
    Extract variants within a specified genomic interval for a given individual.

    Args:
    - vcf_file (str): Input VCF file.
    - genome_fasta (str): Reference genome FASTA file.
    - genomic_interval (str): Genomic interval in the format "chromosome:start-end".
    - output_file (str): Output file for the generated sequence.

    Returns:
    - None
    """
    # Open the VCF file for reading
    vcf_reader = vcf.Reader(filename=vcf_file)

    # Extract variants within the specified genomic interval
    variants_in_interval = [record for record in vcf_reader if genomic_interval == f"{record.CHROM}:{record.POS}-{record.POS + len(record.ALT[0]) - 1}"]

    # Create a dictionary to store alternate alleles for each position
    variants_dict = {record.POS: record.ALT[0] for record in variants_in_interval}

    # Open the reference genome FASTA file for reading
    with open(genome_fasta, 'r') as fasta_file:
        # Extract the sequence within the genomic interval
        sequence = ""
        for line in fasta_file:
            if line.startswith(">"):
                continue
            sequence += line.strip()

    # Generate the sequence with alternate alleles for variant positions
    for variant_position, alternate_allele in variants_dict.items():
        position = variant_position - 1
        sequence = sequence[:position] + str(alternate_allele) + sequence[position + len(alternate_allele):]

    # Write the generated sequence to the output file
    with open(output_file, 'w') as output:
        output.write(f">{genomic_interval}\n")
        output.write(sequence)

def main():
    # Input VCF file
    vcf_file = "Chr17_sites.vcf"

    # Reference genome FASTA file
    genome_fasta = "reference_genome.fasta"

    # Genomic interval in the format "chromosome:start-end"
    genomic_interval = "chr17:1000000-2000000"

    # Output file for the generated sequence
    output_file = "reconstructed_sequence.fasta"

    # Extract variants within the specified genomic interval and generate the sequence
    extract_variants_in_interval(vcf_file, genome_fasta, genomic_interval, output_file)

if __name__ == "__main__":
    main()

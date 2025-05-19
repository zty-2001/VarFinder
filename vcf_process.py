def vcfline2snpindex(vcfline):
    line = vcfline.strip().split('\t')
    dp4 = line[-3].split(';')[-2].split('=')[1].split(',')
    snp_index = (int(dp4[-1]) + int(dp4[-2])) / (int(dp4[0]) + int(dp4[1]) + int(dp4[2]) + int(dp4[3]))
    # print(snp_index)
    return snp_index



def load_gff3file():
    print('Loading gff3 file ...')
    file = "./Zm-B73-REFERENCE-GRAMENE-4.0_Zm00001d.2.gff3"
    with open(file) as f:
        gene_anno = {}
        gene1 = {}
        gene2 = {}
        gene3 = {}
        gene4 = {}
        gene5 = {}
        gene6 = {}
        gene7 = {}
        gene8 = {}
        gene9 = {}
        gene10 = {}
        for line in f:
            if '#' not in line:
                if line.split('\t')[2] == 'gene':
                    gene_id = line.split('ID=gene:')[1].split(';')[0]
                    chr = line.split('\t')[0]
                    start = line.split('\t')[3]
                    end = line.split('\t')[4]
                    if 'Chr' in chr:
                        if chr.replace('Chr', '') == str(1):
                            gene1[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(2):
                            gene2[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(3):
                            gene3[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(4):
                            gene4[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(5):
                            gene5[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(6):
                            gene6[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(7):
                            gene7[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(8):
                            gene8[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(9):
                            gene9[gene_id] = [start, end]
                        if chr.replace('Chr', '') == str(10):
                            gene10[gene_id] = [start, end]
        gene_anno['1'] = gene1
        gene_anno['2'] = gene2
        gene_anno['3'] = gene3
        gene_anno['4'] = gene4
        gene_anno['5'] = gene5
        gene_anno['6'] = gene6
        gene_anno['7'] = gene7
        gene_anno['8'] = gene8
        gene_anno['9'] = gene9
        gene_anno['10'] = gene10

        return gene_anno


def search_gene(gene_anno,chr, pos):

    chr_num_str = str(chr.replace('Chr', ''))
    if chr_num_str == '1':
        for gene_id in gene_anno['1']:
            if int(gene_anno['1'][gene_id][0]) <= int(pos) <= int(gene_anno['1'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif  chr_num_str == '2':
        for gene_id in gene_anno['2']:
            if int(gene_anno['2'][gene_id][0]) <= int(pos) <= int(gene_anno['2'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif chr_num_str == '3':
        for gene_id in gene_anno['3']:
            if int(gene_anno['3'][gene_id][0]) <= int(pos) <= int(gene_anno['3'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif  chr_num_str == '4':
        for gene_id in gene_anno['4']:
            if int(gene_anno['4'][gene_id][0]) <= int(pos) <= int(gene_anno['4'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif chr_num_str == '5':
        for gene_id in gene_anno['5']:
            if int(gene_anno['5'][gene_id][0]) <= int(pos) <= int(gene_anno['5'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif chr_num_str == '6':
        for gene_id in gene_anno['6']:
            if int(gene_anno['6'][gene_id][0]) <= int(pos) <= int(gene_anno['6'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif chr_num_str == '7':
        for gene_id in gene_anno['7']:
            if int(gene_anno['7'][gene_id][0]) <= int(pos) <= int(gene_anno['7'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif  chr_num_str == '8':
        for gene_id in gene_anno['8']:
            if int(gene_anno['8'][gene_id][0]) <= int(pos) <= int(gene_anno['8'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif chr_num_str == '9':
        for gene_id in gene_anno['9']:
            if int(gene_anno['9'][gene_id][0]) <= int(pos) <= int(gene_anno['9'][gene_id][1]):
                return gene_id
            else:
                return '.'
    elif chr_num_str == '10':
        for gene_id in gene_anno['10']:
            if int(gene_anno['10'][gene_id][0]) <= int(pos) <= int(gene_anno['10'][gene_id][1]):
                return gene_id
            else:
                return '.'



def main(vcf_file_in):
    gene_anno_dict = load_gff3file()
    with open(vcf_file_in, 'r') as f:
        with open(vcf_file_in.replace('.vcf', '.out.vcf'), 'w') as f_out:
            for line in f:
                if line.startswith('#'):
                    f_out.write(line)
                else:
                    if 'Chr' in line:
                        chr = line.strip().split('\t')[0]
                        pos = line.strip().split('\t')[1]
                        gene_id = search_gene(gene_anno_dict, chr, pos)
                        snp_index = vcfline2snpindex(line)
                        line_out = str(snp_index) + '\t' + gene_id + '\t' + line
                        f_out.write(line_out)



def mutation_type_check(input_file, output_file):
    print('Starting mutation_type_check ...')
    f_out = open(output_file, 'w')
    with open(input_file, 'r') as f_in:
        for line in f_in:
            ref = line.split('\t')[3]
            alt = line.split('\t')[4]
            if ref == 'G' and alt == 'A' or ref == 'C' and alt == 'T':  # EMS突变规则
                f_out.write(line)
        f_out.flush()
        f_out.close()


if __name__ == '__main__':
    vcf_file = '324.cleaned.vcf'
    mutation_type_check(vcf_file, vcf_file.replace('.vcf', '.filter.vcf'))
    main(vcf_file.replace('.vcf', '.filter.vcf'))
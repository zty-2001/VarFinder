#/usr/bin/python
import argparse
import os
import subprocess
from vcf_process import mutation_type_check
from vcf_process import main as vcf_process

def varfinder_file_check(bk_path,ref_path):
    if os.path.exists(bk_path):
        print('Background B73WTqc check : OK ')
    if os.path.exists(ref_path):
        print('Reference B73_v4 check : OK ')

def varfinder_mutant(name_mutant, fq1, fq2, perl_path):
    """
    运行VarFinder工具来检测突变。

    该函数使用给定的突变体名称、成对的fastq文件和Perl路径，
    通过调用VarFinder相关的脚本来识别和处理基因突变。

    参数:
    name_mutant -- 突变体的名称
    fq1 -- 第一个fastq文件的路径
    fq2 -- 第二个fastq文件的路径
    perl_path -- Perl脚本所在的路径
    """
    # 定义B73参考基因组路径
    b73_ref_path = '/mnt/e/varfinder_data/Zm-B73-REFERENCE-GRAMENE-4.0.fasta'
    # 定义背景变异的VCF文件路径
    background_path = '/mnt/e/varfinder/VarFinder-main/B73WTqc_output/B73WTqc.vcf'

    # 检查必要的参考文件是否存在
    varfinder_file_check(background_path, b73_ref_path)

    # 构建运行VarFinder_mutant的命令
    cmd_mutant = f'perl {perl_path}/VarFinder_mutant {name_mutant} {fq1},{fq2} {b73_ref_path} 100 2 90'
    # 构建运行bkRemover.pl移除背景变异的命令
    cmd_remove = (f'perl {perl_path}/bkRemover.pl {perl_path}/{name_mutant}_output/{name_mutant}.vcf '
                  f'{background_path} {perl_path}/{name_mutant}_output/{name_mutant}.cleaned.vcf')

    try:
        # 执行VarFinder_mutant命令
        result_mutant = subprocess.run(cmd_mutant, shell=True)
        if result_mutant.returncode == 0:
            # 如果执行成功，则移除背景变异
            result_remove = subprocess.run(cmd_remove, shell=True)
            if result_remove.returncode == 0:
                # 如果移除背景变异成功，则进行下一步处理
                print(f'{name_mutant} VarFinder_mutant done... \n prepare to run next step')
                # 检查突变类型并处理VCF文件
                mutation_type_check(
                    f'{perl_path}/{name_mutant}_output/{name_mutant}.cleaned.vcf',
                    f'{perl_path}/{name_mutant}_output/{name_mutant}.cleaned.filter.vcf')
                vcf_process(f'{perl_path}/{name_mutant}_output/{name_mutant}.cleaned.filter.vcf')
    except Exception as e:
        # 异常处理，打印错误信息
        print(e)



def main(args):
    """
    主函数，用于执行变异检测流程。

    检查VarFinder Perl脚本路径是否存在且为目录，如果条件满足，则调用varfinder_mutant函数进行变异检测；
    否则，输出错误信息"perl_Path_Error"。

    参数:
    - args: 命令行参数对象，包含以下属性：
        - name: 样本名称。
        - fastq1: 第一个FASTQ文件路径。
        - fastq2: 第二个FASTQ文件路径。
    """
    # 定义VarFinder Perl脚本的路径
    perl_script_path = '/mnt/e/varfinder/VarFinder-main'

    # 检查Perl脚本路径是否存在且为目录
    if os.path.exists(perl_script_path) and os.path.isdir(perl_script_path):
        # 调用varfinder_mutant函数进行变异检测
        varfinder_mutant(args.name, args.fastq1, args.fastq2, perl_script_path)
    else:
        # 如果路径不存在或不是目录，输出错误信息
        print("perl_Path_Error")



if  __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog= 'VarFinder_auto script',
        description='using this script, you can run VarFinder pipline by one cmd.',
    )
    parser.add_argument('-n', '--name', dest='name', type=str, help='input your mutant name')
    parser.add_argument('-fq1', '--fastq1', dest='fastq1', type=str, help='input your fastq1 file')
    parser.add_argument('-fq2', '--fastq2', dest='fastq2', type=str, help='input your fastq2 file')
    arg = parser.parse_args()
    main(arg)


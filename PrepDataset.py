import glob
import os
import argparse
from tqdm import tqdm
import shutil

#Argument Parser
def process_command_line_arguments() -> argparse.Namespace:
    """Parse the command line arguments and return an object with attributes
    containing the parsed arguments or their default values.
    """

    parser = argparse.ArgumentParser()

    #Global Params
    parser.add_argument("-input", "--input", dest="input", metavar="INPUT", 
                        type=str, help="Input Folder Containing extracted files")
    parser.add_argument("-outputi", "--outputi", dest="outputi", metavar="OUTPUTI", 
                        type=str, help="Where to place input files")
    parser.add_argument("-outputt", "--outputt", dest="outputt", metavar="OUTPUTT", 
                        type=str, help="Where to place target files")
    

    args = parser.parse_args()
    if not os.path.exists(args.input):
        raise SystemExit(
            "Error: Input file '{}' does not exist".format(args.input))
    if not os.path.exists(args.outputi):
        raise SystemExit(
            "Error: Input file '{}' does not exist".format(args.outputi))
    if not os.path.exists(args.outputt):
        raise SystemExit(
            "Error: Input file '{}' does not exist".format(args.outputt))

    return args

def main():
    args = process_command_line_arguments()

    #vars
    root = args.input
    desti = args.outputi
    destt = args.outputt

    #convert to alligned dataset structure
    input_names = sorted(glob.glob(root + '*.jpg', recursive = True)) #get file names
    target_names = sorted(glob.glob(root + '*.pth', recursive = True))
    for j in tqdm(range(len(input_names))):
        tmp = input_names[j].split("/")
        P2Pformat = desti + tmp[-1] #new file structure
        shutil.copy(input_names[j], P2Pformat)
        tmp = target_names[j].split("/")
        P2Pformat = destt + tmp[-1] #new file structure
        shutil.copy(target_names[j], P2Pformat)




if __name__ == '__main__':
    main()
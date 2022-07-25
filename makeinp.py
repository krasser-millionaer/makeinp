#!/usr/bin/env python3
import os, re
from argparse import ArgumentParser
try:
    import input_blocks
except ImportError:
    print("No input_blocks.py module found! Check your installation")
import time


start = time.perf_counter()

SUPPORTED_EXTENSIONS = (".out", ".log", ".xyz")


class Reader:

    def __init__(self, filename,append):
        self.filename = os.path.splitext(filename)[0]
        self.intial_extention = os.path.splitext(filename)[1]
        self.nats, self.molname, self.atoms, self.filedata, self.struc_list = 0, "", [], [], []
        self.spe_dict = {}
        self.spe = 0
        self.append = append

    def read_xyz(self):
        """
        Read an XMOL-formatted xyz-file
        """
        print(f"Reading {self.filename}.xyz")
        with open(self.filename + self.intial_extention, "r") as f:
            self.filedata = f.readlines()
        self.nstruc = 0
        while self.filedata:
            try:
                self.nats = int(self.filedata[0].strip("\n"))
                self.molname = self.filedata[1].strip("\n"),
                self.atoms = self.filedata[2:2 + self.nats]
                self.struc_list.append(
                {   "nstruc": self.nstruc,
                    "nats": self.nats,
                    "molname": self.molname,
                    "atoms": self.atoms
                })

                self.filedata = self.filedata[2+self.nats:]
            except IndexError:
                self.filedata = []
            finally:
                print(f"Succesfully read structure {self.nstruc} from file {self.filename}{self.intial_extention}")
                self.nstruc +=1


    def read_orca_opt(self):
        """
        Retrieve the geometry of the last optimization step
        """
        print(f'Reading {self.filename}{self.intial_extention}')
        # final_spe = re.compile("final single point energy.*(-[0-9]+.[0-9]+).*")
        geom_pattern_start = re.compile("CARTESIAN COORDINATES \(ANGSTROEM\)")
        geom_pattern_stop = re.compile("CARTESIAN COORDINATES \(A\.U\.\)")
        with open(self.filename + self.intial_extention, "r") as f:
            filedata = f.readlines()

        angs_coords_list, au_coords_list = [], []
        for i, a in enumerate(filedata):
            if re.search(geom_pattern_start, a):
                angs_coords_list.append(i)
            elif re.search(geom_pattern_stop, a):
                au_coords_list.append(i)

        zipped = list(zip(angs_coords_list, au_coords_list))

        self.atoms = filedata[zipped[-1][0]+2:zipped[-1][1]-2:]
        self.nats = zipped[-1][0] - zipped[-1][1] - 4
        self.molname = self.filename
        self.struc_list.append(
            {"nats": self.nats,
             "molname": self.molname,
             "atoms": self.atoms
             })


class Writer(Reader):

    def write_inp(self, ctrlstr, charge, multiplicity, procs, mem, preblocks=None):
        for item in self.struc_list:
            if len(self.struc_list) > 1:
                self.append = f"{self.append}_{item['nstruc']}"
            print(f'Writing {self.filename}{self.append}.inp')
            with open(f"{self.filename}{self.append}.inp", "w") as inpf:
                inpf.write(f'!{ctrlstr}\n')
                inpf.writelines([f'%pal nprocs {procs} end\n', f'%maxcore {mem}\n\n'])
                if preblocks:
                    for prb in preblocks:
                        inpf.writelines(prb)
                        inpf.write("\n")
                inpf.write(f'* xyz {charge} {multiplicity}\n')
                inpf.writelines(item["atoms"])
                inpf.write('*\n\n')
            self.append = self.append.split("_")[0]

    def write_xyz(self):
        """
        Writes a simple XMOL-formatted xyz-file
        """
        print(f'Writing {self.filename}{self.append}.xyz')
        with open(f"{self.filename}{self.append}.xyz", "w") as xyz:
            xyz.write(f"{self.nats}\n")
            xyz.write(f"{self.molname}, E={self.spe}\n")
            xyz.writelines(self.atoms)


def main():
    parser = ArgumentParser()
    parser.add_argument("--ctrlstr", dest="CRTLSTR", help="Control string of your job",required=True)
    parser.add_argument("--mem", dest="MEM", help="Memory in MB per core", default=4000)
    parser.add_argument("--nprocs", dest="NPROCS", help="Number of cores", default=24)
    parser.add_argument("--chrg", dest="CHRG", default=0, type=int, help="Charge of the molecule")
    parser.add_argument("--mult", dest="MULT", default=1, type=int, help="Multiplicity of the molecule")
    parser.add_argument("--block", dest="BLOCK", action="append", nargs="+", type=str, help="Add block without %%")
    parser.add_argument("--append", dest="APP", help="String to append to the filename", default="")
    parser.add_argument("--rename", dest="RENAME", help="String to rename your file, no extension", default="")
    parser.add_argument("--xyz", dest="XYZOUT", help="Export the structure into XYZ", action="store_true", default=False)
    parser.add_argument("--inp", dest="INP", help="Export the structure into INP", action="store_true", default=False)
    parser.add_argument("source", help="files to extract geometries and convert to inputs", nargs='*')
    (options, args) = parser.parse_known_args()


    preblocks = []

    if options.BLOCK:
        for block_item in options.BLOCK:
            block = input_blocks.InputBlock(block_item)
            preblocks.append(block.make_block())



    for file in options.source:
        obj = Writer(file,options.APP)
        if obj.intial_extention.lower() in SUPPORTED_EXTENSIONS:
            if obj.intial_extention.lower() == ".xyz":
                obj.read_xyz()
            elif obj.intial_extention.lower() == ".log" or obj.intial_extention.lower() == ".out":
                obj.read_orca_opt()

            if options.RENAME:
                obj.filename = options.RENAME
            if options.INP:
                obj.write_inp(charge=options.CHRG, multiplicity=options.MULT, ctrlstr=options.CRTLSTR, mem=options.MEM,
                              procs=options.NPROCS, preblocks=preblocks)
            elif options.XYZOUT:
                obj.write_xyz()
        else:
            print(f"Extension {obj.intial_extention.lower()} is not supported!")
            pass


if __name__ == '__main__':
    main()
    print(f"Script execution time: {round(time.perf_counter() - start, 6)} seconds.")

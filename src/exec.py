import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--time", "-t", default = 60*15, type=int)
args = parser.parse_args()

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
BIN_DIR = os.path.join( BASE_DIR, 'bin' )

data_path = os.path.join( DATA_DIR, 'data_report.csv' )
bin_path = os.path.join( BIN_DIR , 'speedtest-csv')

if not os.path.exists( data_path ):
    call = "{command} --header --sep ';' > {data_path}"
    call = call.format( command = bin_path, data_path=data_path )
    os.system( call )

while True:
    call = "{command} --sep ';' >> {data_path}"
    call = call.format( command = bin_path, data_path=data_path )
    os.system( call )
    time.sleep(args.time)
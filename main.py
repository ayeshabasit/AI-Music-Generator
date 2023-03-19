import urllib
import zipfile
import nottingham_util
import argparse
#import rnn

# collect the data
url = "http://www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
urllib.urlretrieve(url, "dataset.zip")

zip = zipfile.ZipFile(r'dataset.zip')  
zip.extractall('data')  

# build the model by taking user input about number of tracks available
parser = argparse.ArgumentParser()
parser.add_argument("NumTracks", type = int)
args = parser.parse_args()
nottingham_util.create_model(args.NumTracks)

# train the model
#rnn.train_model()

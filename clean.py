import glob
import os
import torch
os.system('clear')
def Del():
 for f in files:
    os.remove(f)
current_directory = os.path.dirname(os.path.abspath(__file__))
files = glob.glob( os.path.join(current_directory, 'Op/*'))
Del()
files = glob.glob( os.path.join(current_directory, 'Anotated/*'))
Del()
files = glob.glob( os.path.join(current_directory, 'data/*'))
Del()
if torch.cuda.is_available:
    torch.cuda.empty_cache()
print('Done')
# You need to install the progress package first
from progress.bar import Bar#install module 'pip install progress'
import time

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(0.1)
    bar.next()
bar.finish()
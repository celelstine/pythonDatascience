import os
import tempfile

tmpdir = tempfile.gettempdir()

print(tmpdir)

# store existing directory path
workingDir = os.getcwd()
print('current working directory is:', os.getcwd())

# change current working directory to the temporary path
os.chdir(tmpdir)
print('current working directory is:', os.getcwd())

# build a new path from the project directory
mytmpdir = os.path.join(workingDir, 'learnDatascience')

# check if the folder exist else create it
if not os.path.exists(mytmpdir):
  os.mkdir(mytmpdir)

# create a file in the new create directory 
sweetWordsfile = os.path.join(mytmpdir, 'sweetWords.txt')

# create some sweet lines
awesome_lines = [
  "God is the being behind all good thought and deed",
  "sometime, Human have deny themselves the opportnuity to enjoy God's favour",
  "I believe in Love"
]

#  write these lines to the file: open it with the intention to write into it
# we love using a context which would close the connection to the file when we are done
with open(sweetWordsfile, 'w') as fileWriter:
  for line in awesome_lines:
    fileWriter.write(line + "\n")

# let us read the lines 
with open(sweetWordsfile, 'r') as fileReader:
  for line in awesome_lines:
    print(line)

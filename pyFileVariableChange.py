import os


def changeSettingsAndSend(fileToModify, variableToChange, valueToChange, pathToSend=None):
    """Opens a .py file, modifies a variable, and saves the file. 
    If no pathToSend is specified, returns the file.
    If pathToSend is specified, saves the file.

    Parameters:
    argument1 (int): Description of arg1
    fileToModify (str): Absolute filepath of file to read and modify
    variableToChange (str): The name of the variable to change
    valueToChange (str): The new value for the variable.
    pathToSend (str): Absolute filepath of the file to save as.

    Returns:
    str:String containing original .py file with updated variable.

    """

    def saveFile(pathToSaveAs, contentToSave):

        print(pathToSaveAs)

        destinationFolder, destinationFilename = os.path.split(pathToSaveAs)

        print(destinationFolder, destinationFilename)

        # Handle folder creation or skipping
        if os.path.exists(destinationFolder):
            print('Folder already exists - skipping folder creation')
        else:
            os.makedirs(destinationFolder, exist_ok=True)


        # Handle file saving - 
        if os.path.exists(pathToSaveAs):
            print('File with that name exists. Overwrite?')
            overwrite_choice = input('Y or N: ')
            if overwrite_choice.lower() in ('y', 'yes'):

                with open(pathToSaveAs, 'w') as dest:
                    dest.write(contentToSave)
                    
                print('Saved')


            else:
                filename, ext = os.path.splitext(destinationFilename)
                appendix_count = 1
                while True:
                    newFilename = f'{filename}_{appendix_count}{ext}'
                    newFilename_withPath = os.path.join(destinationFolder, newFilename)


                    if os.path.exists(newFilename_withPath):
                        appendix_count += 1
                    else:
                        break

                with open(newFilename_withPath, 'w') as dest:
                    dest.write(contentToSave)
                    
                print(f'Saved at {newFilename_withPath}')
        
        else:
            
            with open(pathToSaveAs, 'w') as dest:
                    dest.write(contentToSave)
                    
            print(f'Saved at {pathToSaveAs}')


    
        os.path.exists(pathToModify)
        
    ### Error handling - make sure the file put in is a real file!
    pathToModify_exists_check = os.path.exists(pathToModify)
    if pathToModify_exists_check == False:
        raise FileNotFoundError(f'{pathToModify} does not exist')

    ### Make sure the file is a python file.
    pathToModify_pythonFile_check = pathToModify.endswith('.py')
    if pathToModify_exists_check == False:
        raise FileNotFoundError(f'{pathToModify} file is not a .py file')


    with open(fileToModify, 'r') as pythonFile:
        PyFile_contents = pythonFile.readlines()

    
    ### Using range/len so we can access the indexes easily
    found_variable = False
    for L in range(len(PyFile_contents)):
        line = PyFile_contents[L]

        #### Using strip to clear off newline chars so we can use startswith
        #### And using startswith so we don't change any 'self.' lines
        if line.strip().startswith(variableToChange):

            lineToChange_Index = L
            found_variable = True

            ### And break so we only catch the first instance.
            break
    
    
    ### If the variable isn't in the file, raise an exception
    if found_variable == False:
        raise Exception(f'Variable {variableToChange} was not found.')

    lineToChange_split = PyFile_contents[lineToChange_Index].split('=') # Use split to preserve the indentation at the beginning of the line

    lineToChange_split[-1] = f'{valueToChange}\n' # Make variable change
    updatedVariableLine = '='.join(lineToChange_split) # Reconstruct variable line

    PyFile_contents[lineToChange_Index] = f'{updatedVariableLine}' #Update original 'contents' list

    updatedPythonFile = ''.join(PyFile_contents) #Combine updated list into new string

    if pathToSend:
        saveFile(pathToSend, updatedPythonFile)
    else:      
        return updatedPythonFile


# Name/main to allow you to use this code on its own, or import the function into other python files
if __name__ == '__main__':

    # testPath = r'C:\Users\User\.spyder-py3\Fiverr\pairSettingsClass.py'
    # testVariable = 'ObDepth'
    # testValue = '20'

    print('\nimpacChangeSettingsAndSend -----------\n\n')

    print('Enter path to .py file to modify:')
    while True:
        pathToModify = input()
        if pathToModify:
            break
    
    print('Enter variable to change:')
    while True:
        variableToChange = input()
        if variableToChange:
            break

    print('Enter the new value for the variable:')
    while True:
        valueToChange = input()
        if valueToChange:
            break
        
    print('Enter the destination path to save to, or enter S or SAME to use the input file path:')
    while True:
        pathToSend = input()
        if pathToSend:
            if pathToSend.lower() in ('s', 'same', 'sam', 'sa'):
                pathToSend = pathToModify
            break



    changeSettingsAndSend(pathToModify, variableToChange, valueToChange, pathToSend)

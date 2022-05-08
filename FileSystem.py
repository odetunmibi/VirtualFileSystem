class VirtualFileSystem:
    # initializing file system, current directory and the directory stack
    def __init__(self):
        self.rootDirectory = {}
        self.currentDirectory = self.rootDirectory
        self.dirStack = [self.currentDirectory]

    # mkdir command
    def set_new_directory(self, directory_name):
        #make sure user does not accidentally overwrite a directory
        if directory_name in self.currentDirectory:
            errorMessage = "Directory already exists."
            return errorMessage
        else: 
            self.currentDirectory[directory_name] = {}
            return f"{directory_name} has been created."
    
    # touch command
    def set_new_file(self, file_name):
        if "." in file_name:
          if file_name in self.currentDirectory:
            errorMessage = "File already exists."
            return errorMessage
          else: 
            self.currentDirectory[file_name] = {}
            return f"{file_name} has been created."
        else:
            errorMessage = "File extension required."
            return errorMessage

    # cd command
    def set_current_directory(self, directory_name):
        # cd back one directory
        # check if user entered the symbol for the back command
        if (directory_name == "../"):
            # if the current directory is the root directory we dont want to pop the directory stack
            if (self.currentDirectory == self.rootDirectory):
                errorMessage = "You are already in the root directory."
                return errorMessage
            else: 
                self.dirStack.pop()
                # calculate the last index in the dirStack
                prevDir = len(self.dirStack) - 1
                # update the current directory to the previous directory
                self.currentDirectory = self.dirStack[prevDir]
                return self.currentDirectory


        # Make sure no one can cd into files
        # check if a string contains a period (.)
        if "." in directory_name:
            errorMessage = "Cannot cd into files."
            return errorMessage

        # check if the name of the directory is within the current directory
        if directory_name in self.currentDirectory:
            # update the currentDirectory to the directory of the directory_name
            self.currentDirectory = self.currentDirectory[directory_name]
            # update the Directory Stack
            self.dirStack.append(self.currentDirectory)
            
            return f"current directory: {directory_name}"
        else:
            errorMessage = "Directory does not exist."
            return errorMessage
        
    # ls command
    def get_files_in_current_directory(self):
        return self.currentDirectory

    # help command
    def get_help_log(self):
        helpMessage = "commands:\n    ls           list all directories and files in the current directory.\n    mkdir        create a new directory.\n    cd           step into a directory.\n    touch        create a new file.\n    exit         exit the virtual file system."
        return helpMessage



def __main__():
    # Give interface introduction to users' with help command
    print("Welcome To Your Virtual File System.\n")
    print("Type \'help\' for a list of commands.\n")
    
    #call class to frontend
    VFS1 = VirtualFileSystem()

    while 1:
        #create a system for users to input commands
        userInput = input(">>> ")

        # Creating commands
        if userInput == "exit":
            print("exiting virtual file system...")
            break
        #use class as an instance
        #print the return 
        elif userInput == "ls":
            print(VFS1.get_files_in_current_directory())
        
        # make a seperation between command and user's additional input 
        elif userInput[:5] == "mkdir":
            print(VFS1.set_new_directory(userInput[6:]))

        elif userInput[:2] == "cd":
            print(VFS1.set_current_directory(userInput[3:]))

        elif userInput[:5] == "touch":
            print(VFS1.set_new_file(userInput[6:]))

        elif userInput == 'help':
            print(VFS1.get_help_log())
    # create default error handling in case any of the given commands aren't entered 
        else:
            print(f"{userInput} is not recognized as an internal command.")

# start the program
__main__()

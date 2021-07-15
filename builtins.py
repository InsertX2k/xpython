"""
The module that contains the built-in functions and methods and even classes of the XPy Project.

The XPy Project is made to help you extend the functionality of the Python as a Programming Language.

To fully import the built-in functions of the XPy, do this :

```py
from xpy.builtins import *
```
"""
# imports
import time
import rotatescreen
import os

class x:
    """
    This class represents the built-in functions of the XPy.
    """
    def __init__(self):
        """
        This represents a great collection of functions that could improve and extend the functionality of the Python programming language.
        """
        pass

    def show(Text):
        """
        Prints the given text in the console window/screen.

        Syntax :
        x.show(Text)

        Example :
        x.show("Hello, World!")

        This method/function always return "<x.builtins>->x.func.show"
        """
        usrinput = str(Text)
        print(usrinput)
        return "<x.builtins>->x.func.show"

    def wait(delayinSecs):
        """
        Waits for the specific time of seconds, if given, then continues the execution of the code when the given time has passed.

        Syntax :
        x.wait(delayinSecs)

        Example :
        x.wait(12)

        This method/function always return <x.builtins>->x.func.wait
        """
        waittimeinsecs = int(delayinSecs)
        time.sleep(waittimeinsecs)
        return "<x.builtins>->x.func.wait"

    
    def get_char(stringValue):
        """
        Gets the first character in uppercase state of the given string, and returns it.

        Syntax : 
        x.get_char(stringValue)

        Example :
        x.get_char("Hello") -> H
        x.get_char("hi") -> H

        This method/function always return a string value.
        """
        get_char_str = str(stringValue)
        get_char_str = get_char_str[0]
        get_char_str = get_char_str.upper()
        return get_char_str

    def uinput(text_message = None):
        """
        Gets the text written using user's keyboard and returns it, if a message were given, it shows it to the user.

        Syntax : 
        x.uinput(text_message = None | text_message = 'str')

        Example :
        x.uinput(text_message = None)
        x.uinput(text_message = "What's your name? : ")

        This method/function always return a string value.
        """
        if text_message == None:
            return_value = input()
            return_value = str(return_value)
            return return_value
        else:
            message_to_show = text_message
            return_value = input(message_to_show)
            return_value = str(return_value)
            return return_value


    def rotate_primary_disp(intDegrees):
        """
        Rotate the primary display by the given degrees (int), and return True when successed.

        Syntax :
        x.rotate_primary_disp(intDegrees)

        Example :
        x.rotate_primary_disp(90) -> returns True if successed, otherwise returns False.

        This method/function always return a boolean (either True, or False)
        """
        rotate_by_degrees = int(intDegrees)
        try:
            primary_monitor = rotatescreen.get_primary_display()
            primary_monitor.rotate_to(rotate_by_degrees)
            return True
        except Exception as excpt:
            return False
    
    def reset_rotate():
        """
        Sets the primary display's orientation to landscape, if successed it returns True, otherwise it returns False.

        Syntax : 
        x.reset_rotate()

        Example :
        x.reset_rotate()

        This method/function always return a boolean (either True, or False)
        """
        try:
            primary_disp = rotatescreen.get_primary_display()
            primary_disp.set_landscape()
            return True
        except Exception as excpt1:
            return False

    def reset_rotate1():
        """
        The second attempt to reset the rotation state of the current monitor, returns True if the attempt has successed, else returns False.

        Syntax :
        x.reset_rotate1()

        Example :
        x.reset_rotate1()

        This method/function always return a boolean (either True, or False)
        """
        try:
            primary_disp0 = rotatescreen.get_primary_display()
            primary_disp0.rotate_to(0)
            return True
        except Exception as excpt2:
            return False
    
    def reset_rotate_loop():
        """
        Does a while True loop with the code of reseting the rotation state of your monitor, This command isn't recommended, as it might damage your display adapter.

        Syntax :
        x.reset_rotate_loop()

        Example :
        x.reset_rotate_loop()

        This method/function returns False if the user doesn't confirm they wish to processed.
        """
        confirmation_input = x.uinput(text_message="This can be dangerous to your monitor, Do you wish to processed anyway? [Y,N] ")
        confirmation = x.get_char(confirmation_input)
        if confirmation == "Y":
            while True:
                try:
                    primary_disp1 = rotatescreen.get_primary_display()
                    primary_disp1.rotate_to(0)
                except Exception as excpt16:
                    print("\nUnable to communicate with the monitor's software configuration to rotate it.")

        if confirmation == "N":
            return False
        
    def get_monitors():
        """
        Returns a list of all available monitors attached to this system (localhost), and if an exception occurs during the process, it returns False.

        Syntax : 
        x.get_monitors()

        Example :
        x.get_monitors()

        This method/function either returns a boolean or a list.
        """
        try:
            monitors = rotatescreen.get_displays()
            return monitors
        except Exception as excpt10:
            print("Unable to get a list of all connected monitors in this system.")
            return False

    def get_secondary_disps():
        """
        Returns a list of all available secondary displays attached to this system (localhost), and if an exception occurs during the process, it returns False.

        Syntax :
        x.get_secondary_disps()

        Example :
        x.get_secondary_disps()

        This method/function either returns a boolean or a list.
        """
        try:
            disps = rotatescreen.get_secondary_displays()
            return disps
        except Exception as excpt9:
            x.show("Unable to get a list of all available secondary displays in this system.")
            return False

    def make_string(valueToConvert):
        """
        Converts the given float or integer to a string value, if an exception occurs during the convertion process, this must return False.

        Syntax :
        x.make_string(valueToConvert)

        Example :
        x.make_string(12) -> '12'
        x.make_string(12.4) -> '12.4'

        Note : This method/function always return a string value.
        """
        try:
            string = valueToConvert
            return str(string)
        except Exception as excpt12:
            print("Unable to make this a string.")
            return False

    def make_int(Value):
        """
        Converts the given float or string value to an integer, if an exception occurs during the convertion process, this must return False.

        Syntax : 
        x.make_int(Value)

        Example :
        x.make_int("12.2") -> 12
        x.make_int(15.2) -> 15

        Note : This method/function always return an integer.
        """
        value = Value
        try:
            value = int(value)
            return value
        except Exception as excpt6:
            return False

    def make_float(intToMakeFloat):
        """
        Converts the given integer or string value to a float, if an exception occurs during the convertion process, this must return False.

        Syntax :
        x.make_float(intToMakeFloat)

        Example :
        x.make_float("12") -> Converts the given string to an integer then converts it again to a float value -> 12.0
        x.make_float(15) -> The float value of 15 -> 15.0

        Note : This method/function always return a float.
        """
        inttomakefloat = intToMakeFloat
        try:
            inttomakefloat = float(inttomakefloat)
            return inttomakefloat
        except Exception as excpt4:
            return False
    
    def auinput(text_message = None, *args, **kwargs):
        """
        An advanced version of the x.uinput() method, this method accepts *args, and **kwargs.

        Syntax : 
        x.auinput(text_message = None, *args, **kwargs)

        Example : 
        x.auinput(text_message = "Enter your name : ")
        """
        try:
            messagetoshow = text_message
        except:
            pass
        method_args = args
        method_kwargs = kwargs

        if text_message == None:
            try:
                return_value = input(method_args, method_kwargs)
                return return_value
            except:
                return_value = input()
                return return_value
        else:
            try:
                return_value = input(messagetoshow, method_args, method_kwargs)
                return return_value
            except:
                return_value = input(messagetoshow)
                return return_value



    def choice(strMessageToShow, tubleChoices):
        """
        Gives the user a list of choices, where user is supposed to choose anything from the list, otherwise returns False.

        Syntax :
        x.choice(strMessageToShow, tubleChoices)

        Example : 
        x.choice("Choose your favorite food: ", ['pizza', 'apples', 'bananas'])
        """
        list_of_choices = tubleChoices
        message_to_show = strMessageToShow
        
        usr_choice = x.auinput(rf"{message_to_show} {list_of_choices}  ")
        if usr_choice in list_of_choices:
            return usr_choice
        else:
            return False

    def term(command = None):
        """
        The built-in function term() is used to execute the given command(s) when specified, and the return value of this function/method will be the console command return value, if a command were given.

        Syntax :
        x.term(command = None | command = 'str')

        Example :
        x.term(command = r'echo Hello World!')
        x.term(command = r"pause >nul")
        x.term(command = r"myapp_wargs.exe /arg1 /arg2 /arg3 /arg4")
        x.term(command = r"start cmd.exe")
        Please note that you will have to use the 'r' parameter before the given string to ignore ANSI Escapes.

        When command is None, it returns False instead of the value the console command return value.
        """
        if command == None:
            return False
        else:
            try:
                command_to_execute = command
                return_value = os.system(command_to_execute)
                return return_value
            except OSError or WindowsError or Exception as excpt28:
                return False

    def clr_scr():
        """
        This function is used to clear the console screen, it has no return value, and it automatically detects the name of your operating system and it executes the appropriate console clear command for that OS.

        Syntax :
        x.clr_scr() -> None

        Example :
        x.clr_scr() -> None

        Note : This doesn't work with Python's default IDLE.
        """
        try:
            osname = os.name
        except Exception as excpt32:
            print("Unable to get the operating system name, this can cause exceptions with the runtime.")
            pass
        # print(osname) -> nt for windows, posix for linux and macos idk.
        if osname == 'nt':
            x.term("cls")
            return
        else:
            x.term("clear")
            return


    def make_file(strFileName):
        """
        The built-in function used to make a file with the given name(s), either in the current working directory, or in another directory.

        Syntax : 
        x.make_file(strFileName) -> boolean True | False

        Example : 
        x.make_file("MyZip.rar") -> boolean True if successed, else returns boolean False.

        This method/function always return a boolean.
        """
        file_name_to_make = str(strFileName)
        try:
            with open(file_name_to_make, 'w') as NewFile:
                NewFile.write("")
            
            # Now, let's close the file, to make other programs able to modify it.
            NewFile.close()
            return True
        except Exception as excpt34:
            return False

    def get_os_name():
        """
        This function gets the OS name, then returns it.

        When running on Microsoft Windows OS, this returns 'nt'
        Otherwise, returns 'posix', if retrieving the current OS name fails, this method is intended to return False

        Syntax :
        x.get_os_name() -> str 'nt' | str 'posix'

        Example :
        x.get_os_name() -> either 'nt' or 'posix'

        This method/function either return a boolean or a string value.
        """
        try:
            os_name = str(os.name)
            return os_name
        except OSError or Exception as excpt71:
            return False

    # Defining the get current working directory function.
    def cd():
        """
        Returns a string contains the full path of the current working directory (%cd%), if unable to retrieve the current wdir, it returns False.

        Syntax :
        x.cd() -> 'str' represents the current working directory.

        Example :
        x.cd() -> 'str' represents the current working directory -> "C:/MyWork/Python" for an example.

        This method/function either return a boolean or a string value.
        """
        try:
            cur_dir = os.getcwd()
            return str(cur_dir)
        except Exception as excpt70:
            return False
    

    def remdir(path = None):
        """
        Removes the given directory(s), if no directory were given, it will delete the current working directory (cd) instead (While of course showing you a confirmation of this process).

        Syntax :
        x.remdir(path = None | path = 'str')

        Example :
        x.remdir(path = r"C:\MyWork\MyWork.Confirmed")
        x.remdir(path = z) Where z = r"C:\MyWork\MyWork.Confirmed\MyDir"

        This method/function always return a boolean.
        """
        try:
            rmdir_path = path
        except:
            pass
        if path == None:
            rmdir_path = os.getcwd()
            confirm0 = x.choice(rf"This will delete the current working directory, Which is : {rmdir_path} , Do you wish to processed? : ", ['Y', 'N'])
            if confirm0 == 'Y':
                try:
                    os.rmdir(rmdir_path)
                    return True
                except Exception as excpt45:
                    return False
            if confirm0 == 'N':
                return False
        else:
            rmdir_path = path
            # Let's go.
            try:
                os.rmdir(rmdir_path)
                return True
            except Exception as excpt47:
                return False
    
    def ren(strSourceFile, strDestination):
        """
        Renames the given file(s) or directory(s) to the given name(s).

        Syntax :
        x.ren(strSourceFile, strDestination)

        Example :
        x.ren("myfile.txt", "yourfile.txt")
        x.ren("Myfile.txt", "myfile.md")

        Note : This doesn't show a confirmation or even a warning when trying to change the extension of the given file(s)

        This method/function always return a boolean (either a True or a False)
        """
        filetorename = str(strSourceFile)
        fileasadestination = str(strDestination)
        try:
            os.rename(filetorename, fileasadestination)
            return True
        except Exception as excpt49:
            return False

    def rem(strFileName, *args):
        """
        Removes the given file(s), if multiple files are given, it must delete them before deleting the given file in the parameter 'strFileName'

        Syntax :
        x.rem(strFileName, *args) -> boolean True | False

        Example :
        x.rem("mYFILE.txt", "myfile.md", "mycompiled app.exe", "myandroidapp.apk")
        """
        filename_toremove = str(strFileName)
        try:
            files = args
        except:
            pass

        try:
            for file_name in files:
                try:
                    os.remove(file_name)
                except:
                    pass
        except:
            pass

        try:
            os.remove(filename_toremove)
            return True
        except Exception as excpt51:
            return False



    def make_list(elementToMakeListOf):
        """
        Tries to make a list of the given item, if successed, it will return the list, otherwise it will return False.

        Syntax :
        x.make_list(elementToMakeListOf) -> False | [list]

        Example :
        x.make_list(z) -> False | [list]

        This method/function either return a boolean or a string value.
        """
        make_list_of = elementToMakeListOf
        try:
            return_list = list(make_list_of)
            return return_list
        except Exception as excpt69:
            return False

    def make_xs(strDestinationFile):
        """
        Makes a XPy script file with the given name, if fails it returns False.

        Syntax :
        x.make_xs(strDestinationFile)

        Example :
        x.make_xs(r"xscript.x")
        x.make_xs(r"C:\MyWork\XScripts\MyScript.x")

        Please keep in mind that you will have to copy the folder 'xpy' to the folder/directory where the XPy script is made.

        This method/function always return a boolean (Either True or False)
        """
        make_xscript_fname = str(strDestinationFile)
        try:
            with open(make_xscript_fname, 'w', encoding='utf-8') as ScriptFile:
                ScriptFile.write("\n# This file is automatically made by the XPy Framework.\nfrom xpy.builtins import *\n\n# Don't forget to include the folder xpy in the same directory as this script file to work \n# Start typing X scripts in the next line\n")
            ScriptFile.close()
            return True
        except Exception as excpt77:
            return False

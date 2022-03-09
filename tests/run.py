import subprocess
import os

def test_spams(args=None, python_exec = 'python'):
    """Run spams-python tests from python
    
    To run the tests, from the command line, please check the README.md file
    
    Input:
        args (string|string list): argument to pass to the the main test script,
            use `args='-h'` for more details. If None (default), all tests are
            run.
        python_exec (string): python executable. By default, it is `'python'`.
            Python 3+ is required. On some system, you may have to set 
            `python_exec = 'python3'`.
    """
    
    # check spams availability
    try:
        import spams
    except:
        raise ModuleNotFoundError("No module named 'spams'")
    
    # main test file
    test_file = os.path.join("tests", "test_spams.py")
    if os.path.isfile(test_file):
        test_file = os.path.abspath(test_file)
    else:
        test_file = os.path.join(
            os.path.dirname(os.path.abspath(spams.__file__)), test_file
        )
        
    # test dir
    test_dir = os.path.dirname(test_file)
    
    # check python executable
    try:
        python_version = subprocess.run([python_exec, "-V"], capture_output=True)
    except:
        raise SystemError(f"{python_exec} is not a valid python executable")
    # check python version
    if not "Python 3." in python_version.stdout.decode('UTF-8'):
        raise SystemError("Python 3+ is required, try using python_exec = 'python3'")
    
    # check args
    if args is None:
        args = []
    elif not (isinstance(args, str) or \
        (isinstance(args, list) and \
        all(isinstance(arg, str) for arg in args))):
        raise TypeError("'args' input should be a string or a list of strings.")
    
    if isinstance(args, str):
        args = [args]
    
    # run
    subprocess.run([python_exec, 'test_spams.py'] + args, cwd = test_dir)
    
    

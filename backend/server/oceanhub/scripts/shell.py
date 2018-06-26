def test_global():
    print('Hi, my name is Si!')


def make_shell_context():  # get all the tasks loaded up into the application
    return {
        'test_global': test_global
    }

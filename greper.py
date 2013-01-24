import os
import re
import sys
import getopt

class Greper:
    """
    A greper for any platform.
    """
    params_dict = {}
    path_list = []
    search_pattern = ''
    search_pattern_cmp = None
    
    def __init__(self):
        """
        """
        pass
    
    def grep(self):
        """
        - 'params': a dict containing all parameters
        """
        for path in self.path_list:
            for root, dirs, files in os.walk(path):
                for f in files:
                    p = os.path.join(root, f)
                    self.print_file(p)

    def print_file(self, path):
        """
        - `path`:
        """
        line_number = 0
        file_content = ''
        print_content = ''
        try:
            f = open(path, 'r')
            file_content = f.readlines()
        except:
            pass
        finally:
            f.close()

        for line in file_content:
            line_number += 1
            if self.need_to_print_line(line):
                print_content += '    ' + '< ' + str(line_number) + ' > ' + line
        if not print_content == '':
            print(path)
            print(print_content, end='')
        f.close()

    def need_to_print_line(self, line):
        """
        """
        return re.search(self.search_pattern_cmp, line)
    
    def set_params(self, params):
        """
        - `params`: a dict containing all parameters
        """
        self.params_dict = params
        self.path_list = self.params_dict['path_list']
        self.search_pattern = self.params_dict['search_pattern']
        self.search_pattern_cmp = re.compile(self.search_pattern)

    def dump(self):
        """
        dump all parameters.
        """
        p = ''
        for (k, v) in self.params_dict.items():
            p += '  dump parameters>> ' + str(k) + ' : ' + str(v) + '\n'
        print(p, end='')

def get_options():
    """
    deal with cmdline options.
    """
    pass

if __name__ == '__main__':
    params = {
        'path_list' : ['E:/git/github/emacs'],
        'search_pattern' : 'requ+',
    }
    # print(str(params))
    greper = Greper()
    greper.set_params(params)
    greper.grep()
    # greper.dump()


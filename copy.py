#!/usr/bin/env python

import sys
import os

def main():
    if len(sys.argv) != 2:
        print 'usage) copy.py <new_name>'
        exit(1)
    
    new_name = sys.argv[1]
    copy_files = [
        'CMakeLists.txt',
        'LICENSE.md',
        'test//gtest-all.cc',
        'test/gtest.h',
        'test/main.cc',
        'cli/main.cc',
    ]

    rename_files = [
        ('src/cpptemplate/exception.hpp',
         'src/{0}/exception.hpp'.format(new_name)),
        ('src/cpptemplate.cc',  'src/{0}.cc'.format(new_name)),
        ('src/cpptemplate.hpp', 'src/{0}.hpp'.format(new_name)),
    ]

    copy_list = [(x, os.path.join(new_name, x)) for x in copy_files] + \
                [(x[0], os.path.join(new_name, x[1])) for x in rename_files]
    
    os.makedirs(new_name)
    for src, dst in copy_list:
        d = os.path.dirname(dst)
        if not os.path.exists(d): os.makedirs(d)

        ofd = open(dst, 'w')
        for line in open(src, 'r'):
            ofd.write(line.replace('cpptemplate', new_name)
                      .replace('CPPTEMPLATE', new_name.upper()))

    readme = '{0}\n===========\n'.format(new_name)
    open(os.path.join(new_name, 'README.md'), 'w').write(readme)

if __name__ == '__main__': main()

#!/usr/bin/env python

# Jonathon Staff - March 22, 2015
#
# gitman
# ======
#
# Simple script to read a manifest file and download Git repos as listed
# therein.

import os
import sys
import argparse

class Gitman(object):
     
    def __init__(self):
        print "\n,---.o|                   "
        print "|  _..|--- ,-.-. ---.,---."
        print "|   |||    | | |,---||   |"
        print "`---''`---'' ' '`---''   '"
        print "--------------------------\n"

        parser = argparse.ArgumentParser(
            description='Manage multiple repos at once.',
            usage='''gitman <command> [<args>]

The most commonly used gitman commands are:
   clone      Downloads Git repos in a predefined file structure
   index      Generates an index file based on local repos
''')
        parser.add_argument('command', help='Subcommand to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)

        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def clone(self):
        if not sys.stdin.isatty():
            lines = sys.stdin.readlines()
        else:
            parser = argparse.ArgumentParser(
                    description='Clones down repos as specified by a manifest',
                    usage='gitman clone <manifest_file>'
                    )
            parser.add_argument('manifest', nargs='*', help='Manifest file name')

            # Disregard the first and second arguments since they will always
            # be `gitman` and `clone`
            args = parser.parse_args(sys.argv[2:])
            if len(args.manifest) < 1:
                print "No manifest provided."
                parser.print_help()
                exit(1)
            else:
                manifest = args.manifest[0]
                lines = open(manifest).readlines()

        print "Cloning repos..."

        for line in lines:
            if '#' in line or not 'git' in line:
                continue

            print "  ==> " + line.rstrip()
            os.system('git clone --quiet ' + line)

    def index(self):
        parser = argparse.ArgumentParser(
                description='Creates a recursive index of all repos beneath the current directory.',
                usage='gitman index <output_index>'
                )
        parser.add_argument('output', nargs='*', help='Name of the output index file')

        # Disregard the first and second arguments since they will always
        # be `gitman` and `index`
        args = parser.parse_args(sys.argv[2:])
        if len(args.output) > 0:
            output = args.output[0]
        else:
            output = 'gitman_index'

        print "Indexing Git repos...\n"
        
        repos = []
        for path, dirnames, filenames in os.walk('.'):
            if '.git' in dirnames:
                del dirnames[:]
                
                for line in open(os.path.join(path, '.git/config')):
                    if 'url' in line and '=' in line and '.git' in line:
                        # We have our remote url
                        remote_url = self.parse_remote_url(line)
                        print "  ==> " + self.parse_repo_name(remote_url)
                        repos.append(remote_url + ' ' + path + '\n')
        
        with open(output, 'w') as f:
            f.writelines(repos)
                
    @staticmethod
    def parse_remote_url(line):
        url = line.split('=').pop()
        url = url.rstrip()
        return url.lstrip()

    @staticmethod
    def parse_repo_name(line):
        repo = line.split('/').pop()
        return repo.rstrip('.git')


if __name__ == '__main__':
    Gitman()

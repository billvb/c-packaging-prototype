#!/usr/bin/env python

import subprocess
import argparse
import logging
import os

TEMP_repo_source = '/'

class Package(object):

    def __init__(self, name, repo_source, packages_base):
        self.repo_source = repo_source
        self.packages_base = packages_base
        self.name = name
        self.base_dir = os.path.join(self.packages_base, name)

    def fetch(self, force=False):
        logging.info('Fetching %s ...' % self.name)
        orig_dir = os.getcwd()
        if os.path.exists(self.base_dir):
            if force:
                logging.warning('Found %s, cleanly re-installing.' % self.name)
                subprocess.call(['rm', '-rf', self.base_dir])
                os.makedirs(self.base_dir)
            else:
                logging.warning('Package %s already found (use -f to force '
                                'reinstallation).' % self.name)
                return

        logging.debug('Setting CWD to %s.' % self.packages_base)
        os.chdir(self.packages_base)
        #cmds = ['git', 'clone', os.path.join(self.repo_source, self.name)]
        cmds = ['cp', '-r', os.path.join(self.repo_source, self.name), '.']
        logging.info('Executing: %s' % ' '.join(cmds))
        rc = subprocess.call(cmds)
        if rc != 0:
            raise Exception('Cannot get repo')
        os.chdir(orig_dir)

    def compile(self):
        logging.info('Compiling %s ...' % self.name)
        orig_dir = os.getcwd()
        os.chdir(self.base_dir)
        logging.debug('In directory %s' % os.getcwd())
        logging.info('Calling Make ...')
        subprocess.call('make')
        os.chdir(orig_dir)

        for fname in os.listdir(os.path.join(self.base_dir, 'build')):
            if '.a' in fname:
                cmds = ['cp', os.path.join(self.base_dir, 'build', fname),
                        os.path.join(self.packages_base, 'lib')]
                logging.warning('Copying library: %s' % ' '.join(cmds))
                subprocess.call(cmds)

        for fname in os.listdir(os.path.join(self.base_dir, 'include')):
            if '.h' in fname:
                cmds = ['cp', os.path.join(self.base_dir, 'include', fname),
                        os.path.join(self.packages_base, 'include')]
                logging.warning('Copying header: %s' % ' '.join(cmds))
                subprocess.call(cmds)

        logging.info("Done compilation of %s" % self.name)


class PackageContext(object):
    def __init__(self, project_base_dir):
        self.project_base_dir = project_base_dir

    def init_context(self):
        if not os.path.exists(os.environ['CPAK_REPO_ROOT']):
            logging.error('Environment variable CPAK_REPO_ROOT not set')
            return

        repo_base = os.environ['CPAK_REPO_ROOT']
        if not os.path.exists(repo_base) or not os.path.isabs(repo_base):
            logging.error('`%s` not valid repo base.' % repo_base)
            return

        logging.info('Creating lib and include dir')
        try:
            os.makedirs(os.path.join(self.project_base_dir, 'cpak-deps',
                        'lib'))
            os.makedirs(os.path.join(self.project_base_dir, 'cpak-deps',
                        'include'))
        except OSError as e:
            logging.error('cpak environment already exists!')

    def install_package(self, package_name, force):
        package = Package(package_name, os.environ['CPAK_REPO_ROOT'],
                          os.path.join(self.project_base_dir, 'cpak-deps'))
        try:
            package.fetch(force)
            package.compile()
        except Exception as e:
            logging.error('Cannot get package %s.' % (package_name))

    def remove_package(self, package_name, force=False):
        if not os.path.exists(os.path.join('cpak-deps', package_name)):
            logging.error('%s not found in project.' % package_name)
            return

        try:
            cmds = ['rm', '-rf', os.path.join('cpak-deps', package_name)]
            logging.info('Executing: %s' % ' '.join(cmds))
            subprocess.call(cmds)
        except OSError as e:
            logging.error('Error removing %s: %s' % (package_name, e))

    def cleanup(self, force):
        if not force:
            logging.error('Cannot cleanup environment unless forced (-f)')
        else:
            cmds = ['rm', '-rf', 'cpak-deps']
            logging.info('Executing: %s' % ' '.join(cmds))
            subprocess.call(cmds)
            

    def rebuild_project(self):
        raise NotImplemented


if __name__ == '__main__':
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='C Package Manager')
    subparsers = parser.add_subparsers(dest='subcommand')

    install_p = subparsers.add_parser('install', help='Install a package')
    install_p.add_argument('package_name', type=str,  help='Name of package')
    install_p.add_argument('--force', '-f', action='store_true',
                           help='Force re-install if already exists')

    remove_p = subparsers.add_parser('remove', help='Remove a package')
    remove_p.add_argument('package_name', type=str, help='Remove package')

    rebuild_p = subparsers.add_parser('rebuild', help='Clean rebuild of all')
    
    init_p = subparsers.add_parser('init', help='Initialize environment here')
    
    cleanup_p = subparsers.add_parser('cleanup', help='Remove entire cpak env')
    cleanup_p.add_argument('--force', '-f', action='store_true',
                           help='Force this (required).')

    args = parser.parse_args()

    context = PackageContext(os.getcwd())

    if args.subcommand == 'install':
        context.install_package(args.package_name, args.force)
    elif args.subcommand == 'remove':
        context.remove_package(args.package_name)
    elif args.subcommand == 'cleanup':
        context.cleanup(args.force)
    elif args.subcommand == 'rebuild':
        context.rebuild_project()
    elif args.subcommand == 'init':
        context.init_context()
    else:
        logging.error('Unknown option')

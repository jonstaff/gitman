# Gitman

Gitman is a simple tool that allows you to easily recreate your directory tree of Git repositories on multiple computers.

This can be useful when migrating to a new computer or standardizing a development environment across teams.

## Installation

Download `gitman.py` and place it on your $PATH.

## Usage

### Index

You can create a manifest of your current Git repos using the `index` command.  If no output filename is specified, `gitman_index` will be used.

```
gitman index <optional_filename>
```

This will recursively search through directories beneath your current path and generate a manifest from all Git repos that have remote URLs.

### Clone

```
gitman clone <manifest_filename>
```

The manifest file is simply a mapping of remote URLs to local paths.  Rather than cloning from a local manifest file, I prefer to host mine as a gist or snippet, using the clone command as follows:

```
curl https://gist.githubusercontent.com/jonstaff/9c4145fb2864f4e8d091/raw/6c00c5de296f5e7376e02984e657317a8b25513b/gitman_index | gitman clone
```

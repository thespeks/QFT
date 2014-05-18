


if __name__ == __main__:
    import sys
    # Check were running the right version of python
    if (sys.version_info.major == 3 and sys.version_info.minor >= 2):
        import qft
        qft.run
    else:
        sys.exit("""Invalid python version. (Got version {0}.{1})\n
Requires python version 3.2 or greater.\n
see: https://www.python.org/download/""".format(
    sys.version_info.major, sys.version_info.minor))

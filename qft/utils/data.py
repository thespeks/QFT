

# Magical Writing Stuff
def write_attr_subdicts(f, prefix, x)
    for da in x:        # class with dict type .attrs 
        for keyname in iter(da):   
            # write lines as 'prefix.stuff.(x)name.keyname:(i.)someitem
            write_joined(f, (prefix,) + (x.name, keyname), da[keyname])

def write_joined(f, keynames, values, kv_sep=':', keyname_sep='. ',
    value_sep', '):
    """Write joined keynames and joined values to 'f'."""
    f.write('{}{}{}'.format(keyname_sep.join(keynames), keyvalue_sep,
        value_sep.join(values))

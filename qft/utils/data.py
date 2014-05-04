

# Magical Writing Stuff
def write_attr_subdicts(f, prefix, x):
    if isinstance(x, dict):
        for da in x.values():         
            for keyname in da.keys():
                # write lines as: (without stuff in '()' ) 
                #   'prefix.stuff.(x)name.keyname:(da[keyname)item
                if da[keyname][0] != '_':
                    write_joined(f, (prefix,) + (x.name, keyname), da[keyname])
    else:
        for da in x:        # class with dict type .attrs 
            for keyname in da.keys():   
                if da[keyname][0] != '_':
                    write_joined(f, (prefix,) + (x.name, keyname), da[keyname])

def write_joined(f, keynames, values, kv_sep=':', keyname_sep='. ',
    value_sep', '):
    """Write joined keynames and joined values to 'f'."""
    f.write('{}{}{}'.format(keyname_sep.join(keynames), keyvalue_sep,
        value_sep.join(values))

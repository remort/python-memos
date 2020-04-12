def load_config():
    """
    CONF is being imported first time from 'b', where it was 'locally',
    mistakenly modified. No matter which module you import it from next time,
    it will remain modified.
    So, changed once and imported in this state,
    original CONF state is being globally broken and lost forever.
    """
    # Taken from 'a' module.
    ORIG_VER = '1.0'
    ORIG_LEVEL = 'DEBUG'

    # First import of CONF from 'b' where it was assumingly 'locally modified'.
    # In 'b' it could be reimported from 'a', but it doesn't work this way.
    from b import CONF
    assert CONF['modules']['logger']['level'] != ORIG_LEVEL
    assert CONF['version'] != ORIG_VER

    # Ok. Let's 'reimport' it from 'c' (with no luck).
    from c import CONF as CONF2
    from c import mod_conf

    assert CONF2['modules']['logger']['level'] != ORIG_LEVEL
    assert CONF2['version'] != ORIG_VER

    assert mod_conf['version'] == '3.0'
    assert mod_conf['modules']['logger']['level'] == 'TRACE'

    # Import 'original CONF' from it's original module 'a'. No changes.
    from a import CONF as CONF3

    assert CONF3['modules']['logger']['level'] != ORIG_LEVEL
    assert CONF3['version'] != ORIG_VER

    # Conclusion: Imported once - object is being saved in global scope forever
    # in it's current state by the time of import.

    # But there is a way to forecefully reload a whole module:
    import a

    assert a.CONF['modules']['logger']['level'] != ORIG_LEVEL
    assert a.CONF['version'] != ORIG_VER

    from importlib import reload
    reload(a)

    assert a.CONF['modules']['logger']['level'] == ORIG_LEVEL
    assert a.CONF['version'] == ORIG_VER

    # At finals, reloaded whole module - we've got original CONF values.


if __name__ == '__main__':
    load_config()

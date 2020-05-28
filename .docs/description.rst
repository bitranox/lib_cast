cast float, int, time, file sizes etc. to human readable text with SI Prefixes

it can also be used on the commandline for windows and linux bash



.. code-block:: python

    >>> # cast floating point values
    >>> cast_float_to_human_readable_size(1000,'Volt')
    '1.00 KiloVolt (x10^3)'
    >>> cast_float_to_human_readable_size(0.1,'Volt')
    '100.00 MilliVolt (x10^-3)'
    >>> cast_float_to_human_readable_size(0.1,'V', short_form=True)
    '100.00 mV (x10^-3)'
    >>> cast_float_to_human_readable_size(0.1,'V', short_form=True, show_exponent=False)
    '100.00 mV'
    >>> cast_float_to_human_readable_size(0.1,'V', short_form=True, show_exponent=False, remove_trailing_zeros=True)
    '100 mV'

    >>> # cast byte or bit sizes
    >>> cast_float_to_human_readable_size(65535,base1024=True)
    '64 KibiByte (x1024^1)'

    >>> # cast time german
    >>> cast_float_2_human_readable_timediff(2455.456898418)
    '40 Minuten, 55 Sekunden'

    >>> # cast time english
    >>> cast_float_2_human_readable_timediff(2455.456898418, language='en')
    '40 minutes, 55 seconds'

    >>> # cast looong time german
    >>> cast_float_2_human_readable_timediff(89452.456898418)
    '  1 Tage,  0 Stunden, 50 Minuten, 52 Sekunden'

    >>> # AND MANY MORE ! - see usage !

.. code-block::

    IEC Prefixe (2**n)                  ISO Prefixe (10**-n)                ISO Prefixe (10**n)
    =======================             =======================             =======================
    'Ki', 'Kibi', (x1024^1)             'm', 'Milli', (x10^-3)              'k', 'Kilo' , (x10^3)
    'Mi', 'Mebi', (x1024^2)             'µ', 'Mikro', (x10^-6)              'M', 'Mega' , (x10^6)
    'Gi', 'Gibi', (x1024^3)             'n', 'Nano' , (x10^-9)              'G', 'Giga' , (x10^9)
    'Ti', 'Tebi', (x1024^4)             'p', 'Piko' , (x10^-12)             'T', 'Tera' , (x10^12)
    'Pi', 'Pebi', (x1024^5)             'f', 'Femto', (x10^-15)             'P', 'Peta' , (x10^15)
    'Ei', 'Exbi', (x1024^6)             'a', 'Atto' , (x10^-18)             'E', 'Exa'  , (x10^18)
    'Zi', 'Zebi', (x1024^7)             'z', 'Zepto', (x10^-21)             'Z', 'Zetta', (x10^21)
    'Yi', 'Yobi', (x1024^8)             'y', 'Yokto', (x10^-24)             'Y', 'Yotta', (x10^24)

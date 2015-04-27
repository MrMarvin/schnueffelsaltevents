SchnueffelSaltEvents
====================
Schnueffelt (engl. sniffs) salt events from a salt-masters event bus. The events are sent to a (remote) logging collector. The GELF (Graylog Extended Logging Format) is used.

Install
============
There are multiple ways to install SchnueffelSaltEvents:
```
# Via pip directly from the web
(sudo) pip install schnueffelsaltevents
```

```
# download & manuall installation
(sudo) python setup.py install
(sudo) pip install -r requirements.txt
```

Or building your own .deb/.rpm packages and install them. See 'Packaging' below.


Requirements
============
See `requirements.txt` for technical (e.g. python package) requirements. Currently schnueffelsaltevents only dependency is `gelfHandler`.

Assumptions
===========
* the salt node mode is `master`
* the salt event socket is in `/var/run/salt`
* sending messages via TCP (`--log_proto` can be used to change that. Please note that the only other option is UDP which does not provide any secrecy whatsoever)
* wrapping TLS around the tcp socket (can be tuned with `--i_do_not_want_any_securtiy'`)

See the the output of `--help`` for all possible arguments.

Usage
==========
This package should install a script called `schnueffel-salt-events` to you PATH. Use it.

## Example
```
schnueffel-salt-events --log_host graylog2.example.com -d
```

Packaging
==========
We used `fpm` to build SchnueffelSaltEvents into a .deb package for convinient distribution and versioning.
The full command is rather long but takes into account correct maintainer email, dependencies and even upstart scripts.
```
fpm -s python -t deb -m $GIT_AUTHOR_EMAIL -d python-gelfhandler --deb-upstart integration/upstart/schnueffel-salt-events.conf --deb-default integration/upstart/schnueffel-salt-events ./setup.py
```

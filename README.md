SchnueffelSaltEvents
====================
Schnueffelt (engl. sniffs) salt events from a salt-masters event bus. The events are sent to a (remote) logging collector. The GELF (Graylog Extended Logging Format) is used.

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
import pprint
import time
import os
import salt.utils.event

class Schnueffelstueck(object):

  def __init__(self, config, logger):
    self._config = config
    self._logger = logger

  def schnueffel(self):
    event = salt.utils.event.SaltEvent(
            self._config.salt_node,
            os.path.join(self._config.salt_sock_dir, self._config.salt_node)
            )
    if self._config.debug:
      print "listening on: %s" % event.puburi
    while True:
      ret = event.get_event(full=True)
      if ret is None:
        continue
      if self._config.debug:
        print 'Event fired at {0}'.format(time.asctime())
        print '*' * 25
        print 'Tag: {0}'.format(ret['tag'])
        print 'Data:'
        pprint.pprint(ret['data'])

      self._logger.info(ret['tag'], extra={'gelfProps': ret['data']})
      #self._logger.info("eine log zeile")

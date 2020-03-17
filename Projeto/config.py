import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='[%(asctime)s] [%(levelname)s] %(name)s' +
    '[%(funcName)s] [%(filename)s %(lineno)s] %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

covid = 19
logging.addLevelName(covid, 'covid')
def alert(self, message, *args, **kwargs):
    if self.isEnabledFor(covid):
        self._log(covid, message, args, **kwargs)
logging.Logger.covid = alert
corona_virus = logging.getLogger()

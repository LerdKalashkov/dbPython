import logging as log

log.basicConfig(level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I:%M:%S %p',
    handlers=[
        log.FileHandler('capaDatos.log'),
        log.StreamHandler()
    ])

if __name__ == '__main__':

    log.debug('DEGUB LEVEL')
    log.info('INFO LEVEL')
    log.warning('WARNING LEVEL')
    log.error('ERROR LEVEL')
    log.critical('CRITICAL LEVEL')

"""
Updating mapbox tiles
"""
import logging
import django
django.setup()
from services.jp2_to_tiff_conversion import jp2_to_tiff
from services.model_call import ModelCaller
from services.sentinel_download import SentinelDownload
from services.upload_to_mapbox import start_upload

sentinel_download = 1
call_model = 1
convert_to_tiff = 1
mapbox_upload = 1


logger = logging.getLogger('update')

if __name__ == '__main__':
    if sentinel_download:
        sentinel_downloader = SentinelDownload()
        sentinel_downloader.process_download()
    logger.info('Sentinel pictures were downloaded')

    if call_model:
        model_caller = ModelCaller()
        model_caller.start()
    if convert_to_tiff:
        logger.info('Start convert jp2_to_tiff')
        jp2_to_tiff()
        logger.info('Convert jp2_to_tiff finished')

    if mapbox_upload:
        try:
            logger.info('Start uploading to mapbox')
            uploader = start_upload()
        except (IOError, ValueError, FileNotFoundError, FileExistsError, Exception):
            logger.error('Error\n\n', exc_info=True)

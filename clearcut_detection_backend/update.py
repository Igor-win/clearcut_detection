"""
Updating mapbox tiles
"""
import traceback

import django
from django.conf import settings
from django.core.mail import EmailMessage

django.setup()
from sentinel_download import SentinelDownload
from upload_to_mapbox import start_upload
from jp2_to_tiff_conversion import jp2_to_tiff

if __name__ == '__main__':
    try:
        sentinel_downloader = SentinelDownload()
        sentinel_downloader.process_download()
        sentinel_downloader.executor.shutdown()
        jp2_to_tiff()
        start_upload().shutdown()
    except Exception as error:
        EmailMessage(
            subject='Pep download issue',
            body=(
                f'Daemon can not download Sentinel2 data. Issue information listed bellow: '
                f'\n\n{str(error)}\n\n {"".join(traceback.format_tb(error.__traceback__))}'
            ),
            from_email=settings.EMAIL_HOST_USER,
            to=settings.EMAIL_ADMIN_MAILS
        ).send()

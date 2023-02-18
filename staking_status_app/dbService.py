import datetime

from django.utils import timezone
from staking_status_app.models import PriceHistory



def save_staking_log(data):
    asset = ""
    is_available = []
    timestamp = datetime.datetime.now()
    for item in data:
        asset_name = item['asset']
        asset = asset_name.split()[0]
        is_available.append( {asset_name: item['available']} )
        timestamp_str = item['time']
        timestamp = timezone.datetime.strptime(timestamp_str.strip(), '%H:%M:%S  , %d-%b-%Y')
    last_record = PriceHistory.objects.using('mongoDb').latest('timestamp')
    if not is_same(last_record, is_available):

        price_history = PriceHistory(asset_name=asset, is_available=is_available, timestamp=timestamp)
        print(asset , is_available, timestamp)
        price_history.save(using='mongoDb')
    else:
        print('both records are same, skipping')


def is_same(last_record, current_is_available):
    formatted_data = [{k: v for k, v in item.items()} for item in last_record.is_available]
    # print(current_is_available)
    # print(formatted_data)
    # print(last_record.is_available == formatted_data)
    return last_record.is_available == formatted_data
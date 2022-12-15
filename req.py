import os
import requests

dump_directory = os.path.join(os.getcwd(), 'mp3')
os.makedirs(dump_directory, exist_ok=True)


def dump_mp3_for(resource):
    payload = {
        'api': 'advanced',
        'format': 'JSON',
        'video': resource
    }
    initial_request = requests.get('http://youtubeinmp3.com/fetch/', params=payload)
    if initial_request.status_code == 200:  
        download_mp3_at(initial_request)


def download_mp3_at(initial_request):
    j = initial_request.json()
    filename = '{0}.mp3'.format(j['title'])
    r = requests.get(j['link'], stream=True)
    with open(os.path.join(dump_directory, filename), 'wb') as f:
        print('Dumping "{0}"...'.format(filename))
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
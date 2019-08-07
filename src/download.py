from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os
import argparse


def download(key_word, save_dir='./data/'):
    save_dir = os.path.join(save_dir, key_word)
    os.makedirs(save_dir, exist_ok=True)

    flickr = FlickrAPI(
        os.getenv('FLICKR_API_KEY'),
        os.getenv('FLICKR_API_SECRET_KEY'),
        format='parsed-json')
    result = flickr.photos.search(
        text=key_word,
        per_page=400,
        media='photos',
        sort='relevance',
        safe_search=1,
        extras='url_q, license'
    )

    photos = result['photos']

    for i, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        file_path = os.path.join(
            save_dir, '{file_name}.jpg'.format(file_name=photo['id']))
        if os.path.exists(file_path):
            continue
        urlretrieve(url_q, file_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('key_word')

    args = parser.parse_args()
    download(
        key_word=args.key_word
    )

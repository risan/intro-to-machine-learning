# coding: utf8
import os
import errno
import urllib
import tarfile
from urlparse import urlparse

def get_filename_from_url(url):
    """Extract the filename from the url.

    :param str url: The url to extract the filename from
    :return: The extracted filename
    :rtype: str
    """
    url_components = urlparse(url)

    return os.path.basename(url_components.path)

def is_file_exists(filename):
    """Check whether the given file exists.

    :param str filename: The path to the file
    :rtype: bool
    """
    return os.path.isfile(filename)

def create_directory_if_not_exists(directory):
    """Create the directory if it's not exists.

    :param str directory: The path to the directory
    :raises OSError: if it cannot create the directory
    """
    try:
        os.makedirs(directory)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise

def download_enron_dataset_gzip(directory):
    """Download the compressed Enron dataset.

    :param str directory: The directory path where the downloaded file will be stored
    :return: The fullpath to the downloaded file
    :rtype: str
    """
    url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
    filename = os.path.join(directory, get_filename_from_url(url))

    if is_file_exists(filename):
        print("✅ Enron dataset is already downloaded: " + filename)
    else:
        create_directory_if_not_exists(directory)
        print("⏳ Downloading the Enron dataset, this may take a while...")
        urllib.urlretrieve(url, filename)
        print("✅ Enron dataset is downloaded: " + filename)

    return filename

def download_enron_dataset(directory):
    """Download the compressed Enron dataset and extract it.

    :param str directory: The directory path where the dataset will be stored
    """
    filename = download_enron_dataset_gzip(directory)
    directory = os.path.dirname(filename)

    print("⏳ Unzipping Enron dataset, this may take a while...")
    tfile = tarfile.open(filename, "r:gz")
    tfile.extractall(directory)
    print("✅ Enron dataset is extracted to: " + directory)

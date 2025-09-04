import os

CONFIG = {'local_data_dir': 'chs_data/', 
          'remote_data_dir': 'https://chs.isee.nagoya-u.ac.jp/data/chs/'}

if os.environ.get('SPEDAS_DATA_DIR'):
    CONFIG['local_data_dir'] = os.sep.join([os.environ['SPEDAS_DATA_DIR'], 'chs'])

if os.environ.get('SUSANOO_DATA_DIR'):
    CONFIG['local_data_dir'] = os.environ['SUSANOO_DATA_DIR']

if os.environ.get('SUSANOO_REMOTE_DATA_DIR'):
    CONFIG['remote_data_dir'] = os.environ['SUSANOO_REMOTE_DATA_DIR']
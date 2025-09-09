from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download import download
from pytplot import time_clip as tclip
from pytplot import cdf_to_tplot
from .config import CONFIG

def su_load(trange=["2021-8-10","2021-8-11"], 
        pathformat=None,
        datatype=None,
        prefix="",
        suffix="",
        get_support_data=False,
        varformat=None,
        varnames=[],
        downloadonly=False,
        notplot=False,
        no_update=False,
        time_clip=True,
        force_download=False,
        uname=None, 
        passwd=None,
        mode=None,
        site=None,
        model=None,
        file_res=None,
        version=None,
        ):

    if site == None:
        site = 'earth'

    # https://chs.isee.nagoya-u.ac.jp/data/chs/simulation/susanoo/data/cdf/earth/2021/02/susanoo_sw_earth_5m_20210202_v01.01.cdf
    pathformat = (
        "simulation/susanoo/data/cdf/" + site
        + "/%Y/%m/"
        + "susanoo_sw_" + site +"_5m_%Y%m%d_v0?.0?.cdf"
    )

    remote_names = dailynames(file_format=pathformat, trange=trange)
    prefix = 'susanoo_sw_'
    suffix = '_' + site

    # elif instrument == "": # other instruments
    # Modules for other instruments will be added...


# find the full remote path names using the trange
    remote_names = dailynames(file_format=pathformat, trange=trange)
    out_files = []

    files = download(
            remote_file=remote_names,
            remote_path=CONFIG["remote_data_dir"],
            local_path=CONFIG['local_data_dir'],
            no_download=no_update,
            force_download=force_download,
            username=uname, password=passwd,
        )

    if files is not None:
        for file in files:
            out_files.append(file)

    out_files = sorted(out_files)

    if downloadonly:
        return out_files


    tvars = cdf_to_tplot(
        out_files,
        prefix=prefix,
        suffix=suffix,
        get_support_data=get_support_data,
        varformat=varformat,
        varnames=varnames,
        notplot=notplot,
    )

    if tvars is None or notplot:
        return tvars

    if time_clip:
        for new_var in tvars:
            tclip(new_var, trange[0], trange[1], suffix="")

    return tvars
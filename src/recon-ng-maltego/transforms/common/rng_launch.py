#!/usr/bin/env python

import os
import os.path
import subprocess
import tempfile
from canari.config import config

__author__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__copyright__ = 'Copyright 2013, Recon-ng-maltego Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__email__ = 'david.bressler@guidepointsecurity.com'
__status__ = 'Development'


def create_workspace(workspace):
    rec_source = "exit"
    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def set_domain(workspace, domain):
    rec_source = "set DOMAIN %s\nexit" % domain
    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def set_company(workspace, company):
    rec_source = "set COMPANY %s\nexit" % company
    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def set_radius(workspace, radius):
    rec_source = "set RADIUS %s\nexit" % radius
    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp

# TODO set latitude and longitude


def hosts_gather(workspace):
    rec_source = """use recon/hosts/gather/dns/brute_force\nrun\nexit\n
use recon/hosts/gather/dns/reverse_resolve\nrun\nexit\n
use recon/hosts/gather/http/api/bing_ip\nrun\nexit\n
use recon/hosts/gather/http/api/google_site\nrun\nexit\n
use recon/hosts/gather/http/api/shodan_hostname\nrun\nexit\n
use recon/hosts/gather/http/api/shodan_net\nrun\nexit\n
use recon/hosts/gather/http/web/baidu_site\nrun\nexit\n
use recon/hosts/gather/http/web/bing_domain\nrun\nexit\n
use recon/hosts/gather/http/web/census_2012\nrun\nexit\n
use recon/hosts/gather/http/web/google_site\nrun\nexit\n
use recon/hosts/gather/http/web/ip_neighbor\nrun\nexit\n
use recon/hosts/gather/http/web/netcraft\nrun\nexit\n
use recon/hosts/gather/http/web/ssl_san\nrun\nexit\n
use recon/hosts/gather/http/web/yahoo_site\nrun\nexit\nexit"""

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def hosts_enum(workspace):
    rec_source = """use recon/hosts/enum/dns/resolve\nrun\nexit\n
use recon/hosts/enum/http/api/builtwith\nrun\nexit\n
use recon/hosts/enum/http/api/punkspider\nrun\nexit\n
use recon/hosts/enum/http/api/wascompanyhacked\nrun\nexit\n
use recon/hosts/enum/http/api/whatweb\nrun\nexit\n
use recon/hosts/enum/http/api/whois_lookup\nrun\nexit\n
use recon/hosts/enum/http/web/age_analyzer\nrun\nexit\n
use recon/hosts/enum/http/web/asafaweb\nrun\nexit\n
use recon/hosts/enum/http/web/gender_analyzer\nrun\nexit\n
use recon/hosts/enum/http/web/ipvoid\nrun\nexit\n
use recon/hosts/enum/http/web/malwaredomain\nrun\nexit\n
use recon/hosts/enum/http/web/mywot\nrun\nexit\n
use recon/hosts/enum/http/web/netbios\nrun\nexit\n
use recon/hosts/enum/http/web/netcraft_history\nrun\nexit\n
use recon/hosts/enum/http/web/open_resolvers\nrun\nexit\n
use recon/hosts/enum/http/web/urlvoid\nrun\nexit\n
use recon/hosts/enum/http/web/web_archive\nrun\nexit\n
use recon/hosts/enum/http/web/xssed\nrun\nexit\nexit"""

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def hosts_geo(workspace):
    rec_source = """use recon/hosts/geo/http/api/hostip\nrun\nexit\n
use recon/hosts/geo/http/api/ipinfodb\nrun\nexit\n
use recon/hosts/geo/http/api/uniapple\nrun\nexit\n
use recon/hosts/geo/http/web/wigle\nrun\nexit\nexit"""

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def contacts_gather(workspace):
    rec_source = """use recon/contacts/gather/http/api/jigsaw/point_usage\nrun\nexit\n
use recon/contacts/gather/http/api/jigsaw/purchase_contact\nrun\nexit\n
use recon/contacts/gather/http/api/jigsaw/search_contacts\nrun\nexit\n
use recon/contacts/gather/http/api/linkedin_auth\nrun\nexit\n
use recon/contacts/gather/http/api/twitter\nrun\nexit\n
use recon/contacts/gather/http/api/whois_pocs\nrun\nexit\n
use recon/contacts/gather/http/web/jigsaw\nrun\n\nexit\n
use recon/contacts/gather/http/web/pgp_search\nrun\nexit\nexit"""

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def contacts_enum(workspace):
    rec_source = """use recon/contacts/enum/http/web/dev_diver\nrun\nexit\n
use recon/contacts/enum/http/web/namechk\nrun\nexit\n
use recon/contacts/enum/http/web/pwnedlist\nrun\nexit\n
use recon/contacts/enum/http/web/should_change_password\nrun\nexit\nexit"""

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def creds_gather(workspace):
    """must have access to the pwnedlist API for use"""
    rec_source = """use recon/creds/gather/http/api/pwnedlist/account_creds\nrun\nexit\n
    use recon/creds/gather/http/api/pwnedlist/api_usage\nrun\nexit\n
    use recon/creds/gather/http/api/pwnedlist/domain_creds\nrun\nexit\n
    use recon/creds/gather/http/api/pwnedlist/domain_ispwned\nrun\nexit\n
    use recon/creds/gather/http/api/pwnedlist/leaks_dump\nrun\nexit\n
    use recon/creds/gather/http/api/pwnedlist/leak_lookup\nrun\nexit\nexit"""

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


def creds_enum(workspace):
    rec_source = """use recon/creds/enum/http/api/leakdb\nrun\nexit\n
    use recon/creds/enum/http/api/noisette\nrun\nexit\nexit"""

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir(config["recon-ng/reconng_path"])
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp

def run_pushpin(workspace, lat, longi):
    rec_source = """set LATITUDE %f
    set LONGITUDE %f
    use recon/pushpin/flickr\nrun\nexit\n
    use recon/pushpin/picasa\nrun\nexit\n
    use recon/pushpin/shodan\nrun\nexit\n
    use recon/pushpin/twitter\nrun\nexit\n
    use recon/pushpin/youtube\nrun\nexit\nexit""" % (float(lat), float(longi))

    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf.write(rec_source)
    recfile = tf.name
    tf.close()
    os.chdir("/Users/dbressler/tools/recon-ng")
    rng_wrkspc = subprocess.Popen(["python", "recon-ng.py", "-w", workspace, "-r", recfile], stdout=subprocess.PIPE)
    outp = rng_wrkspc.stdout.read()
    os.chdir(cwd)
    return outp


# config["recon-ng/reconng_path"]
# "/Users/dbressler/tools/recon-ng"
# print run_pushpin('Test111', 39.1588, -75.4941)

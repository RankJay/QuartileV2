import subprocess
import time

def Activator():
    subprocess.Popen("pushd ./contracts/chainlink/scripts", shell=True)
    subprocess.Popen("brownie run ./price_feed_scripts/01_deploy_price_consumer_v3.py  --network kovan", shell=True)
    time.sleep(100)
    subprocess.Popen("brownie run ./price_feed_scripts/02_read_price_feed.py  --network kovan", shell=True)
    time.sleep(100)
    subprocess.Popen("brownie run ./price_feed_scripts/02_read_price_with_ens.py  --network kovan", shell=True)
    
    # subprocess.Popen("brownie run ./vrf_scripts/01_deploy_vrf.py  --network kovan", shell=True)
    # time.sleep(100)
    # # subprocess.Popen("brownie run ./vrf_scripts/fund_vrf.py  --network kovan", shell=True)
    # # time.sleep(100)
    # subprocess.Popen("brownie run  ./vrf_scripts/02_request_randomness.py  --network kovan", shell=True)
    # time.sleep(100)
    # subprocess.Popen("brownie run  ./vrf_scripts/03_read_random_number.py  --network kovan", shell=True)

    return

Activator()
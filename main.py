import asyncio
import time
from web3 import Web3
from functions import (
    approve,
    enroll,
    transfer,
    pool_tx,
    bsc_quest,
    claim_tasks,
    check_user_points,
    enroll_verify,
    btc_quest,
    eth_quest,
    bsc_izumi_quest,
)

RPC = "https://zetachain-evm.blockpi.network/v1/rpc/public"
web3 = Web3(Web3.HTTPProvider(RPC))
proxies = []

'''
with open("proxies.txt", "r") as p:
    for proxy in p:
        proxy = proxy.strip()
        proxies.append(proxy)
'''
workflow = [3, 4, 6, 7, 8, 9, 6, 5, 11, 10]


# workflow = [1,2]


def run_sync_in_executor(func, *args):
    loop = asyncio.get_event_loop()
    return loop.run_in_executor(None, func, *args)


async def handle_transaction(semaphore, key, workflow):
    async with semaphore:
        transaction_functions = {
            1: enroll,
            2: enroll_verify,
            3: transfer,
            4: bsc_quest,
            5: approve,
            6: pool_tx,
            7: btc_quest,
            8: eth_quest,
            9: bsc_izumi_quest,
            10: check_user_points,
            11: claim_tasks,
        }

        for num in workflow:
            try:
                func = transaction_functions[num]
                await run_sync_in_executor(func, key)
            except Exception as e:
                error_message = f"Error for address: {web3.eth.account.from_key(key).address} | Error: {e}\n"
                print(error_message)
                await asyncio.sleep(3)
                with open("fail_logs.txt", "a") as log_file:
                    log_file.write(error_message + f" ")


async def async_run(private_keys, workflow):
    # async core num
    semaphore = asyncio.Semaphore(20)
    tasks = []
    for key in private_keys:
        task = asyncio.create_task(handle_transaction(semaphore, key, workflow))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    print(
        "\n----------------------"
        "\n1: Enroll                    | +2000 XP ONCE"
        "\n2: Enroll verify             "
        "\n3: Send & Receive Zeta quest | +3500 XP"
        "\n4: Receive BNB in ZetaChain  | +2500 XP "
        "\n5: Approve BNB for LP transaction"
        "\n6: LP any core pool          | +5000 XP"
        "\n7: Receive BTC in Zetachain  | +2500 XP"
        "\n8: Receive ETH in Zetachain  | +2500 XP"
        "\n9: Receive BNB (Izumi)       | +2500 XP"
        "\n10: Check total XP|Rank|Level"
        "\n11: Claim all available tasks"
        "\n----------------------"
    )

    # load private keys
    private_keys = []
    with open("keys.txt", "r") as f:
        for line in f:
            line = line.strip()
            private_keys.append(line)

    asyncio.run(async_run(private_keys, workflow))

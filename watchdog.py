#!/usr/bin/env python

import GPUtil
import requests as r
from time import sleep
from os import environ as env

# CONFIG
SLEEP_DURATION = float(env.get("INTERVAL") or 10)
LIMIT_TRIGGER = float(env.get("LIMIT") or 0.99)
LOW_TRIGGER = float(env.get("LOW_LIMIT") or 0.1)
WEBHOOK_URL = env.get("WEBHOOK_URL")

if not WEBHOOK_URL or WEBHOOK_URL == "":
    print('YOU NEED A WEBHOOK URL. ENV VAR "WEBHOOK_URL" IS NULL OR NOTHING!')
    exit(1)

gpus = GPUtil.getGPUs()


def gen_payload(gpu):
    return {
        "content": f'**[WARNING]** `"{gpu.name}"#{gpu.id}` {gpu.memoryUtil * 100 : .2f}% | L: {LOW_TRIGGER * 100 : .2f} H: {LIMIT_TRIGGER * 100 : .2f}% !!! @everyone'
    }


if __name__ == "__main__":
    while True:
        for gpu in gpus:
            print(f"{gpu}: {gpu.memoryUtil * 100 : .2f}%")
            if gpu.memoryUtil >= LIMIT_TRIGGER or gpu.memoryUtil < LOW_TRIGGER:
                # send payload
                data = gen_payload(gpu)
                r.post(WEBHOOK_URL, json=data)
                
        sleep(SLEEP_DURATION)

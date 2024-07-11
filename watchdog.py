#!/usr/bin/env python

import GPUtil
import requests as r
from time import sleep
from os import environ as env

# CONFIG
SLEEP_DURATION = 10
LIMIT_TRIGGER = float(env.get("LIMIT") or 0.99)

WEBHOOK_URL = env.get("WEBHOOK_URL")

if not WEBHOOK_URL or WEBHOOK_URL == "":
    print('YOU NEED A WEBHOOK URL. ENV VAR "WEBHOOK_URL" IS NULL OR NOTHING!')
    exit(1)

gpus = GPUtil.getGPUs()


def gen_payload(gpu, limit_trigger: float):
    return {
        "content": f'**[WARNING]** `"{gpu.name}"#{gpu.id}` ( *{gpu.memoryUtil * 100 : .2f}%* ) >= {limit_trigger * 100 : .2f}% !!! @everyone'
    }


if __name__ == "__main__":
    while True:
        for gpu in gpus:
            print(f"{gpu}: {gpu.memoryUtil * 100 : .2f}%")
            if gpu.memoryUtil >= LIMIT_TRIGGER:
                # send payload
                data = gen_payload(gpu, LIMIT_TRIGGER)
                r.post(WEBHOOK_URL, json=data)

                # Also wake people up:
                for _ in range(4):
                    r.post(WEBHOOK_URL, json={"content": "@everyone !"})
        sleep(SLEEP_DURATION)

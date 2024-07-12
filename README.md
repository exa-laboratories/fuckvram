# Fuck VRAM
Tired of running out of VRAM when doing cool runs? Same.

![vram meme lmao](https://github.com/exa-laboratories/fuckvram/assets/38406360/935a3914-5202-471f-883c-c11d85b2d9f8)

Now, instead of waking up to realize that your GPU instance on [lambdalabs.com](https://lambdalabs.com) ran out of VRAM during a training run, you will be awakened by the constant spamming of the desired webhook!!11!!1

## Quickstart
### Bootstrapping an environment
If you want to bootstrap an environment, then copy-paste this and replace the desired webhook URL with your own.

It works great with Discord webhooks and probably with Slack too.
```sh
export WEBHOOK_URL=https://example.com/webhook 
export LIMIT=0.98
export LOW_LIMIT=0.08 
export INTERVAL=20 
curl -s https://raw.githubusercontent.com/exa-laboratories/fuckvram/main/bootstrap.sh | bash
```
### Else
Otherwise just clone the repo and run `watchdog.py`. Don't forget to set the `WEBHOOK_URL` environment variable.

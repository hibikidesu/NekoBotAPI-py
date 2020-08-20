from nekobot import NekoBotAsync
import asyncio


async def async_test():
    api = NekoBotAsync()
    img = (await api.get_image("neko")).message
    print("Image: {}".format(img))
    print("Threats: {}".format(await api.threats(img)))
    print("Baguette: {}".format(await api.baguette(img)))
    print("Clyde: {}".format(await api.clyde("owo")))
    print("Ship: {}".format(await api.ship(img, img)))
    print("Captcha: {}".format(await api.captcha(img, "hibiki")))
    print("whowouldwin: {}".format(await api.whowouldwin(img, img)))
    print("Changemymind: {}".format(await api.changemymind("baka")))
    print("ddlc: {}".format(await api.ddlc("m", "bedroom", "1", "1t", "baka")))
    print("jpeg: {}".format(await api.jpeg(img)))
    print("lolice: {}".format(await api.lolice(img)))
    print("kannagen: {}".format(await api.kannagen("baka")))
    print("iphonex: {}".format(await api.iphonex(img)))
    print("amimeface: {}".format(await api.animeface(img)))
    print("awooify: {}".format(await api.awooify(img)))
    print("trap: {}".format(await api.trap("hibiki", "abc", img)))
    print("trumptweet: {}".format(await api.trumptweet("owo")))
    print("tweet: {}".format(await api.tweet("hibikiqt", "owo")))
    print("deepfry: {}".format(await api.deepfry(img)))
    print("blurpify: {}".format(await api.blurpify(img)))
    print("phcomment: {}".format(await api.phcomment(img, "owo", "hibiki")))
    print("magik: {}".format(await api.magik(img)))
    print("trash: {}".format(await api.trash(img)))
    print("stickbug: {}".format(await api.stickbug(img)))
    await api.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_test())
    loop.close()

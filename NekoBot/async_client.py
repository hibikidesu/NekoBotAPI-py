from .client import BaseClass, Response
import asyncio
import aiohttp
import typing


class NekoBotAsync(BaseClass):

    def __init__(self, authorization: str = "", *, loop: asyncio.AbstractEventLoop = None):
        super().__init__(authorization)
        if loop is None:
            loop = asyncio.get_event_loop()
        self._http = aiohttp.ClientSession(
            loop=loop,
            headers={
                "User-Agent": self.user_agent,
                "Authorization": self.authorization
            }
        )

    async def close(self):
        await self._http.close()

    async def _request(self, path: str, params: dict) -> typing.Union[Response, bytes]:
        async with self._http.get(self.BASE_URL + path, params=params) as r:
            try:
                data = Response(**(await r.json()))
            except:
                data = await r.read()
        return data

    async def get_image(self, image_type: str) -> Response:
        """
        Get an image from the api
        :param image_type: https://docs.nekobot.xyz/#image-endpoints-image
        :return: JSON data from server
        """
        return await self._request("/image", {
            "type": image_type
        })

    async def threats(self, url: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param url: Image URL to add to template.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "threats",
            "url": url,
            "raw": str(int(raw))
        })

    async def baguette(self, url: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param url: Any image URL to generate, can be user avatar or anything.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "baguette",
            "url": url,
            "raw": str(int(raw))
        })

    async def clyde(self, text: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param text: Text to clydify.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "clyde",
            "text": text,
            "raw": str(int(raw))
        })

    async def ship(self, user1: str, user2: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param user1: User 1’s avatar
        :param user2: User 2’s avatar
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "ship",
            "user1": user1,
            "user2": user2,
            "raw": str(int(raw))
        })

    async def captcha(self, url: str, username: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param url: User’s avatar URL or any image.
        :param username: User’s username or or any other string to show up.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "captcha",
            "url": url,
            "username": username,
            "raw": str(int(raw))
        })

    async def whowouldwin(self, user1: str, user2: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param user1: User 1’s avatar
        :param user2: User 2’s avatar
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "whowouldwin",
            "user1": user1,
            "user2": user2,
            "raw": str(int(raw))
        })

    async def changemymind(self, text: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param text: Change my mind text.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "changemymind",
            "text": text,
            "raw": str(int(raw))
        })

    async def ddlc(self, character: str, background: str, body: str, face: str, text: str,
             *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param character: Can be either monika, yuri, natsuki, sayori or m, y, n , s
        :param background: Background of the image, types: bedroom, class, closet, club, corridor, house, kitchen,
            residential, sayori_bedroom
        :param body: Body of the character, there is only 1 or 2 for monika and 1, 1b, 2, 2b for the rest
        :param face: Face of the character to go with the body, is best to just see all the types at
            https://github.com/hibikidesu/NekoBot/blob/master/modules/fun.py#L14 (line14 to 34)
        :param text: Text for the character to say, max length of 140
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "ddlc",
            "character": character,
            "background": background,
            "body": body,
            "face": face,
            "text": text,
            "raw": str(int(raw))
        })

    async def jpeg(self, url: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param url: URL to JPEGify, would be recommended if the URL is as an JPEG or JPG format but PNG will still work
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "jpeg",
            "url": url,
            "raw": str(int(raw))
        })

    async def lolice(self, url: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param url: Lolice chief
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "lolice",
            "url": url,
            "raw": str(int(raw))
        })

    async def kannagen(self, text: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param text: Text to kannafy
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "kannagen",
            "text": text,
            "raw": str(int(raw))
        })

    async def iphonex(self, url: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param url: Image to fill into an iphone.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "iphonex",
            "url": url,
            "raw": str(int(raw))
        })

    async def animeface(self, image: str) -> typing.Union[Response, bytes]:
        """
        :param image: Image to find heccin weaboos
        :return:
        """
        return await self._request("/imagegen", {
            "type": "animeface",
            "image": image
        })

    async def awooify(self, url: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param url: Users avatar to AwOOOOify :3
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "awooify",
            "url": url,
            "raw": str(int(raw))
        })

    async def trap(self, name: str, author: str, image: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param name: User to trap.
        :param author: Author trapping user.
        :param image: Avatar’s URL to trap.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "trap",
            "name": name,
            "author": author,
            "image": image,
            "raw": str(int(raw))
        })

    async def trumptweet(self, text: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param text: Text to TrumpTweet
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "trumptweet",
            "text": text,
            "raw": str(int(raw))
        })

    async def tweet(self, username: str, text: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param username: Twitter Username without the @
        :param text: Text to tweet
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "tweet",
            "username": username,
            "text": text,
            "raw": str(int(raw))
        })

    async def deepfry(self, image: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param image: Image URL to DeepFry.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "deepfry",
            "image": image,
            "raw": str(int(raw))
        })

    async def blurpify(self, image: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param image: Image URL to Blurpify.
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "blurpify",
            "image": image,
            "raw": str(int(raw))
        })

    async def phcomment(self, image: str, text: str, username: str, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param image: User image URL
        :param text: Text to comment.
        :param username: User’s Username
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "phcomment",
            "image": image,
            "text": text,
            "username": username,
            "raw": str(int(raw))
        })

    async def magik(self, image: str, intensity: int = 5, *, raw: bool = False) -> typing.Union[Response, bytes]:
        """
        :param image: Image to magikify
        :param intensity: an integer of magik intensity from 0 to 10
        :param raw: Get raw image bytes
        :return:
        """
        return await self._request("/imagegen", {
            "type": "magik",
            "image": image,
            "intensity": intensity,
            "raw": str(int(raw))
        })

    async def trash(self, url: str) -> typing.Union[Response, bytes]:
        """
        :param url: URL of trash waifu
        :return:
        """
        return await self._request("/imagegen", {
            "type": "trash",
            "url": url
        })

    async def stickbug(self, url: str) -> typing.Union[Response, bytes]:
        """
        :param url: Image url for stickbug
        :return:
        """
        return await self._request("/imagegen", {
            "type": "stickbug",
            "url": url
        })

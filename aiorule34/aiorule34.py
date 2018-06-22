import aiohttp
import asyncio
from defusedxml.ElementTree import fromstring

class Rule34Image:
	def __init__(self,
				 **kwargs):
		self.url = kwargs['file_url']
		self.score = kwargs['score']
		self.tags = kwargs['tags'].split(' ')
		self.id = kwargs['id']
		self.date = kwargs['created_at']
		self.attribs = kwargs

async def rule34get(tags = None, limit: int = 50, pid: int = None) -> list:

	if not 1 <= limit <= 100:
		raise AttributeError('The page limit must be between 1 and 100')

	if isinstance(tags, list):
		tags = ' '.join(tags)

	if tags is None and pid is None:
		raise AttributeError('either tags or pid must be used')

	if pid is None:
		url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tags}&limit={limit}'.format(
			tags = tags,
			limit = limit
		)

	else:
		url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index&id={}'.format(pid)


	async with aiohttp.ClientSession() as session:
		async with session.get(url) as resp:
			root = fromstring(await resp.text())

			if not root and pid is None:
				raise AttributeError('Nothing with tags <{}> found'.format(tags))

			elif not root:
				raise AttributeError('No post with an id of <{}> found'.format(pid))

			ret = []
			for post in root:
				kwargs = post.attrib
				ret.append(Rule34Image(**kwargs))

			return ret

async def test():
	x = await r34get()
	for a in x:
		print(a.url)

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
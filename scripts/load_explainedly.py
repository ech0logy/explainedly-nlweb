"""Load Explainedly.net into NLWeb from the public Blogger sitemap."""

import asyncio
import os

from nlweb_dataload import load_sitemap


SITEMAP_URL = os.getenv("EXPLAINEDLY_SITEMAP", "https://www.explainedly.net/sitemap.xml")
SITE_NAME = os.getenv("NLWEB_SITE_NAME", "explainedly")


async def main():
    print(f"Loading {SITEMAP_URL} into NLWeb site '{SITE_NAME}'")
    result = await load_sitemap(SITEMAP_URL, site=SITE_NAME)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

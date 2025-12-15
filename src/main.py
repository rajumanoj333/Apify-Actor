from __future__ import annotations
import asyncio
import aiohttp
from apify import Actor

PLACES_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
PHOTO_URL = "https://maps.googleapis.com/maps/api/place/photo"

CATEGORIES = {
    "Engineering": "engineering college in Telangana",
    "Medical": "medical college in Telangana",
    "Degree": "degree college in Telangana",
    "Polytechnic": "polytechnic college in Telangana"
}


def extract_district(address: str) -> str | None:
    if not address:
        return None
    parts = address.split(",")
    for p in parts:
        if "district" in p.lower():
            return p.strip()
    return parts[-3].strip() if len(parts) >= 3 else None


async def fetch_places(session, api_key, query, page_token=None):
    params = {
        "query": query,
        "key": api_key
    }
    if page_token:
        params["pagetoken"] = page_token

    async with session.get(PLACES_URL, params=params) as resp:
        return await resp.json()


async def main() -> None:
    async with Actor:
        input_data = await Actor.get_input() or {}
        api_key = input_data["googleApiKey"]
        max_images = input_data.get("maxImages", 5)

        async with aiohttp.ClientSession() as session:
            for category, query in CATEGORIES.items():
                Actor.log.info(f"Fetching {category} colleges...")

                next_page_token = None
                while True:
                    data = await fetch_places(session, api_key, query, next_page_token)
                    results = data.get("results", [])

                    for college in results:
                        photos = college.get("photos", [])
                        image_urls = [
                            f"{PHOTO_URL}?maxwidth=800&photo_reference={p['photo_reference']}&key={api_key}"
                            for p in photos[:max_images]
                        ]

                        address = college.get("formatted_address", "")
                        district = extract_district(address)

                        record = {
                            "college_name": college.get("name"),
                            "category": category,
                            "district": district,
                            "address": address,
                            "google_maps_url": f"https://www.google.com/maps/place/?q=place_id:{college.get('place_id')}",
                            "latitude": college["geometry"]["location"]["lat"],
                            "longitude": college["geometry"]["location"]["lng"],
                            "rating": college.get("rating"),
                            "total_reviews": college.get("user_ratings_total"),
                            "google_images": image_urls
                        }

                        await Actor.push_data(record)

                    next_page_token = data.get("next_page_token")
                    if not next_page_token:
                        break

                    await asyncio.sleep(2)
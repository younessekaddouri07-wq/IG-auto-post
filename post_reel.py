import os
import requests

# Instagram API credentials (stored in GitHub Secrets)
ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")

# Repo video file
VIDEO_URL = "https://github.com/younessekaddouri07-wq/IG-auto-post/raw/refs/heads/main/video.mp4"

# Step 1: Read day number
with open("day.txt", "r") as f:
    day_number = int(f.read().strip())

caption = f"day {day_number}"

print(f"Uploading reel with caption: {caption}")

# Step 2: Create media container
url = f"https://graph.facebook.com/v23.0/{IG_USER_ID}/media"
params = {
    "media_type": "REELS",
    "video_url": VIDEO_URL,
    "caption": caption,
    "access_token": ACCESS_TOKEN
}
res = requests.post(url, params=params)
res.raise_for_status()
upload_id = res.json().get("id")

print(f"Media container created: {upload_id}")

# Step 3: Publish media
publish_url = f"https://graph.facebook.com/v23.0/{IG_USER_ID}/media_publish"
res = requests.post(publish_url, params={
    "creation_id": upload_id,
    "access_token": ACCESS_TOKEN
})
res.raise_for_status()
print(f"Published successfully: {res.json()}")

# Step 4: Increment day and save back
with open("day.txt", "w") as f:
    f.write(str(day_number + 1))

from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    
    parsed = urlparse(url)
    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed.query).get("v", [None])[0]
    elif parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")
    else:
        return None

def get_captions(video_url, lang="en"):
    
    video_id = get_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        text = " ".join([t["text"] for t in transcript])
        return text
    except Exception as e:
        return f"No captions available or error: {e}"


if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    captions = get_captions(video_url)
    print("\n--- Captions Preview (first 500 chars) ---\n")
    print(captions[:500])

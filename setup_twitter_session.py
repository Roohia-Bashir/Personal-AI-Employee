from playwright.sync_api import sync_playwright
import json
from pathlib import Path

SESSION_PATH = "./.twitter_session"
Path(SESSION_PATH).mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        SESSION_PATH,
        headless=False,
        args=["--no-sandbox"],
    )
    
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto("https://x.com/login")
    
    print("Browser mein login karo manually...")
    print("Home feed par aane ke baad Enter dabao...")
    input()
    
    cookies = browser.cookies()
    cookies_file = Path(SESSION_PATH) / "cookies.json"
    with open(cookies_file, "w") as f:
        json.dump(cookies, f, indent=2)
    
    print(f"Done! {len(cookies)} cookies save ho gayi: {cookies_file}")
    browser.close()
import requests
import os
import sys
import dotenv
import time
import logging
from googletrans import Translator


logging.basicConfig(level=logging.INFO)
dotenv.load_dotenv(override=True)
translator = Translator()


# System Variables (Weblate)
API_URL = (os.getenv("WEBALTE_URL").strip()).rstrip("/")
if not API_URL.endswith("/api"):
    API_URL += "/api"
WEBLATE_API_TOKEN = os.getenv("WEBLATE_API_TOKEN").strip()
if not WEBLATE_API_TOKEN:
    logging.error("Missing Weblate API token. Set WEBLATE_API_TOKEN in your environment/.env")
    sys.exit(1)
PROJECT_SLUG = os.getenv("WEBLATE_PROJECT_SLUG").strip()


# System Variables (DeepL)
DEEPL_API_TOKEN = os.getenv("DEEPL_API_TOKEN")
DEEPL_URL = os.getenv("DEEPL_URL")


# Headers (Weblate)
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Token {WEBLATE_API_TOKEN}",
}


# Changeable Variables
languages = ["ca", "es_CR", "en"]
do_translate = True


def get_paginated(url: str):
    """Helper to iterate through paginated Weblate results."""
    while url:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            # Yield each item in the results list
            yield from data.get("results", [])
            url = data.get("next")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            break


def translate_logic(source_text: str, target_lang: str, retries: int = 0, max_retries: int = 5):
    """Placeholder for your translation logic"""
    if not source_text:
        return None

    target_lang = target_lang.split("_")[0]

    if target_lang == 'ca':
        try:
            traduccion = translator.translate(source_text, dest="ca")
            return traduccion.text
        except Exception as e:
            logging.error(f"Error translating to Catalan '{source_text}': {e}")
            return None
    else:
        while retries <= max_retries:
            try:
                
                # Request payload
                data = {
                    "auth_key": DEEPL_API_TOKEN,
                    "text": source_text,
                    "target_lang": target_lang,
                }
                response = requests.post(DEEPL_URL, data=data)
                response.raise_for_status()
                return response.json()["translations"][0]["text"]
            except requests.exceptions.HTTPError as e:
                logging.error(e)
                if response.status_code == 429:
                    retries += 1
                    delay = 2 ** retries  # Exponential backoff
                    logging.warning(f"Rate limit exceeded when translating '{source_text}', retrying in {delay} seconds...")
                    time.sleep(delay)  # Wait before retrying
                elif 500 <= response.status_code < 600:
                    retries += 1
                    delay = 2 ** retries
                    logging.warning(f"Internal server error ({e}) when translating '{source_text}', retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    logging.error(f"HTTP error while translating '{source_text}': {e}")
                    error = f'ERROR::{e}'
                    return error
            except Exception as e:
                logging.error(f"Error translating '{source_text}': {str(e)}")
                error = f'ERROR::{e}'
                return error

        # If max retries are exceeded, print the error and return None
        logging.error(f"Max retries exceeded for translating '{source_text}'")
        return None
    

# STEP 1: Get components
components_url = f"{API_URL}/projects/{PROJECT_SLUG}/components/"

print(f"Fetching components from: {components_url}")

for i, comp in enumerate(get_paginated(components_url)):
    if i > 1: 
        break
        
    source_lang_obj = comp.get("source_language")
    original_lang_code = source_lang_obj.get("code") if source_lang_obj else "en"

    comp_slug = comp.get("slug")
    print(f"\n=== Component: {comp_slug}: {original_lang_code} ===")

    # STEP 2: Get languages (Statistics endpoint is good for getting the list)
    stats_url = f"{API_URL}/components/{PROJECT_SLUG}/{comp_slug}/statistics/"
    
    for lang_stats in get_paginated(stats_url):
        lang_code = lang_stats.get("code")
        
        if lang_code not in languages:
            continue
            
        print(f"\n   --- Language: {lang_code} ---")

        # STEP 3: Get the actual Translation Units (Strings)
        units_url = f"{API_URL}/translations/{PROJECT_SLUG}/{comp_slug}/{lang_code}/units/"
        
        for j, unit in enumerate(get_paginated(units_url)):
            if j > 2:
                break
            
            # Basic unit information
            source = unit.get("source")
            target = unit.get("target")
            unit_id = unit.get("id")
            state = unit.get("state", 0)
            unit_url = f"{API_URL}/units/{unit_id}/"

            if state in [100, 30]:
                continue

            # Target and original text
            current_translation = target[0] if target else None
            original_text = source[0] if source else None
            
            # Translate and update if target is empty OR if we force translation
            should_translate = not current_translation or do_translate
            new_translation = None
            if should_translate:
                new_translation = translate_logic(original_text, lang_code)
                payload = {"target": [new_translation], "state": 20}
                
                # UNCOMMENT TO APPLY CHANGES
                patch_response = requests.patch(unit_url, headers=headers, json=payload)
                if patch_response.status_code != 200:
                    if patch_response.status_code == 401:
                        logging.error("      Error patching: 401 Unauthorized. Set WEBLATE_API_TOKEN/WEBLATE_API_KEY and ensure it matches the target server URL.")
                    else:
                        logging.error(f"      Error patching: {patch_response.content}")

            # Debug print
            print(f"      Source: {original_text}...")
            if current_translation:
                print(f"      Target: {current_translation}...")
            if new_translation:
                print(f"      New Translation: {new_translation}")
            print("      ----")
    
commit_url = f"{API_URL}/components/{PROJECT_SLUG}/1-base-component/repository/"
print(f"commit_url: {commit_url}")
try:
    print(f"   [VCS] Attempting commit for {comp_slug}...")
    
    # CRITICAL FIX: You must send {"operation": "commit"}
    commit_payload = {"operation": "commit"} 
    
    resp = requests.post(commit_url, headers=headers, json=commit_payload)
    
    if resp.status_code == 200:
        # Weblate returns 200 even if it worked, we need to check the boolean 'result'
        if resp.json().get('result') is True:
            logging.info(f"      ✅ Commit success for {comp_slug}")
        else:
            # result: False usually means "Nothing to commit"
            logging.info(f"      ⚠️  Weblate says: Nothing to commit (Changes might already be auto-committed).")

    elif resp.status_code == 423:
        logging.warning(f"      🔒 Repository is locked (Another operation is in progress).")
    else:
        logging.error(f"      ❌ Error {resp.status_code}: {resp.text}")

except Exception as e:
    logging.error(f"      Failed to connect: {e}")
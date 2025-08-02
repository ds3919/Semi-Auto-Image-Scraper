import pandas as pd
import sys
import pyperclip
import time

# Configuration
INPUT_CSV = sys.argv[1]
WORD_COLUMN = sys.argv[2]
URL_PREFIX = "https://pixabay.com/vectors/search/"  # Can change to any image search prefix
OUTPUT_CSV = "scraped_images.csv"
POLL_INTERVAL = 1.0  
IMAGES_PER_WORD = int(sys.argv[3])

#reset clipboard for next link
def clear_clipboard():
    pyperclip.copy("")  # clears clipboard content

def main():
    df = pd.read_csv(INPUT_CSV)
    output_data = []

    print("Starting automatic image collector.")
    print(f"Collecting {IMAGES_PER_WORD} image URLs per word...\n")

    for word in df[WORD_COLUMN]:
        print(f"\n=== WORD: {word} ===")
        print(f"{URL_PREFIX + word}")
        print("Copy image URLs to clipboard. Script is listening...")

        seen = set()
        image_count = 0
        last_clipboard = ""

        while image_count < IMAGES_PER_WORD:
            clipboard = pyperclip.paste().strip()

            if clipboard != last_clipboard and clipboard.startswith("http"):
                if clipboard not in seen:
                    output_data.append({"word": word, "image_url": clipboard})
                    seen.add(clipboard)
                    image_count += 1
                    print(f"[{image_count}/{IMAGES_PER_WORD}] {clipboard}")
                last_clipboard = clipboard

            time.sleep(POLL_INTERVAL)

        print(f"Collected {IMAGES_PER_WORD} images for '{word}'")
        clear_clipboard()

    print("\n Saving results...")
    pd.DataFrame(output_data).to_csv(OUTPUT_CSV, index=False)
    print(f"Done! Data saved to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()

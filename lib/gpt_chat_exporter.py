import json
from playwright.sync_api import sync_playwright


def extract_chat_from_share_url(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")  # Wait for page to be relatively stable

        chat = []
        # Find all message containers
        message_elements = page.locator("div[data-message-author-role]")

        for i in range(message_elements.count()):
            element = message_elements.nth(i)
            role = element.get_attribute("data-message-author-role")
            content = ""

            if role == "assistant":
                # Assistant messages have content in a 'div.markdown.prose'
                content_element = element.locator("div.markdown.prose")
                if content_element.count() > 0:
                    content = content_element.inner_text()
            elif role == "user":
                # User messages have content in a 'div.whitespace-pre-wrap'
                content_element = element.locator("div.whitespace-pre-wrap")
                if content_element.count() > 0:
                    content = content_element.inner_text()

            if role and content:  # Ensure we have a role and some content
                chat.append({"role": role.strip(), "content": content.strip()})

        browser.close()
        return chat


def import_chat(url):
    chat_history = extract_chat_from_share_url(url)

    for entry in chat_history:
        content = str(entry["content"])
        entry["content"] = (
            content.replace("\n\n", " ")
            .replace("\n", "")
            .replace("  ", "")
            .replace('"', "")
        )

    return json.dumps(chat_history, indent=2)

#!/usr/bin/env python3
import os
import re
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from markdownify import markdownify as md
from urllib.parse import urlparse
import time

def fetch_sitemap(sitemap_url):
    """Fetch sitemap.xml and return list of URLs."""
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        
        # Handle namespace
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        urls = []
        for url_elem in root.findall('ns:url', namespaces):
            loc_elem = url_elem.find('ns:loc', namespaces)
            if loc_elem is not None:
                url = loc_elem.text.strip()
                # Filter for blog post URLs (containing /p/)
                if '/p/' in url:
                    urls.append(url)
        
        return urls
    except Exception as e:
        print(f"Error fetching sitemap {sitemap_url}: {e}")
        return []

def extract_article_slug(url):
    """Extract article slug from URL path."""
    parsed = urlparse(url)
    path = parsed.path
    match = re.search(r'/p/([^/?]+)', path)
    if match:
        return match.group(1)
    return None

def fetch_article_content(url):
    """Fetch article content from URL and extract title, subtitle, and body."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title_elem = soup.find('h1', class_='post-title published')
        title = title_elem.get_text().strip() if title_elem else ''
        
        # Extract subtitle
        subtitle_elem = soup.find('h3', class_='subtitle')
        subtitle = subtitle_elem.get_text().strip() if subtitle_elem else ''
        
        # Extract body
        body_elem = soup.find('div', class_='body markup')
        body_html = str(body_elem) if body_elem else ''
        body_markdown = md(body_html) if body_html else ''
        
        return {
            'title': title,
            'subtitle': subtitle,
            'body': body_markdown,
            'url': url
        }
    except Exception as e:
        print(f"Error fetching article {url}: {e}")
        return None

def save_article(article_data, slug):
    """Save article to markdown file in article folder."""
    if not os.path.exists('article'):
        os.makedirs('article')
    
    filename = f"article/{slug}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {article_data['title']}\n\n")
        if article_data['subtitle']:
            f.write(f"## {article_data['subtitle']}\n\n")
        f.write(f"**URL:** {article_data['url']}\n\n")
        f.write("---\n\n")
        f.write(article_data['body'])
    
    print(f"Saved: {filename}")

def main():
    # Request sitemap URL from user
    print("🔗 Article Scraper - Sitemap Mode")
    print("=" * 40)
    sitemap_url = input("Enter sitemap.xml URL: ").strip()
    
    if not sitemap_url:
        print("❌ No sitemap URL provided. Exiting...")
        return
    
    print(f"\n📥 Fetching sitemap from: {sitemap_url}")
    urls = fetch_sitemap(sitemap_url)
    
    if not urls:
        print("❌ No article URLs found in sitemap")
        return
    
    print(f"✅ Found {len(urls)} article URLs")
    
    # Ask for confirmation
    confirm = input(f"\nProceed to scrape {len(urls)} articles? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("❌ Operation cancelled")
        return
    
    print(f"\n🚀 Starting article processing...")
    print("-" * 40)
    
    successful = 0
    failed = 0
    
    for i, article_url in enumerate(urls, 1):
        slug = extract_article_slug(article_url)
        
        if not slug:
            print(f"⚠️  [{i}/{len(urls)}] Could not extract slug from URL: {article_url}")
            failed += 1
            continue
        
        print(f"📄 [{i}/{len(urls)}] Processing: {slug}")
        
        article_data = fetch_article_content(article_url)
        if article_data:
            save_article(article_data, slug)
            successful += 1
            print(f"✅ [{i}/{len(urls)}] Saved: {slug}.md")
        else:
            failed += 1
            print(f"❌ [{i}/{len(urls)}] Failed to process: {slug}")
        
        # Be nice to the server
        time.sleep(1)
    
    print("\n" + "=" * 40)
    print(f"🎉 Processing completed!")
    print(f"✅ Successfully processed: {successful} articles")
    print(f"❌ Failed: {failed} articles")
    print(f"📁 Articles saved in: ./article/ directory")

if __name__ == "__main__":
    main()
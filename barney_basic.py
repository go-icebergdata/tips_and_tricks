#!/usr/bin/env python3
"""
🍺 Barney Simpson: Basic Scraper (Gets Kicked Out by Moe)

This is your typical 2015-era scraper with static headers.
Moe (anti-bot systems) can spot this guy from a mile away.
"""

import requests
import time
from fake_useragent import UserAgent
from rich.console import Console
from rich.panel import Panel

console = Console()

class BarneyBasicScraper:
    """Basic scraper that Moe easily detects and kicks out"""
    
    def __init__(self):
        # Old school: just slap on some headers and hope for the best
        ua = UserAgent()
        self.headers = {
            'User-Agent': ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def test_fingerprint_site(self, url="https://tls.browserleaks.com/json"):
        """Test against a fingerprint detection site"""
        console.print("\n[bold red]🍺 Barney's Basic Approach[/bold red]")
        console.print("Using static headers like it's 2015...")
        
        try:
            response = self.session.get(url, timeout=10)
            
            console.print(f"[green]✓ Status Code:[/green] {response.status_code}")
            console.print(f"[yellow]Headers sent:[/yellow]")
            
            for key, value in self.headers.items():
                console.print(f"  {key}: {value}")
            
            # Try to parse response
            if response.headers.get('content-type', '').startswith('application/json'):
                data = response.json()
                console.print(f"\n[cyan]Server detected TLS fingerprint:[/cyan]")
                console.print(f"  JA3: {data.get('ja3_hash', 'Unknown')}")
                console.print(f"  User Agent: {data.get('user_agent', 'Unknown')}")
            
            return response
            
        except Exception as e:
            console.print(f"[red]❌ Request failed:[/red] {str(e)}")
            return None
    
    def test_httpbin_headers(self):
        """Test what headers actually get sent"""
        console.print("\n[bold yellow]🔍 Testing Header Detection[/bold yellow]")
        
        try:
            response = self.session.get("https://httpbin.org/headers", timeout=10)
            data = response.json()
            
            console.print("[cyan]Headers as seen by server:[/cyan]")
            for key, value in data.get('headers', {}).items():
                console.print(f"  {key}: {value}")
                
            return response
            
        except Exception as e:
            console.print(f"[red]❌ Header test failed:[/red] {str(e)}")
            return None
    
    def scrape_example_site(self, url="https://httpbin.org/user-agent"):
        """Example scraping attempt"""
        console.print(f"\n[bold blue]🎯 Attempting to scrape: {url}[/bold blue]")
        
        try:
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                console.print("[green]✓ Request successful![/green]")
                
                if 'json' in response.headers.get('content-type', ''):
                    data = response.json()
                    console.print(f"Server sees our User-Agent as: {data.get('user-agent')}")
                else:
                    console.print(f"Response: {response.text[:200]}...")
            else:
                console.print(f"[red]❌ Request blocked! Status: {response.status_code}[/red]")
                
            return response
            
        except Exception as e:
            console.print(f"[red]❌ Scraping failed:[/red] {str(e)}")
            return None

def main():
    """Demonstrate Barney's basic scraping approach"""
    
    console.print(Panel.fit(
        "[bold red]🍺 Barney Simpson: Basic Scraper Demo[/bold red]\n"
        "[yellow]Using 2015-era static headers...[/yellow]\n"
        "[dim]Spoiler: Moe is about to kick us out! 🚫[/dim]",
        title="Basic Scraper",
        border_style="red"
    ))
    
    scraper = BarneyBasicScraper()
    
    # Test 1: Check our fingerprint
    scraper.test_fingerprint_site()
    
    time.sleep(1)
    
    # Test 2: See what headers we're actually sending
    scraper.test_httpbin_headers()
    
    time.sleep(1)
    
    # Test 3: Try scraping
    scraper.scrape_example_site()
    
    console.print(Panel.fit(
        "[bold red]🚫 RESULT: DETECTED & BLOCKED[/bold red]\n"
        "[yellow]Why Barney gets caught:[/yellow]\n"
        "• Static headers that don't match real browsers\n"
        "• Missing TLS fingerprint consistency\n"
        "• No JavaScript execution environment\n"
        "• Predictable request patterns\n\n"
        "[dim]Time for Barney to get a disguise! 🥸[/dim]",
        title="Detection Summary",
        border_style="red"
    ))

if __name__ == "__main__":
    main() 